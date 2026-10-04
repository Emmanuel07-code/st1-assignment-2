# Stage 1 – Comparison and Notes

## Part A – Understanding the problem

**What data must be stored?**
Patient name, doctor name, and appointment date and time.

**What functions might be useful?**
Booking an appointment, showing all appointments, cancelling one, searching for a patient, and checking if a time slot is already taken.

**What could go wrong?**
Someone could type nothing or garbage as a name, two patients could get booked with the same doctor at the same time, typos could create fake duplicate patients, and everything gets lost when you close the program.

**What requirements are unclear?**
How do you type the time in? How long is each appointment? What if two patients have the same name? Does the data need to be saved between runs? Can you reschedule? Who else uses the system besides the receptionist?

## Part B – Limitations of the human-written prototype

I ran both programs and they worked. Then I tried some weird inputs to see what would break.

1. The appointments are typed straight into the code so you can't actually enter new ones.
2. You can book the same doctor at the same time twice and it doesn't complain.
3. If you type only spaces as a patient name it accepts it.
4. There's no check on the doctor name or the time at all. You can even put None and it works.
5. You can type "banana" as a time and it just saves it.
6. When you close the program everything is gone.
7. There's no way to cancel, change or search for anything.
8. There's no patient ID, and you can even put a number like 12345 as a name.

## Part D – AI-generated alternative (Copilot)

Prompt: "Create a simple beginner-friendly Python function that stores a patient name, practitioner name and appointment time for a small clinic. Do not use a database or a GUI. Keep it short and use only basic Python (functions, lists and dictionaries)."

Copilot's raw output (unedited):

```python
appointments = []

def book_appointment(patient, practitioner, time):
    appointment = {
        "patient": patient,
        "practitioner": practitioner,
        "time": time
    }
    appointments.append(appointment)
    return appointment
```

## Part E – Compare human and AI versions

| Question | Human version | AI version |
| --- | --- | --- |
| Easy to understand? | Yeah, it has comments and a display function so you can see what's happening. | It's really short which is nice but there's no comments and no way to see the output. |
| Runs successfully? | Yes, it printed all six lines I expected. | It runs but it doesn't actually show anything because nobody calls the function. |
| Uses only required features? | It does what was asked plus adds a display function and a blank-name check. | It does exactly what the prompt said and nothing more. |
| Adds assumptions? | It assumes names are just text and that you do everything in one go. | It assumes someone else will check the inputs. It also returns the appointment which I didn't ask for. The parameter is called `time` which is the same as a Python module name. |
| Handles errors? | It catches a blank or None patient name but nothing else. | No checks at all. Blank names, None, anything goes. |
| Could I explain it? | Yes because I wrote it. | Yes it's simple but I'd have to figure out what the return value is for. |


## Part F – Verify behaviour


I tested both versions by adding some test calls at the bottom of the file and running it.

**Normal booking:** Both versions accepted it fine.

**Blank patient name (""):** My version gave a ValueError and stopped it. Copilot's version just saved it with no name, which is wrong.

**Same doctor at the same time:** Both versions let it through. Neither one checks for double bookings.

**None as patient name:** My version caught it and gave a ValueError. Copilot's version saved it, which is wrong.

**None as appointment time:** Both versions accepted it, which is wrong. There should be a check for that.

Overall my version caught two of the four bad inputs and Copilot's caught none. Neither version stops double bookings or checks the time.