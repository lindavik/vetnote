import sys
from unittest.mock import patch
import pytest
from vetnote.main import main


def test_main_no_arguments(capsys):
    with patch.object(sys, "argv", ["main.py"]):
        with pytest.raises(SystemExit) as excinfo:
            main()
    captured = capsys.readouterr()

    assert "Usage: python main.py <input_file_path>" in captured.out
    assert excinfo.value.code == 1


def test_main_file_not_found(capsys):
    with patch.object(sys, "argv", ["main.py", "non_existent_file.json"]):
        main()
    captured = capsys.readouterr()

    assert "File 'non_existent_file.json' not found." in captured.out


def test_main_valid_file(capsys, tmp_path):
    temp_file = tmp_path / "sample.json"
    temp_file.write_text('{"key": "value"}')

    with patch.object(sys, "argv", ["main.py", str(temp_file)]):
        main()

    captured = capsys.readouterr()

    assert '{"key": "value"}' in captured.out
