# Stage 2 Reflection

Before using AI, I wrote 10 functional requirements, 5 non-functional requirements, 6 user stories and acceptance criteria based on the SmartCare case study. I identified stakeholders, defined scope and labelled uncertain features as provisional.

Copilot's review caught several gaps I had missed. It pointed out that FR-01 and FR-04 do not define what "name" means or how the ID is generated. It flagged that FR-03's search behaviour (exact, partial or case-insensitive) is undefined, and that FR-06 implies conflict checking but no appointment duration exists to check against. It also noted that NFR-02 says "responsive" without giving a measurable target, which makes it untestable.

Copilot did not invent new features, which matched the prompt. However, its cross-requirement observation about FR-08 versus FR-09 and FR-10 was an assumption requiring validation: the brief says to retain cancelled appointments but does not say whether to display them on schedules.

After the review, I modified FR-01 and FR-04 by adding assumptions about ID generation, and I accepted the search-behaviour and time-format gaps as open questions for a later stage.

Requirements need evidence because AI generates plausible suggestions from patterns, not from this client's actual needs. Without evidence, a requirement could waste development time on something nobody asked for.