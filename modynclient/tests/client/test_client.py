from unittest.mock import MagicMock, patch

from modynclient.client import Client
from modynclient.client.internal.grpc_handler import GRPCHandler

PIPELINE_ID = 42


def get_minimal_pipeline_config() -> dict:
    return {
        "pipeline": {"name": "Test"},
        "model": {"id": "ResNet18"},
        "model_storage": {"full_model_strategy": {"name": "PyTorchFullModel"}},
        "training": {
            "gpus": 1,
            "device": "cpu",
            "dataloader_workers": 1,
            "use_previous_model": True,
            "initial_model": "random",
            "initial_pass": {"activated": False},
            "batch_size": 42,
            "optimizers": [
                {"name": "default1", "algorithm": "SGD", "source": "PyTorch", "param_groups": [{"module": "model"}]},
            ],
            "optimization_criterion": {"name": "CrossEntropyLoss"},
            "checkpointing": {"activated": False},
            "selection_strategy": {"name": "NewDataStrategy", "maximum_keys_in_memory": 10},
        },
        "data": {"dataset_id": "test", "bytes_parser_function": "def bytes_parser_function(x):\n\treturn x"},
        "trigger": {"id": "DataAmountTrigger", "trigger_config": {"data_points_for_trigger": 1}},
    }


def get_minimal_evaluation_config() -> dict:
    return {
        "handlers": [
            {
                "execution_time": "after_training",
                "strategy": {
                    "name": "SlicingEvalStrategy",
                    "config": {
                        "eval_every": "100s",
                        "eval_start_from": 0,
                        "eval_end_at": 300,
                    },
                },
                "models": "matrix",
                "datasets": ["MNIST_eval"],
            }
        ],
        "device": "cpu",
        "datasets": [
            {
                "dataset_id": "MNIST_eval",
                "bytes_parser_function": "def bytes_parser_function(data: bytes) -> bytes:\n\treturn data",
                "dataloader_workers": 2,
                "batch_size": 64,
                "metrics": [{"name": "Accuracy"}],
            }
        ],
    }


def get_minimal_system_config() -> dict:
    return {}


def noop_constructor_mock(
    self,
    client_config: dict,
    pipeline_config: dict,
    start_replay_at: int | None = None,
    stop_replay_at: int | None = None,
    maximum_triggers: int | None = None,
) -> None:
    pass


def sleep_mock(duration: int):
    raise KeyboardInterrupt


@patch.object(GRPCHandler, "init_supervisor", return_value=None)
@patch("modyn.utils.grpc_connection_established", return_value=True)
def get_non_connecting_client(
    test_connection_established,
    test_init_supervisor,
) -> Client:
    client = Client(get_minimal_system_config(), get_minimal_pipeline_config())
    return client


def test_initialization() -> None:
    get_non_connecting_client()  # pylint: disable=no-value-for-parameter


@patch.object(GRPCHandler, "start_pipeline", return_value={"pipeline_id": PIPELINE_ID})
def test_start_pipeline(test_start_pipeline: MagicMock):
    client = get_non_connecting_client()  # pylint: disable=no-value-for-parameter
    started = client.start_pipeline()

    test_start_pipeline.assert_called_once_with(get_minimal_pipeline_config(), None, None, None)
    assert started is True
    assert client.pipeline_id == PIPELINE_ID


@patch.object(GRPCHandler, "start_pipeline", return_value={"pipeline_id": -1, "exception": "an error"})
def test_start_pipeline_failed(test_start_pipeline: MagicMock):
    client = get_non_connecting_client()  # pylint: disable=no-value-for-parameter
    started = client.start_pipeline()

    test_start_pipeline.assert_called_once_with(get_minimal_pipeline_config(), None, None, None)
    assert started is False
    assert client.pipeline_id is None
