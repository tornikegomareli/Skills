---
id: therac-25-cryptic-malfunction
product: Therac-25
type: failure
category: hardware
year: 1986
principles: [poor-feedback-and-errors, usability-heuristic-violations]
---

**Decision.** The Therac-25 was a software-controlled radiation therapy machine. When it detected a low-priority problem, it showed "treatment pause" and the operator could press the P key to proceed, up to five times. Error messages were cryptic. The machine displayed "Malfunction" plus a number. The operator's manual did not explain the codes, and the maintenance manual listed them without meaning or any hint of risk to patients.

**Outcome.** Between June 1985 and January 1987, six known accidents gave patients massive overdoses. In March 1986 in Tyler, Texas, the screen showed "Malfunction 54" and a treatment pause. A sheet on the machine called it a "dose input 2" error. Later testimony said it meant the dose was too high or too low. The display showed an underdose, the machines often paused for harmless reasons, and the operator pressed P as usual. The patient had already been hit and was trying to get help. He died of the overdose five months later. The corrective plan included replacing cryptic malfunction messages with meaningful ones.

**Lesson.** If an error can mean danger, the message must say what happened and what to do, and routine harmless pauses must not train users to dismiss it.

## Sources
- https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/therac25.pdf (Nancy Leveson and Clark Turner, "An Investigation of the Therac-25 Accidents", IEEE Computer, 1993)
- https://en.wikipedia.org/wiki/Therac-25
