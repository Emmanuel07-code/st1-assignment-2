# Stage 4 Reflection

The AI suggested using an enum for the appointment status and a custom error for bad transitions, which I kept because they both make sense. The enum means status can only be Scheduled or Cancelled, not some random string, and the custom error makes it really obvious what went wrong when you try to cancel something twice.

The thing I changed from the AI was removing the type hints. They make the code look more professional but we haven't really covered them properly in class and they made the code harder to read for me. The logic is exactly the same without them.

I rejected the AI's suggestion to add a reschedule() method because rescheduling is still an open question from Stage 2. Nobody confirmed that the system needs it yet, so I didn't want to add something that might not be needed.

The double-booking check was my own addition. It goes through the existing appointments and checks if the same doctor already has something scheduled at that time. I tested it and it correctly rejected the duplicate. The cancel method also works right because it checks the current status first, so you can't cancel something that's already been cancelled.

The hardest part was getting the properties right. Using underscores to make things private and then adding @property so you can still read them from outside but not change them was new to me.