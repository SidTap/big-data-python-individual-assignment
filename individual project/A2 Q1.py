import random
import datetime

class Patient:
    def __init__(self, id):
        self.id = id
        self.last_test_date = None

    def set_last_test_date(self, date):
        self.last_test_date = date

class PatientPool:
    def __init__(self):
        self.patients = []
        self.patient_ids = set()

    def add_patient(self, patient):
        if patient.id not in self.patient_ids:
            self.patients.append(patient)
            self.patient_ids.add(patient.id)

    def select_random_patients(self, batch_size):
        selected_patients = []
        now = datetime.datetime.now()
        date = now.date()

        for patient in random.sample(self.patients, batch_size):
            patient.set_last_test_date(date)
            selected_patients.append(patient.id)

        return selected_patients

def main():
    patient_pool = PatientPool()
    for i in range(1, 21):
        patient_pool.add_patient(Patient(f"p{i}"))

    batch_size = 5
    selected_patients = patient_pool.select_random_patients(batch_size)
    for patient in patient_pool.patients:
        if patient.id in selected_patients:
            print(f"Patient {patient.id} was tested on {patient.last_test_date}")
        else:
            print(f"Patient {patient.id} was not selected for testing")

if __name__ == '__main__':
    main()


# Time complexity:O(n)
# Space complexity:O(1)