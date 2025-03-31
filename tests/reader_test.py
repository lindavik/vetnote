import os
import pytest
from vetnote.reader import FileReader


class TestFileReader:

    @pytest.fixture
    def file_reader(self) -> FileReader:
        return FileReader()

    @pytest.fixture
    def expected_file_content(self):
        return (
            "{\n"
            '  "patient": {\n'
            '    "name": "Darth Vader",\n'
            '    "species": "Dog (Canine - Domestic)",\n'
            '    "breed": "Chiuaua",\n'
            '    "gender": "male",\n'
            '    "neutered": false,\n'
            '    "date_of_birth": "2019-01-01",\n'
            '    "microchip": null,\n'
            '    "weight": "3.2 kg"\n'
            "  },\n"
            '  "consultation": {\n'
            '    "date": "2025-02-21",\n'
            '    "time": "12:37",\n'
            '    "reason": "Repeat Consultation",\n'
            '    "type": "Outpatient",\n'
            '    "clinical_notes": [\n'
            "      {\n"
            '        "type": "general",\n'
            '        "note": "Doing a lot better, '
            "cough stopped\\nstarted running and "
            "playing\\neats food without "
            'issues\\nseems better and more lively overall"\n'
            "      }\n"
            "    ],\n"
            '    "treatment_items": {\n'
            '      "procedures": [\n'
            "        {\n"
            '          "date": "2025-02-21",\n'
            '          "time": "12:45",\n'
            '          "name": "Consultation - Repeat",\n'
            '          "code": "con010",\n'
            '          "quantity": 1,\n'
            '          "total_price": 6450,\n'
            '          "currency": "GBP"\n'
            "        }\n"
            "      ],\n"
            '      "medicines": [],\n'
            '      "prescriptions": [],\n'
            '      "foods": [],\n'
            '      "supplies": []\n'
            "    },\n"
            '    "diagnostics": []\n'
            "  }\n"
            "}\n"
        )

    def test_read_file_valid(self, file_reader, expected_file_content):
        file_path = os.path.join(os.path.dirname(__file__), "data", "consultation.json")

        actual_file_content = file_reader.read_file(file_path)

        assert actual_file_content == expected_file_content

    def test_read_file_not_found(self, file_reader):
        file_path = os.path.join(os.path.dirname(__file__), "data", "non_existent.json")

        with pytest.raises(FileNotFoundError, match=f"File '{file_path}' not found."):
            file_reader.read_file(file_path)
