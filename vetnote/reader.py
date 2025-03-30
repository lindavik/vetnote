from json import JSONDecodeError
import os
import json5
from typing import List
from vetnote.models import Patient, Consultation, ConsultationData, TreatmentItems


def read_data_files(data_folder: str) -> List[ConsultationData]:
    """
    Reads all files in the specified data folder and translates them into ConsultationData models.

    Args:
        data_folder (str): Path to the folder containing JSON files.

    Returns:
        list[ConsultationData]: A list of ConsultationData objects.
    """
    data = []

    for filename in os.listdir(data_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(data_folder, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    raw_data = json5.load(file)

                    # Translate raw JSON data into models
                    patient = Patient(**raw_data["patient"])
                    treatment_items = TreatmentItems(**raw_data["consultation"]["treatment_items"])
                    consultation = Consultation(
                        date=raw_data["consultation"]["date"],
                        time=raw_data["consultation"]["time"],
                        reason=raw_data["consultation"]["reason"],
                        type=raw_data["consultation"]["type"],
                        clinical_notes=raw_data["consultation"].get("clinical_notes", []),
                        treatment_items=treatment_items,
                        diagnostics=raw_data["consultation"].get("diagnostics", []),
                    )
                    consultation_data = ConsultationData(patient=patient, consultation=consultation)
                    data.append(consultation_data)
            except JSONDecodeError as e:
                print(f"Error decoding JSON in file {filename}: {e}")
            except KeyError as e:
                print(f"Missing key in file {filename}: {e}")
            except Exception as e:
                print(f"Error reading file {filename}: {e}")

    return data
