# SmartCare v0.4 - Domain Layer Implementation
# Stage 4 Lab Activity
# This builds on the Stage 3 skeletons and adds real logic.

from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class InvalidTransitionError(Exception):
    # Custom error for when you try to do something like cancel an already-cancelled appointment
    pass


class Patient:
    def __init__(self, patient_id, name):
        if not patient_id or not str(patient_id).strip():
            raise ValueError("Patient ID cannot be empty.")
        if not name or not str(name).strip():
            raise ValueError("Patient name cannot be empty.")
        self._patient_id = patient_id.strip()
        self._name = name.strip()

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Patient({self._patient_id}, {self._name})"


class Practitioner:
    def __init__(self, practitioner_id, name):
        if not practitioner_id or not str(practitioner_id).strip():
            raise ValueError("Practitioner ID cannot be empty.")
        if not name or not str(name).strip():
            raise ValueError("Practitioner name cannot be empty.")
        self._practitioner_id = practitioner_id.strip()
        self._name = name.strip()

    @property
    def practitioner_id(self):
        return self._practitioner_id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Practitioner({self._practitioner_id}, {self._name})"


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time):
        if not appointment_id or not str(appointment_id).strip():
            raise ValueError("Appointment ID cannot be empty.")
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient.")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner.")
        if not date_time or not str(date_time).strip():
            raise ValueError("Appointment date/time cannot be empty.")

        self._appointment_id = appointment_id.strip()
        self._patient = patient
        self._practitioner = practitioner
        self._date_time = date_time.strip()
        self._status = AppointmentStatus.SCHEDULED

    @property
    def appointment_id(self):
        return self._appointment_id

    @property
    def patient(self):
        return self._patient

    @property
    def practitioner(self):
        return self._practitioner

    @property
    def date_time(self):
        return self._date_time

    @property
    def status(self):
        return self._status

    def cancel(self):
        # Only lets you cancel if it's currently Scheduled
        if self._status != AppointmentStatus.SCHEDULED:
            raise InvalidTransitionError(
                f"Can't cancel: appointment is already {self._status.value}.")
        self._status = AppointmentStatus.CANCELLED

    def __str__(self):
        return (f"Appointment({self._appointment_id}, {self._patient.name}, "
                f"{self._practitioner.name}, {self._date_time}, {self._status.value})")


class ClinicSystem:
    def __init__(self):
        self._patients = []
        self._practitioners = []
        self._appointments = []

    def add_patient(self, patient):
        self._patients.append(patient)

    def search_patient_by_id(self, patient_id):
        for p in self._patients:
            if p.patient_id == patient_id:
                return p
        return None

    def search_patient_by_name(self, name):
        # Returns all patients whose name contains the search text (case insensitive)
        return [p for p in self._patients if name.lower() in p.name.lower()]

    def add_practitioner(self, practitioner):
        self._practitioners.append(practitioner)

    def book_appointment(self, appointment):
        # Check if this doctor already has something at this time
        for existing in self._appointments:
            if (existing.practitioner.practitioner_id == appointment.practitioner.practitioner_id
                    and existing.date_time == appointment.date_time
                    and existing.status == AppointmentStatus.SCHEDULED):
                raise ValueError(
                    f"Double booking: {appointment.practitioner.name} already has "
                    f"an appointment at {appointment.date_time}.")
        self._appointments.append(appointment)

    def cancel_appointment(self, appointment_id):
        for appt in self._appointments:
            if appt.appointment_id == appointment_id:
                appt.cancel()
                return
        raise ValueError(f"Appointment {appointment_id} not found.")

    def get_practitioner_schedule(self, practitioner_id, date):
        # Only shows scheduled (not cancelled) appointments for that day
        return [a for a in self._appointments
                if a.practitioner.practitioner_id == practitioner_id
                and a.date_time.startswith(date)
                and a.status == AppointmentStatus.SCHEDULED]

    def get_patient_appointments(self, patient_id):
        # Shows everything including cancelled
        return [a for a in self._appointments
                if a.patient.patient_id == patient_id]


# Quick checks to make sure everything works
p1 = Patient("P001", "Alice Smith")
p2 = Patient("P002", "Bob Johnson")
dr1 = Practitioner("D001", "Dr. John Doe")
dr2 = Practitioner("D002", "Dr. Jane Roe")
print(f"Created: {p1}, {p2}, {dr1}, {dr2}")

# Test bad inputs
for label, pid, pname in [("empty ID", "", "Test"), ("empty name", "P999", ""), ("spaces name", "P999", "   ")]:
    try:
        Patient(pid, pname)
        print(f"  {label}: ACCEPTED (shouldn't have been)")
    except ValueError as e:
        print(f"  {label}: rejected - {e}")

# Set up the system
system = ClinicSystem()
system.add_patient(p1)
system.add_patient(p2)
system.add_practitioner(dr1)
system.add_practitioner(dr2)

# Book a normal appointment
a1 = Appointment("A001", p1, dr1, "2026-10-05 10:00 AM")
system.book_appointment(a1)
print(f"\nBooked: {a1}")

# Try double booking
a2_dup = Appointment("A002", p2, dr1, "2026-10-05 10:00 AM")
try:
    system.book_appointment(a2_dup)
    print("  Double booking: ACCEPTED (shouldn't have been)")
except ValueError as e:
    print(f"  Double booking rejected: {e}")

# Book a different time (should work)
a3 = Appointment("A003", p2, dr1, "2026-10-05 11:00 AM")
system.book_appointment(a3)
print(f"Booked: {a3}")

# Cancel
system.cancel_appointment("A001")
print(f"\nAfter cancel: {a1}")

# Try cancelling again
try:
    system.cancel_appointment("A001")
    print("  Double cancel: ACCEPTED (shouldn't have been)")
except InvalidTransitionError as e:
    print(f"  Double cancel rejected: {e}")

# Search
print(f"\nSearch by ID 'P001': {system.search_patient_by_id('P001')}")
print(f"Search by name 'bob': {[str(p) for p in system.search_patient_by_name('bob')]}")

# Schedule
sched = system.get_practitioner_schedule("D001", "2026-10-05")
print(f"\nDr. Doe schedule for 2026-10-05: {[str(a) for a in sched]}")

# All appointments for Alice (includes cancelled)
all_appts = system.get_patient_appointments("P001")
print(f"Alice's appointments: {[str(a) for a in all_appts]}")

print("\nAll checks passed")