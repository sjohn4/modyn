from types import TracebackType

import torch

from modyn.common.benchmark import Stopwatch


class GPUMeasurement:
    def __init__(  # type: ignore[no-untyped-def]
        self, enabled: bool, measurement_name: str, device: str, stop_watch: Stopwatch, **kwargs
    ) -> None:
        self._device = device
        self._enabled = enabled
        self._measurement_name = measurement_name
        self._kwargs = kwargs
        self._stop_watch = stop_watch

    def __enter__(self) -> None:
        if self._enabled:
            torch.cuda.synchronize(device=self._device)
        self._stop_watch.start(name=self._measurement_name, **self._kwargs)

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        ex_traceback: TracebackType | None,
    ) -> None:
        if self._enabled:
            torch.cuda.synchronize(device=self._device)
        self._stop_watch.stop(name=self._measurement_name)
