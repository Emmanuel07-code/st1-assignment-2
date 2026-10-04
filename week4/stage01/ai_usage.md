# AI Usage Log – Stage 1

Tools used: Microsoft Copilot (Parts C and D).

## Before AI

**What I think the code does:**
book_appointment takes three inputs and saves them as a dictionary in a list. If the patient name is blank it gives an error. display_appointments prints out all the saved appointments or says there are none.

**Problems I noticed:**
The appointments are already typed into the code so you can't enter new ones. If you type only spaces as a name it still works, which seems wrong. There's no way to cancel or look up an appointment. The data disappears when you close the program.

## AI request (Copilot, Part C)

Prompt used:
"Act as a Python tutor. I am learning introductory software technology. Here is a small appointment-booking function: [book_appointment code]. 1. Explain what the code does. 2. Identify three limitations. 3. Suggest improvements. 4. Do not rewrite the whole application. 5. Ask me two questions to test my understanding."

## Evaluate Copilot's response

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
| --- | --- | --- | --- | --- |
| Explanation of what the code does | ✔ | | | |
| Limitation: no validation for practitioner or time | ✔ | | | |
| Limitation: no double-booking check | ✔ | | | |
| Limitation: global list, no persistence | ✔ | | | |
| Improvement: stricter input validation | ✔ | | | |
| Improvement: conflict check before booking | ✔ | | | |
| Improvement: encapsulate data in a class | | | | ✔ |
| Improvement: use datetime objects | | ✔ | | |

## Decide

Accept: stricter input validation. The spaces-only name was a problem I noticed myself, so fixing that makes sense.
Keep for later: double-booking check. It's a real problem from the case study but I only wanted to change one thing at a time.
Reject for now: putting everything in a class. We haven't learned classes yet in this stage.
Keep unverified: using datetime. I don't know enough about it yet to use it properly.

## My answers to Copilot's questions

**1. Why might a global appointments list become a problem as the program grows?**
Because any part of the code can change it, so if something breaks you don't know what caused it. It also makes testing annoying because leftover data from one test messes up the next one. You can only ever have one list too, so you couldn't have separate ones for different doctors or clinics.

**2. What validation would I add for appointment_time, and why does it matter?**
I'd check that it's not blank, that it follows one format like YYYY-MM-DD HH:MM, and that it's an actual date and not in the past. Right now you can type "banana" as a time and it just accepts it. Also if someone types "10:00 AM" and someone else types "10:00am" the program thinks they're different times, which would mess up any double-booking check.

## AI request (Copilot, Part D)

Prompt used:
"Create a simple beginner-friendly Python function that stores a patient name, practitioner name and appointment time for a small clinic. Do not use a database or a GUI. Keep it short and use only basic Python (functions, lists and dictionaries)."

Copilot's output is recorded unedited in comparison.md (Part D).

## Verify

I ran both programs and they worked without errors. I tested a normal booking and it went through fine. I also tried a blank name, which my version caught but Copilot's didn't. I tried booking the same doctor at the same time twice and both versions let it through, which is a problem. After my fix, a name with only spaces was also caught.

## Explain

I can explain my final code without looking at Copilot's answer. book_appointment checks that the patient name is not blank or just spaces, then saves the three values in a dictionary and adds it to the list. display_appointments goes through the list and prints each one, or says there are none. I still need to learn how to stop double bookings and how to check that the time is a real date and time.

