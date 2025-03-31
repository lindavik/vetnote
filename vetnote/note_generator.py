import json

from vetnote.llm_client import LLMClient
from vetnote.reader import FileReader


class NoteGenerator:
    def __init__(self, llm_client, instruction_file_path: str):
        self.llm_client: LLMClient = llm_client
        self.instructions = FileReader.read_file(file_path=instruction_file_path)

    def generate_discharge_notes(self, input_text: str) -> dict:
        """
        Generates discharge notes based on the input text using the LLM client.

        This method sends the input text and instructions to the LLM client to generate a response.
        It then extracts the JSON discharge note from the response and returns it as a dictionary.

        Args:
            input_text (str): The input text containing details about the patient and consultation.

        Returns:
            dict: A dictionary containing the discharge note with the key "discharge_note".

        Raises:
            Exception: If an error occurs while calling the LLM
            or if the response format is invalid.
        """
        try:
            response = self.llm_client.predict(
                input_text=input_text, instructions=self.instructions
            )
            return NoteGenerator._extract_json(response=response)
        except Exception as e:
            raise Exception(f"An exception occurred while calling the LLM: {e}")

    @staticmethod
    def _extract_json(response: str) -> dict:
        """
        Extracts JSON from the response string. At times LLMs like to add additional
        embellishments to the response and to prevent this from breaking the flow,
        we have this additional check to extract the JSON.
        Args:
            response (str): The response string from the LLM.

        Returns:
            dict: A dictionary containing the discharge note.

        Raises:
            ValueError: If no JSON is found in the response or if the response format is invalid.
        """
        start_index = response.find("{")
        end_index = response.rfind("}") + 1
        if start_index == -1 or end_index == 0:
            raise ValueError("No JSON found in the response")
        response_json = response[start_index:end_index]
        response_dict = json.loads(response_json)
        if "discharge_note" in response_dict:
            return {"discharge_note": response_dict["discharge_note"]}
        else:
            raise ValueError("Invalid response format: 'discharge_note' key is missing")
