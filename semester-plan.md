# Critical Thinking in Research — Fall 2026 Lab Seminar

Weekly 1-hour sessions. Students: Carol, Marcio, Yishuang.
Committee presentations: week of Dec 1 (comp retake for Carol and Marcio,
committee meeting for Yishuang).

## Why this exists

The August 2026 comprehensive exams exposed a shared pattern: all three
students can operate tools and run models, but struggle to articulate the
scientific question the tool is meant to answer, explain what their models
actually compute, scope their work, describe a validation pathway, or
synthesize results into a finding. They work hard but not smart — they
default to "here's what I did" instead of "here's what I learned."

The core shift this seminar teaches: your job is not to show that you used
ABAQUS. Your job is to ask ABAQUS a question, design experiments to
probe/validate/ablate the answer, and synthesize what you found.

## Weekly format (1 hour)

| Block | Time | What happens |
|-------|------|--------------|
| Warm-up | 5 min | Each student states their current key finding in one sentence. Practiced every week from day 1 — synthesis is a muscle, not a skill you learn in November. |
| Concept | 15 min | Becca introduces the week's principle, ties it to a reading. |
| Workshop | 20 min | Students apply the concept to their own research, in writing. |
| Hot seat | 15 min | One student presents their workshop output; the other two + Becca critique. Rotates weekly (Carol → Marcio → Yishuang → repeat). |
| Takeaway | 5 min | What to prepare for next week. |

---

## Phase 1: The Question (Weeks 1–4)

### Week 1 — What does a good PhD look like? (Aug 26)

*Completed.*

What distinguishes a strong PhD graduate from someone who just finished?
Problem solvers, not stacks of papers. People who know how to ask questions,
not just do technical work. The PhD is training you to think independently —
to identify a problem, design a way to investigate it, and communicate what
you found. The degree is not the papers or the simulations; it is the
demonstrated ability to do that cycle on your own.

**Discussion:** What does "good enough" look like at the end? What are you
optimizing for — and what are you not?

---

### Week 2 — Why does anyone care? (Sep 2)

Tasks vs. questions, and the method for turning a topic into a question
worth asking. The Craft of Research three-step formula (3.4.1–3.4.3):
Topic → Question → Significance. Plus a first conversation about career
paths — who your "reader" is depends on where you end up.

**No pre-reading.** Heilmeier's Catechism handed out in session as a
reference sheet.

**Concept:** Becca teaches the three-step formula with a worked example
(Kallas & Napolitano blast paper). Instrumental vs. expressive behavior
(Unwritten Rules, Ch. 3).

**Workshop:** Write your three-step sentence. Maximum 3 research questions,
each with all three steps. No tool names. Step 3 must name a reader who
is not your advisor.

**Discussion:** Career paths (tenure-line, teaching prof, industry) — how
does your step 3 "reader" change depending on path?

**Reading (for next week):** Platt, "Strong Inference" (1964, Science,
~8 pages). The original argument for hypothesis-driven research.

---

### Week 3 — What are you NOT doing? (Sep 8)

Scope is not a limitation — it is a design decision. Claiming EF5 when your
results apply to EF2-3 is not ambitious, it is indefensible. Claiming you
validated the flat-to-3D translation when you demonstrated replication is not
generous, it is imprecise. Honest scope makes your actual contribution
stronger.

**Workshop:** Write your scope paragraph. What is in. What is out. Why the
boundary is where it is. What assumption or evidence sets each boundary.

**Reading (for next week):** Feynman, "Cargo Cult Science" (1974 Caltech
commencement, ~5 pages). On the difference between doing science and doing
something that looks like science.

**Hot seat:** Yishuang — present scope, group probes the boundaries.

---

### Week 4 — What does your tool compute? (Sep 15)

Your model is not your contribution. Your model is an instrument. You need to
know what it measures, how it measures it, and where it breaks — the way a lab
scientist knows their microscope's resolution limits.

If you built a dashboard that converts wind speed to structural load via
ASCE 7-22, you must be able to explain every step of that conversion without
opening the dashboard. If you run DIANA for nonlinear masonry analysis, you
must be able to explain what the constitutive model assumes, where it
simplifies reality, and what that simplification means for your results.

**Workshop:** For each model or tool you use, write: (1) what question it
answers, (2) what calculation it performs, (3) what it assumes, (4) where it
breaks.

**Reading (for next week):** Whitesides, "Writing a Paper" (Advanced
Materials, 2004, ~4 pages). On building a paper from an outline, not from
accumulated text.

**Hot seat:** Carol — explain what DIANA and Abaqus each do in your workflow
and why you need both. Not what the software can do — what it does for your
specific scientific question.

**Deliverable due: Research questions (revised) + scope paragraph.**
Becca gives written feedback before Week 5.

---

## Phase 2: The Investigation (Weeks 5–8)

### Week 5 — Designing computational experiments (Sep 22)

You do not "run the model." You design experiments. An experiment has a
hypothesis, controlled variables, a measurable outcome, and a criterion for
what counts as support or refutation.

A parameter sweep is not an experiment unless you can say what you expect to
see and what it would mean if you see something else. An ablation study is
not optional — it is how you prove each component of your method earns its
place.

**Workshop:** Design 3 computational experiments for your research. For each:
state the hypothesis, what you vary, what you hold constant, what you measure,
and what result would change your conclusion.

**Hot seat:** Marcio — present experiments, group asks: "What would you learn
from this that you don't already know?"

---

### Week 6 — What counts as evidence? (Sep 29)

The difference between "my model ran" and "my results support the hypothesis."
A converged simulation is not a finding. A pretty contour plot is not
evidence. Evidence is a result that distinguishes between your hypothesis and
an alternative.

**Workshop:** Take one result you already have. Write: (1) what the result is,
(2) what it supports, (3) what alternative explanation it does NOT rule out,
(4) what additional experiment would rule that alternative out.

**Reading (for next week):** One chapter from the data visualization book
(Becca assigns).

**Hot seat:** Yishuang — present a result from the fragility analysis, group
tries to find alternative explanations.

---

### Week 7 — Validation is not confidence (Oct 6)

"I am very confident this will work" is not a validation plan. Validation
requires you to state in advance: what you compare against, what metric you
use, what threshold counts as agreement, and what you do if it fails.

Verification (does the code solve the equations correctly?) is different from
validation (do the equations represent the real phenomenon?). You need both.
Cross-code comparison is verification. Comparison to experimental data is
validation. Citing someone else's validation of a different model is neither.

**Workshop:** Write your validation plan. For each claim in your research:
what is the evidence, and what would make you abandon the claim?

**Hot seat:** Carol — present the flat-wall-to-3D validation pathway. Not
"the seismic literature does this" — what will YOUR validation look like?

**Deliverable due: Experimental design + validation plan.**
Becca gives written feedback before Week 8.

---

### Week 8 — Midpoint presentation (Oct 13)

Each student gives a 10-minute presentation to the group:
Research question → method → preliminary results → what is next.

This is the first full dry run of the December narrative. Use the structure
from Week 11's concept (previewed here): 1-2 slides of motivation, then
hit the question, then results, then next steps.

**Critique focus:** Is the question clear? Does the method follow from the
question (not from the tool)? Did you get to results? Can you explain
everything on every slide in your own words?

**Each student gets ~10 min presentation + ~7 min of feedback.**

---

## Phase 3: The Story (Weeks 9–12)

### Week 9 — What did you find? (Oct 20)

A result is not "the model ran." A result is "the model shows that X because
Y, and this matters because Z." If you cannot state your finding in one
sentence without naming a software package, you have not yet found anything.

**Workshop:** Write your results section as a series of one-sentence findings.
No method, no motivation — just: what did you learn? Then rank them: which
one is the headline?

**Hot seat:** Marcio — present findings, group asks "so what?" after each one.

---

### Week 10 — Making your results visible (Oct 27)

A good figure makes the finding obvious. A bad figure makes the reader do
the work. Every figure must have a point — if you cannot write a one-sentence
caption that states what the reader should see, the figure is not ready.

**Workshop:** Take your most important result. Make a figure (sketch or
draft) that makes the finding immediately clear to someone who has not read
your paper. Write the one-sentence caption.

**Reading (for next week):** Selection from the scientific graphics book
(Becca assigns).

**Hot seat:** Yishuang — show a figure, group gives feedback: can you see the
finding without reading the text?

---

### Week 11 — Narrative arc and presentation structure (Nov 3)

The committee does not need your life story. They need: (1) what problem you
are solving, (2) how you are solving it, (3) what you found so far, (4) what
is next and how you know it will work.

If you spend half your talk on motivation and never get to results, the
committee concludes you do not have results. The fix is not "talk faster" —
it is "cut the motivation to 1-2 slides and lead with what you've done."

**Workshop:** Build your December presentation outline. Slide-by-slide plan
with one sentence per slide. Total presentation should be 20-25 minutes.
Time-check: if more than 3 slides are before your first result, cut.

**Deliverable due: Presentation outline.**
Becca gives written feedback.

**Hot seat:** Carol — walk through the outline, group checks pacing.

---

### Week 12 — Draft presentation + practice questions (Nov 10)

Full draft presentations (15-20 min each if time allows, otherwise rotate
so each student presents a portion and the others present the following week).

Becca and students play committee. Ask the hard questions:
- "What calculation does that tool actually perform?"
- "Why this method and not an alternative?"
- "What would make you wrong?"
- "Who uses this and under what circumstances?"

**Focus:** Can you answer "why" questions, not just "what" questions?

---

### Week 13 — Final practice + committee-style questioning (Nov 17)

Refined presentations. Becca plays each committee member's role — asks the
kinds of questions Paul, Nate, Orsolya, and Maggie would ask based on
their disciplinary perspectives.

- Paul-style: "What does your loading actually represent physically?"
- Nate-style: "What is your computational strategy and is it feasible?"
- Orsolya-style: "Who uses this and what decisions does it support?"
- Maggie-style: "What data do you wish you had, and what do you do without it?"

**Deliverable due: Final presentation draft.**

---

*Thanksgiving week (Nov 24) — no session. Final revisions.*

---

### Week 14 — Committee presentations (Dec 1)

Carol and Marcio: comprehensive exam retake.
Yishuang: committee meeting.

---

## Suggested readings

Short, high-impact pieces. Assign one per week during Phases 1-2, then
shift to presentation work in Phase 3.

| Week | Reading | Why |
|------|---------|-----|
| 2 (in-session) | Heilmeier's Catechism (DARPA, 1 page) | Reference handout — the right questions to ask |
| 2→3 | Platt, "Strong Inference" (Science 1964, ~8 pp) | The original case for hypothesis-driven research |
| 3 | Feynman, "Cargo Cult Science" (1974, ~5 pp) | Intellectual honesty: the difference between doing science and imitating it |
| 4 | Whitesides, "Writing a Paper" (Adv. Materials 2004, ~4 pp) | Building from an outline, not from accumulated text |
| 5–6 | Selected chapter from research design book (Becca assigns) | Experimental design principles |
| 7 | Selected chapter from "How to Write an Impactful Research Paper" | Connecting validation to the written argument |
| 10 | Selected sections from the scientific graphics book | Making results visible |

Other resources Becca may want to pull from:
- Booth, Colomb, Williams — "The Craft of Research" (especially Ch. 3-5 on questions and arguments)
- Heard — "The Scientist's Guide to Writing"
- Tufte — "The Visual Display of Quantitative Information" (for figures)
- Olson — "Houston, We Have a Narrative" (for research storytelling)

---

## Deliverable checkpoints

| Date | What is due | Feedback from |
|------|-------------|---------------|
| Sep 15 (Week 4) | Research questions (revised) + scope paragraph | Becca, written |
| Oct 6 (Week 7) | Experimental design + validation plan | Becca, written |
| Nov 3 (Week 11) | Presentation outline (slide-by-slide) | Becca + group |
| Nov 17 (Week 13) | Final presentation draft | Becca (committee-style) |
| Dec 1 (Week 14) | Committee presentation | Full committee |

---

## What this course is NOT

This is not a writing course, a software tutorial, or a presentation
coaching session. Those are downstream. This is about learning to think
like a scientist: to ask questions instead of performing tasks, to design
experiments instead of running models, to synthesize findings instead of
reporting activities, and to know — in your own words — what every piece
of your work does and why it matters.
