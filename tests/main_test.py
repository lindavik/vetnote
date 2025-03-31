import json
import os
import sys
from unittest.mock import patch, MagicMock
import pytest
from vetnote.main import main, OUTPUT_DIR


def teardown_function():
    output_file_path = os.path.join(OUTPUT_DIR, "sample.json")
    if os.path.exists(output_file_path):
        os.remove(output_file_path)


def test_main_no_arguments(capsys):
    with patch.object(sys, "argv", ["main.py"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
    captured = capsys.readouterr()

    assert "Usage: python main.py <input_file_path>" in captured.out
    assert excinfo.value.code == 1


def test_main_file_not_found(capsys):
    with patch.object(sys, "argv", ["main.py", "non_existent_file.json"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
    captured = capsys.readouterr()

    assert "An exception occurred while reading the input files" in captured.out
    assert excinfo.value.code == 1


def test_main_valid_file(capsys, tmp_path):
    temp_file = tmp_path / "sample.json"
    temp_file.write_text('{"consultation": "Sample input text"}')
    mock_llm_client = MagicMock()
    mock_note_generator = MagicMock()
    mock_note_generator.generate_discharge_notes.return_value = {"discharge_note": "Test note"}

    with patch.object(sys, "argv", ["main.py", str(temp_file)]):
        with patch(
            "vetnote.main.FileReader.read_file",
            return_value='{"consultation": "Sample input text"}',
        ):
            with patch("vetnote.main.OpenAIClient", return_value=mock_llm_client):
                with patch("vetnote.main.NoteGenerator", return_value=mock_note_generator):
                    main()

    captured = capsys.readouterr()
    output_file_path = os.path.join("solution", "sample.json")

    assert (
        "Discharge note below\n{'discharge_note': 'Test note'}"
        "\nDischarge note saved to solution/sample.json\n"
        in captured.out
    )
    assert os.path.exists(output_file_path)
    with open(output_file_path, "r") as file:
        content = file.read()
        assert json.loads(content) == {"discharge_note": "Test note"}
