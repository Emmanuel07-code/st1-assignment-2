# Stage 1 Reflection

Before using any AI I ran both versions of the SmartCare code from the handout. The basic one just prints two hard-coded appointments and the enhanced one uses a list and two functions. They both ran fine. I went through the code and wrote down what I thought was wrong with it, like you can't actually type anything in, the same doctor can be booked twice at the same time, and spaces-only names get accepted.

Copilot was helpful for explaining the function step by step. It pointed out that using a global list could cause problems, which I hadn't thought of. But it missed some things I had already found, like the spaces-only name issue and the fact that there's no cancel or search. The function Copilot wrote was really basic too, it didn't check anything at all.

I tested both versions with the same inputs. Normal bookings worked fine on both. Blank names got caught by mine but not Copilot's. Neither one stopped double bookings.

At the end I picked one thing to fix: making the code reject names that are just spaces. It was a one-line change and I tested it to make sure it worked without breaking anything else. I still need to figure out how to stop double bookings and how to properly check that the time is a real date.