# Stage 4 Reflection

The AI-generated Appointment class included a reschedule() method, which I rejected because rescheduling is listed as an open question in Stage 2, not a confirmed requirement. The approved design constrained the AI: by giving it only the confirmed UML and explicit business rules, it could not invent features that were not in scope.

I accepted the AppointmentStatus enum and the InvalidTransitionError exception, both of which the AI suggested. The enum makes status values explicit and prevents arbitrary strings, and the custom exception distinguishes transition errors from general input errors. Neither was in the Stage 3 UML, but both are justified by the implementation: they enforce FR-07 (cancel) and FR-08 (retain) more strictly than a plain string status would.

The part I modified was the status protection. The AI initially used a public attribute, which any code could change directly. I replaced it with a protected attribute and a property, so status can only be read from outside and changed through cancel(). This matches the encapsulation principle discussed in the tutorial.

The double-booking check (FR-06) was my own addition to ClinicSystem.book_appointment(). It scans the existing list for a scheduled appointment with the same practitioner and time before accepting a new booking. I verified it with a test case that correctly rejected the duplicate.