from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Patient:
    """
    Represents the patient in the consultation data.
    """
    name: str
    gender: str
    species: Optional[str] = None
    breed: Optional[str] = None
    neutered: Optional[bool] = None
    date_of_birth: Optional[str] = None
    microchip: Optional[str] = None
    weight: Optional[str] = None

    def __post_init__(self):
        if not self.name:
            raise ValueError("The 'name' field is required for Patient.")
        if not self.gender:
            raise ValueError("The 'gender' field is required for Patient.")


@dataclass
class TreatmentItems:
    """
    Represents treatment items in the consultation data.
    """
    procedures: Optional[List[str]] = None
    medicines: Optional[List[str]] = None
    prescriptions: Optional[List[str]] = None
    foods: Optional[List[str]] = None
    supplies: Optional[List[str]] = None


@dataclass
class Consultation:
    """
    Represents a consultation in the consultation data.
    """
    date: str
    time: str
    reason: str
    type: str
    clinical_notes: List[str] = field(default_factory=list)
    treatment_items: TreatmentItems = field(default_factory=TreatmentItems)
    diagnostics: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.date:
            raise ValueError("The 'date' field is required for Consultation.")
        if not self.time:
            raise ValueError("The 'time' field is required for Consultation.")
        if not self.reason:
            raise ValueError("The 'reason' field is required for Consultation.")
        if not self.type:
            raise ValueError("The 'type' field is required for Consultation.")


@dataclass
class ConsultationData:
    """
    Represents the full consultation data, including patient and consultation details.
    """
    patient: Patient
    consultation: Consultation

    def __post_init__(self):
        if not self.patient:
            raise ValueError("The 'patient' field is required for ConsultationData.")
        if not self.consultation:
            raise ValueError("The 'consultation' field is required for ConsultationData.")