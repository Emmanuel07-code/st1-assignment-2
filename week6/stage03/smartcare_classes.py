# SmartCare v0.3 - Class Skeletons
# Stage 3 Lab Activity
# These are just the basic structure. The actual logic gets added in Stage 4.


class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def __str__(self):
        return f"Patient({self.patient_id}, {self.name})"


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name

    def __str__(self):
        return f"Practitioner({self.practitioner_id}, {self.name})"


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time, status="Active"):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def cancel(self):
        # Changes status to Cancelled but keeps the appointment in the list
        self.status = "Cancelled"

    def __str__(self):
        return (f"Appointment({self.appointment_id}, {self.patient.name}, "
                f"{self.practitioner.name}, {self.date_time}, {self.status})")


class ClinicSystem:
    def __init__(self):
        self.patients = []
        self.practitioners = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def search_patient_by_id(self, patient_id):
        pass  # Stage 4

    def search_patient_by_name(self, name):
        pass  # Stage 4

    def add_practitioner(self, practitioner):
        self.practitioners.append(practitioner)

    def book_appointment(self, appointment):
        pass  # Stage 4

    def cancel_appointment(self, appointment_id):
        pass  # Stage 4

    def get_practitioner_schedule(self, practitioner_id, date):
        pass  # Stage 4

    def get_patient_appointments(self, patient_id):
        pass  # Stage 4


# Quick check that everything works
p = Patient("P001", "Alice Smith")
dr = Practitioner("D001", "Dr. John Doe")
appt = Appointment("A001", p, dr, "2026-10-05 10:00 AM")

print(p)
print(dr)
print(appt)

appt.cancel()
print(f"After cancel: {appt}")

system = ClinicSystem()
system.add_patient(p)
system.add_practitioner(dr)
print(f"Patients: {len(system.patients)}")
print(f"Practitioners: {len(system.practitioners)}")
print("All good - classes match the domain model")
