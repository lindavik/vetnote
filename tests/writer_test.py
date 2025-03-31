import os
import json
import pytest
from vetnote.writer import write_discharge_note_to_file

TEST_OUTPUT_DIR = "tests/solution"


@pytest.fixture
def test_file_path():
    return os.path.join(TEST_OUTPUT_DIR, "test_discharge_note.json")


@pytest.fixture
def discharge_note():
    return {"discharge_note": "This is a test discharge note."}


def setup_function():
    if not os.path.exists(TEST_OUTPUT_DIR):
        os.makedirs(TEST_OUTPUT_DIR)


def teardown_function():
    test_file_path = os.path.join(TEST_OUTPUT_DIR, "test_discharge_note.json")
    if os.path.exists(test_file_path):
        os.remove(test_file_path)
    if os.path.exists(TEST_OUTPUT_DIR) and not os.listdir(TEST_OUTPUT_DIR):
        os.rmdir(TEST_OUTPUT_DIR)


def test_write_discharge_note_to_file(test_file_path, discharge_note):
    write_discharge_note_to_file(discharge_note, test_file_path)
    assert os.path.exists(test_file_path)

    with open(test_file_path, "r") as file:
        content = json.load(file)
        assert content == discharge_note


def test_write_discharge_note_to_file_exception(discharge_note):
    with pytest.raises(Exception):
        write_discharge_note_to_file(discharge_note, "/invalid_path/test_discharge_note.json")
