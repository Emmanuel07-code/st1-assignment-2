# Stage 3 Reflection

The hardest part was deciding whether to have one big coordinator class or split it into three separate managers. Copilot suggested having Patient, Practitioner and Appointment as the main classes, which is what I had too, so that was reassuring. It also suggested one ClinicSystem class to manage everything, and I went with that because three managers felt like way too much for a small system.

Where Copilot went overboard was suggesting a NotificationManager and a ScheduleEngine. Nobody in the case study asked for notifications, and we already rejected SMS reminders back in Stage 2. And a ScheduleEngine for what is basically one method seemed pointless.

For the relationships I went with one-to-many for both Patient-to-Appointment and Practitioner-to-Appointment, because one patient or doctor can have heaps of appointments but each appointment only has one of each. I made sure Appointment doesn't inherit from Patient because they're completely different things, Appointment just has a reference to a Patient.

The thing I still need to figure out is the actual code for double-booking checks and search. Right now the methods just say "pass" because the handout said to leave the real logic for Stage 4.