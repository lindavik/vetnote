import pytest
from vetnote.models import Patient, TreatmentItems, Consultation, ConsultationData


def test_patient_valid():
    patient = Patient(name="Sparky", gender="male", species="Dog")
    
    assert patient.name == "Sparky"
    assert patient.gender == "male"
    assert patient.species == "Dog"


def test_patient_missing_required_fields():
    with pytest.raises(ValueError, match="The 'name' field is required for Patient."):
        Patient(name=None, gender="male")

    with pytest.raises(ValueError, match="The 'gender' field is required for Patient."):
        Patient(name="Sparky", gender=None)


def test_treatment_items_optional_fields():
    treatment_items = TreatmentItems(
        procedures=["Vaccination"],
        medicines=["Antibiotics"]
    )

    assert treatment_items.procedures == ["Vaccination"]
    assert treatment_items.medicines == ["Antibiotics"]
    assert treatment_items.prescriptions is None
    assert treatment_items.foods is None
    assert treatment_items.supplies is None


def test_consultation_valid():
    consultation = Consultation(
        date="2025-03-19",
        time="09:15",
        reason="Checkup",
        type="Outpatient",
        clinical_notes=["Healthy"],
        treatment_items=TreatmentItems(procedures=["Vaccination"]),
        diagnostics=["Blood Test"]
    )

    assert consultation.date == "2025-03-19"
    assert consultation.time == "09:15"
    assert consultation.reason == "Checkup"
    assert consultation.type == "Outpatient"
    assert consultation.clinical_notes == ["Healthy"]
    assert consultation.treatment_items.procedures == ["Vaccination"]
    assert consultation.diagnostics == ["Blood Test"]


def test_consultation_missing_required_fields():

    with pytest.raises(ValueError, match="The 'date' field is required for Consultation."):
        Consultation(date=None, time="09:15", reason="Checkup", type="Outpatient")

    with pytest.raises(ValueError, match="The 'time' field is required for Consultation."):
        Consultation(date="2025-03-19", time=None, reason="Checkup", type="Outpatient")

    with pytest.raises(ValueError, match="The 'reason' field is required for Consultation."):
        Consultation(date="2025-03-19", time="09:15", reason=None, type="Outpatient")

    with pytest.raises(ValueError, match="The 'type' field is required for Consultation."):
        Consultation(date="2025-03-19", time="09:15", reason="Checkup", type=None)


def test_consultation_data_valid():
    patient = Patient(name="Sparky", gender="male")
    consultation = Consultation(
        date="2025-03-19",
        time="09:15",
        reason="Checkup",
        type="Outpatient"
    )

    consultation_data = ConsultationData(patient=patient, consultation=consultation)
    
    assert consultation_data.patient.name == "Sparky"
    assert consultation_data.consultation.reason == "Checkup"


def test_consultation_data_missing_required_fields():
    with pytest.raises(ValueError, match="The 'patient' field is required for ConsultationData."):
        ConsultationData(patient=None, consultation=Consultation(
            date="2025-03-19", time="09:15", reason="Checkup", type="Outpatient"))

    with pytest.raises(ValueError, match="The 'consultation' field is required for ConsultationData."):
        ConsultationData(patient=Patient(name="Sparky", gender="male"), consultation=None)
