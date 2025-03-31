import json
import os
from typing import Dict


def write_discharge_note_to_file(discharge_note: Dict[str, str], file_path: str):
    """
    Writes the discharge note to a file in the solution folder.

    Args:
        discharge_note (Dict[str, str]): The discharge note to be written to the file.
        file_path (str): The path to the output file.

    Raises:
        Exception: If an error occurs while writing the discharge note to the file.
    """
    output_dir = os.path.dirname(file_path)
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(file_path, "w") as output_file:
            json.dump(discharge_note, output_file, indent=4)
        print(f"Discharge note saved to {file_path}")
    except Exception as e:
        print(f"An exception occurred while saving the discharge note: {e}")
        raise
