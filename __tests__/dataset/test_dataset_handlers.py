import pytest
from dataset.dataset_handlers import (
    get_dataset_handler_by_name,
    DatasetHandler,
    HumanEvalV2,
    SALLM,
)


def test_get_dataset_handler_by_name_human_eval_v2():
    # Arrange & Act
    handler = get_dataset_handler_by_name("HumanEvalV2")
    # Assert
    assert isinstance(handler, DatasetHandler)
    assert handler.dataset_path == "dataset/dataset_dump/human-eval-v2.json"
    assert handler.dataset_structure == HumanEvalV2


def test_get_dataset_handler_by_name_sallm():
    # Arrange & Act
    handler = get_dataset_handler_by_name("SALLM")
    # Assert
    assert isinstance(handler, DatasetHandler)
    assert handler.dataset_path == "dataset/dataset_dump/SALLM.json"
    assert handler.dataset_structure == SALLM


def test_get_dataset_handler_by_name_invalid():
    # Arrange & Act
    with pytest.raises(SystemExit) as excinfo:
        get_dataset_handler_by_name("invalid_dataset")
    # Assert
    assert excinfo.value.code == 1
