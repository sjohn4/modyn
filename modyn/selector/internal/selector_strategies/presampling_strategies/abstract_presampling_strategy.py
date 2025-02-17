from abc import ABC, abstractmethod

from sqlalchemy import Select

from modyn.config.schema.pipeline import PresamplingConfig
from modyn.selector.internal.storage_backend.abstract_storage_backend import AbstractStorageBackend


class AbstractPresamplingStrategy(ABC):
    def __init__(
        self,
        presampling_config: PresamplingConfig,
        modyn_config: dict,
        pipeline_id: int,
        storage_backend: AbstractStorageBackend,
    ):
        self.modyn_config = modyn_config
        self.pipeline_id = pipeline_id
        self._storage_backend = storage_backend
        self.presampling_ratio = presampling_config.ratio
        self.ratio_max = presampling_config.ratio_max
        self.requires_trigger_dataset_size = False

    @abstractmethod
    def get_presampling_query(
        self,
        next_trigger_id: int,
        tail_triggers: int | None,
        limit: int | None,
        trigger_dataset_size: int | None,
    ) -> Select:
        """This abstract class should return the query to get the presampled
        samples.

        The query should have only SelectorStateMetadata.sample_key in
        the SELECT clause.
        """
        raise NotImplementedError()

    def get_target_size(self, trigger_dataset_size: int, limit: int | None) -> int:
        assert trigger_dataset_size >= 0
        target_presampling = (trigger_dataset_size * self.presampling_ratio) // self.ratio_max

        if limit is not None:
            assert limit >= 0
            target_size = min(limit, target_presampling)
        else:
            target_size = target_presampling

        return target_size
