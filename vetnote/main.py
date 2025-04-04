import os
import sys

from vetnote.llm_client import OpenAIClient
from vetnote.note_generator import NoteGenerator
from vetnote.reader import FileReader
from vetnote.writer import write_discharge_note_to_file

OUTPUT_DIR = "solution"


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file_path>")
        print("Please provide a file path")
        sys.exit(1)

    file_path = sys.argv[1]
    file_content = ""

    try:
        file_content = FileReader.read_file(file_path)
    except FileNotFoundError as e:
        print(f"An exception occurred while reading the input files: {e}")
        sys.exit(1)

    llm_client = OpenAIClient()
    note_generator = NoteGenerator(
        llm_client=llm_client, instruction_file_path="vetnote/prompts/prompt.txt"
    )

    try:
        discharge_notes = note_generator.generate_discharge_notes(input_text=file_content)
        print("Discharge note below")
        print(f"{discharge_notes}")
    except Exception as e:
        print(f"An exception occurred while generating discharge notes: {e}")
        sys.exit(1)

    try:
        file_name = os.path.basename(file_path)
        output_file_path = os.path.join(OUTPUT_DIR, file_name)
        write_discharge_note_to_file(discharge_notes, output_file_path)
    except Exception as e:
        print(f"An exception occurred while writing discharge notes to solution folder: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
