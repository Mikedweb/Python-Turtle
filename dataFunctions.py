from patient import Patient
from datetime import datetime

# Initial list of patients
patients = [
    Patient("Nimish", "Narang", datetime(1990,1,6), 185, 90.3, True),
    Patient("Zenva", "Academy", datetime(2000,5,29), 200, 100.5, False),
    Patient("Foo", "Bar", datetime(1965,10,4), 174, 83.6, False)
]

# Returns a list with all patients' info
def convert_patients_to_table_data():
    patients_data = []
    for patient in patients:
        strings = patient.convert_values_to_strings()
        patients_data.append(strings)
    return patients_data

# Validates the input and attemts to create a patient, returns True if patient created successfully and False otherwise
def try_to_create_patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication):
    # Checks for empty strings or invalid first and last names
    if len(first_name) < 2 or len(last_name) < 2 or date_of_birth == "" or height == "" or weight == "":
        return False
    
    try:
        date_of_birth = datetime.strptime(date_of_birth, '%Y/%m/%d')
        # Checks if date is in the future
        if date_of_birth > datetime.now():
            return False
      
        height = int(height)
        weight = float(weight)
        # Checks if height or weight is less than or equal to zero
        if height <= 0 or weight <= 0:
            return False
  
        patient = Patient(first_name, last_name, date_of_birth, height, weight, is_taking_medication)
        patients.append(patient)
        return True
    except:
        return False