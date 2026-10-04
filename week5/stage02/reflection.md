# Stage 2 Reflection

Before using AI I wrote out the requirements based on what the case study said. I came up with 10 things the system should do, 5 quality requirements, and 6 user stories. I also worked out who the stakeholders are and what's in scope versus what isn't.

When I sent the requirements to Copilot for review it found some gaps I'd missed. Like FR-01 doesn't say what "name" means (first name? full name?) or how the ID gets created. FR-03 doesn't say if searching by name is exact match or partial. And it pointed out that FR-06 talks about checking for conflicts but there's no appointment duration defined anywhere, so how do you actually check?

Copilot didn't make up new features which is good because that's what I told it not to do. But it did raise a question about FR-08 versus FR-09 and FR-10: the requirements say to keep cancelled appointments but don't say whether they should show up on the doctor's daily schedule or not. That's something we'd need to ask the client.

After the review I added some of these gaps to the assumptions section. The search behaviour and time format ones I'm leaving as open questions for when we actually start coding.

Requirements need evidence because if you just go with whatever sounds good you might waste time building something nobody actually asked for.