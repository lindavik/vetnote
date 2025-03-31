import json

from vetnote.llm_client import LLMClient
from vetnote.reader import FileReader


class NoteGenerator:
    def __init__(
            self,
            llm_client,
            instruction_file_path: str
    ):
        self.llm_client: LLMClient = llm_client
        self.instructions = FileReader.read_file(
            file_path=instruction_file_path
        )

    def generate_discharge_notes(self, input_text: str) -> dict:
        try:
            response = self.llm_client.predict(
                input_text=input_text, instructions=self.instructions
            )
        except Exception as e:
            print(f"An exception occurred while calling the LLM: {e}")
            raise Exception("An exception occurred while calling the LLM")

        raw_response: str = response["choices"][0]["message"]["content"]
        print(f"Raw response: {raw_response}")
        discharge_note = json.loads(raw_response)
        print(f"Discharge note: {discharge_note}")
        return discharge_note
