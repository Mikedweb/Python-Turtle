# all prompts
welcome_prompt = "Welcome doctor, what would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

name_prompt = "What is the patient's name?\n"

appearance_prompt = "What is the patient's general appearance?\n - Normal appearance, press 1\n - Is he irritable or lethargic, press 2\n"

eye_prompt = "How do the eyes appear?\n - Eyes normal or slightly sunken, press 1\n - Eyes are very sunken, press 2\n"

skin_prompt = "How is the patient's skin when you pinch it?\n - Normal skin pinch, press 1\n - Slow to return shape skin pinch, press 2\n"

#Error message
error_message = "Could not save patient and diagnosis due to invalid input"

# Diagnoses
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

# Storage temp
patients_and_diagnoses = [
  "Mike: Severe dehydration",
  "Sally: No dehydration",
  "Kate: Some dehydration"
]

#List patients
def list_patients():
  for patient in patients_and_diagnoses:
    print(patient)

#Save new diagnoses
def save_new_diagnosis(name, diagnosis):
  if name == "" or diagnosis == "":
    print(error_message)
    return
  final_diagnosis = name + ": " + diagnosis
  patients_and_diagnoses.append(final_diagnosis)
  print("Final diagnosis:", final_diagnosis, "\n")

#def list_patients():
  #print("Listing patients and diagnoses")

#Start diagnosis
def start_new_diagnosis():
   print("Starting a new diagnosis")
   name = input(name_prompt)
   diagnosis = assess_appearance()
   save_new_diagnosis(name, diagnosis)

# Test skin
def assess_skin(skin):
  #skin = input(skin_prompt)
  if skin == "1":
      return some_dehydration
  elif skin == "2":
      return severe_dehydration
  else:
    return ""

#Test eyes
def assess_eyes(eyes):
  #eyes = input(eye_prompt)
  if eyes == "1":
      return no_dehydration
  elif eyes == "2":
      return severe_dehydration
  else:
    return ""
    
 # Main 
def main():
  while (True):
    selection = input(welcome_prompt)
    #print(selection)
    if selection == "1":
      list_patients()
    elif selection == "2":
      start_new_diagnosis()
    elif selection == "q":
      return

# Initial Assessment
def assess_appearance():
    appearance = input(appearance_prompt)
    # direct user based on input
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
      return ""
  

main()

# Assessing all if-then-else cases for both skin and eyes
def test_assess_skin():
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("3") == "")

def test_assess_eyes():
    print(assess_eyes("1") == no_dehydration)
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("3") == "")

def test_assess_appearance():
    print(assess_appearance())

# Assessing all possible cases of entries for name and diagnosis
def test_save_new_diagnosis():
    save_new_diagnosis("", "")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("", "No dehydration")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "Some dehydration")
    print(patients_and_diagnoses == [
        "Mike - Severe dehydration",
        "Sally - No dehydration",
        "Kate - Some dehydration",
        "Nimish - Some dehydration"
    ])


test_assess_skin()
test_assess_eyes()
#test_assess_appearance()
test_save_new_diagnosis()