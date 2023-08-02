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