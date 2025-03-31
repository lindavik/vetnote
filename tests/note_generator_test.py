from unittest.mock import MagicMock, patch

import pytest

from vetnote.llm_client import LLMClient
from vetnote.note_generator import NoteGenerator


@pytest.fixture
def mock_llm_client():
    return MagicMock(spec=LLMClient)


@pytest.fixture
def note_generator(mock_llm_client):
    with patch("vetnote.reader.FileReader.read_file", return_value="Test instructions"):
        return NoteGenerator(llm_client=mock_llm_client, instruction_file_path="dummy_path")


def test_generate_discharge_notes_valid_response(note_generator, mock_llm_client):
    mock_llm_client.predict.return_value = '{"discharge_note": "Test note"}'
    input_text = "Test input"
    result = note_generator.generate_discharge_notes(input_text)
    assert result == {"discharge_note": "Test note"}


def test_generate_discharge_notes_invalid_response(note_generator, mock_llm_client):
    mock_llm_client.predict.return_value = '{"invalid_key": "Test note"}'
    input_text = "Test input"
    with pytest.raises(Exception, match="Invalid response format: 'discharge_note' key is missing"):
        note_generator.generate_discharge_notes(input_text)


def test_generate_discharge_notes_malformed_json(note_generator, mock_llm_client):
    mock_llm_client.predict.return_value = "Invalid JSON response"
    input_text = "Test input"
    with pytest.raises(Exception, match="No JSON found in the response"):
        note_generator.generate_discharge_notes(input_text)


def test_generate_discharge_notes_exception(note_generator, mock_llm_client):
    mock_llm_client.predict.side_effect = Exception("LLM error")
    input_text = "Test input"
    with pytest.raises(Exception, match="An exception occurred while calling the LLM"):
        note_generator.generate_discharge_notes(input_text)
