import os
import pytest
from vetnote.reader import read_data_files
from vetnote.models import ConsultationData


@pytest.fixture
def valid_data_folder():
    return os.path.join(os.path.dirname(__file__), "data/valid")

def test_read_data_valid(valid_data_folder):
    result = read_data_files(valid_data_folder)

    assert len(result) == 1
    assert isinstance(result[0], ConsultationData)
    assert result[0].patient.name == "Darth Vader"
    assert result[0].consultation.reason == "Repeat Consultation"

@pytest.fixture
def invalid_punctuation_data_folder():
    return os.path.join(os.path.dirname(__file__), "data/invalid-punctuation")


def test_read_invalid_punctuation(invalid_punctuation_data_folder):
    
    result = read_data_files(invalid_punctuation_data_folder)

    assert len(result) == 1
    assert isinstance(result[0], ConsultationData)
    assert result[0].patient.name == "Sparky"
    assert result[0].consultation.reason == "Ophtho | Eyelid Mass Removal"

@pytest.fixture
def invalid_missing_data_folder():
    return os.path.join(os.path.dirname(__file__), "data/invalid-missing-data")


def test_read_invalid_missing_data(invalid_missing_data_folder):
    
    result = read_data_files(invalid_missing_data_folder)

    assert len(result) == 1
    assert isinstance(result[0], ConsultationData)
    assert result[0].patient.name == "Sparky"
    assert result[0].consultation.reason == "Ophtho | Eyelid Mass Removal"

@pytest.fixture
def invalid_corrupt():
    return os.path.join(os.path.dirname(__file__), "data/invalid-missing-data")
