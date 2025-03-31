import pytest
from unittest.mock import patch, MagicMock
from vetnote.llm_client import LLMClient, OpenAIClient


def test_predict_abstract_method():
    with pytest.raises(TypeError):
        LLMClient()


@pytest.fixture
@patch("vetnote.llm_client.OpenAI")
def openai_client(MockOpenAI):
    mock_openai_instance = MockOpenAI.return_value
    client = OpenAIClient(model="gpt-4o-mini")
    return client, mock_openai_instance


def test_predict(openai_client):
    client, mock_openai_instance = openai_client
    mock_response = MagicMock()
    mock_response.output_text = '{"discharge_note": "Test note"}'
    mock_openai_instance.responses.create.return_value = mock_response
    input_text = "Test input"
    instructions = "Test instructions"

    result = client.predict(input_text, instructions)

    mock_openai_instance.responses.create.assert_called_once_with(
        model="gpt-4o-mini", instructions=instructions, input=input_text
    )
    assert result == '{"discharge_note": "Test note"}'
