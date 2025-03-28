import os
import shutil
import tempfile
from pathlib import Path

import numpy as np
import pytest

from modyn.common.trigger_sample.trigger_sample_storage import TriggerSampleStorage

TMP_DIR = tempfile.mkdtemp()


@pytest.fixture(autouse=True)
def setup_and_teardown():
    Path(TMP_DIR).mkdir(parents=True, exist_ok=True)

    yield

    shutil.rmtree(TMP_DIR)


def test_save_trigger_sample():
    TriggerSampleStorage(TMP_DIR).save_trigger_samples(
        1, 2, 3, np.array([(1, 1.0), (2, 2.0)], dtype=np.dtype("i8,f8")), [2]
    )

    samples = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3)

    assert len(samples) == 2
    assert samples[0][0] == 1
    assert samples[0][1] == 1.0
    assert samples[1][0] == 2
    assert samples[1][1] == 2.0


def test_save_trigger_samples():
    TriggerSampleStorage(TMP_DIR).save_trigger_samples(
        1, 2, 3, np.array([(1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0), (5, 5.0)], dtype=np.dtype("i8,f8")), [3, 2]
    )

    samples = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3)

    assert len(samples) == 5
    assert samples[0][0] == 1
    assert samples[0][1] == 1.0
    assert samples[1][0] == 2
    assert samples[1][1] == 2.0
    assert samples[2][0] == 3
    assert samples[2][1] == 3.0
    assert samples[3][0] == 4
    assert samples[3][1] == 4.0
    assert samples[4][0] == 5
    assert samples[4][1] == 5.0


def test_get_file_size():
    TriggerSampleStorage(TMP_DIR).save_trigger_samples(
        1, 2, 3, np.array([(1, 1.0), (2, 2.0)], dtype=np.dtype("i8,f8")), [2]
    )

    file_path = Path(TMP_DIR) / "1_2_3_0.npy"
    TriggerSampleStorage(TMP_DIR)._get_num_samples_in_file(file_path)


def test_parse_file():
    TriggerSampleStorage(TMP_DIR).save_trigger_samples(
        1, 2, 3, np.array([(1, 1.0), (2, 2.0)], dtype=np.dtype("i8,f8")), [2]
    )
    file_path = Path(TMP_DIR) / "1_2_3_0.npy"

    samples = TriggerSampleStorage(TMP_DIR).parse_file(file_path)
    assert len(samples) == 2
    assert samples[0][0] == 1
    assert samples[0][1] == 1.0
    assert samples[1][0] == 2
    assert samples[1][1] == 2.0

    file_path.unlink()

    TriggerSampleStorage(TMP_DIR).save_trigger_samples(
        1, 2, 3, np.array([(1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0)], dtype=np.dtype("i8,f8")), [4]
    )

    samples = TriggerSampleStorage(TMP_DIR).parse_file(file_path)
    assert len(samples) == 4
    assert samples[0][0] == 1
    assert samples[0][1] == 1.0
    assert samples[1][0] == 2
    assert samples[1][1] == 2.0
    assert samples[2][0] == 3
    assert samples[2][1] == 3.0
    assert samples[3][0] == 4
    assert samples[3][1] == 4.0


def test_get_trigger_samples():
    expected_order = np.array(
        [
            (1, 1.0),
            (2, 2.0),
            (3, 3.0),
            (4, 4.0),
            (3, 3.0),
            (4, 4.0),
            (5, 5.0),
            (6, 6.0),
            (7, 7.0),
            (8, 8.0),
            (8, 8.0),
            (8, 8.0),
            (9, 9.0),
            (10, 10.0),
            (11, 11.0),
            (12, 12.0),
        ],
        dtype=np.dtype("i8,f8"),
    )
    TriggerSampleStorage(TMP_DIR).save_trigger_samples(1, 2, 3, expected_order, [4, 4, 4, 4])

    assert (TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3) == expected_order).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 0, 4, 16)
    assert len(result) == 4
    assert (result == expected_order[0:4]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 1, 4, 16)
    assert len(result) == 4
    assert (result == expected_order[4:8]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 2, 4, 16)
    assert len(result) == 4
    assert (result == expected_order[8:12]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 3, 4, 16)
    assert len(result) == 4
    assert (result == expected_order[12:16]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 0, 3, 16)
    assert len(result) == 6
    assert (result == expected_order[0:6]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 2, 3, 16)
    assert len(result) == 5
    assert (result == expected_order[11:16]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 0, 1, 16)
    assert len(result) == 16
    assert (result == expected_order).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 9, 10, 16)
    assert len(result) == 1
    assert result == expected_order[15]


def test_extended_get_trigger_samples():
    expected_order = np.array(
        [
            (1, 1.0),
            (2, 2.0),
            (3, 3.0),
            (4, 4.0),
            (3, 3.0),
            (4, 4.0),
            (5, 5.0),
            (6, 6.0),
            (7, 7.0),
            (8, 8.0),
            (9, 9.0),
            (10, 10.0),
            (11, 11.0),
        ],
        dtype=np.dtype("i8,f8"),
    )

    TriggerSampleStorage(TMP_DIR).save_trigger_samples(1, 2, 3, expected_order, [4, 4, 5])

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 0, 2, 12)
    assert len(result) == 6
    assert (result == expected_order[0:6]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 1, 3, 12)
    assert len(result) == 4
    assert (result == expected_order[4:8]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 2, 3, 12)
    assert len(result) == 4
    assert (result == expected_order[8:12]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 0, 12, 12)
    assert len(result) == 1
    assert result == expected_order[0]

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 1, 5, 12)
    assert len(result) == 3
    assert (result == expected_order[3:6]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 2, 5, 12)
    assert len(result) == 2
    assert (result == expected_order[6:8]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 3, 5, 12)
    assert len(result) == 2
    assert (result == expected_order[8:10]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 4, 5, 12)
    assert len(result) == 2
    assert (result == expected_order[10:12]).all()

    result = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, -1, -1, 13)
    assert len(result) == 13
    assert (result == expected_order).all()


def test_get_trigger_samples_no_file():
    tmp = TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3)
    assert not tmp


def test_get_trigger_samples_illegal_workers():
    with pytest.raises(AssertionError):
        TriggerSampleStorage(TMP_DIR).get_trigger_samples(1, 2, 3, 0, -1, 2)


def test_init_directory():
    os.rmdir(TMP_DIR)
    _ = TriggerSampleStorage(TMP_DIR)

    assert os.path.exists(TMP_DIR)
