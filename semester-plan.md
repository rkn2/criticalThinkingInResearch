# H3D Research Methods Class — Fall 2026

Weekly 1-hour sessions, Thursdays. Students: Carol, Marcio, Yishuang, Young, Borna.
Committee presentations: Dec 8 (comp retake for Carol and Marcio,
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
| Hot seat | 10 min | Each student presents their workshop output (~2-4 min each); the others + Becca critique. |
| Takeaway | 5 min | What to prepare for next week. |

---

## Phase 1: The Question (Weeks 1–4)

### Week 1 — What does a good PhD look like? (Sep 1)

*Completed.* Slides: `docs/week01-slides.html`.

What distinguishes a strong PhD graduate from someone who just finished?
Problem solvers, not stacks of papers. People who know how to ask questions,
not just do technical work. The PhD is training you to think independently —
to identify a problem, design a way to investigate it, and communicate what
you found. The degree is not the papers or the simulations; it is the
demonstrated ability to do that cycle on your own.

**Discussion:** What does "good enough" look like at the end? What are you
optimizing for — and what are you not?

**Career paths:** tenure-line, teaching prof, industry. What each job is,
what you're evaluated on, what to build during the PhD, and the tradeoffs
(Feibelman Ch. 6). Which path interests you, and what should you do during
the PhD to keep options open?

---

### Week 2 — Why does anyone care? (Sep 2)

Tasks vs. questions, and the method for turning a topic into a question
worth asking. The Craft of Research three-step formula (3.4.1–3.4.3):
Topic → Question → Significance.

**No pre-reading.** Heilmeier's Catechism handed out in session as a
reference sheet.

**Concept:** Becca teaches the three-step formula with a worked example
(Kallas & Napolitano blast paper). Instrumental vs. expressive behavior
(Unwritten Rules, Ch. 3).

**Workshop:** Write your three-step sentence. Maximum 3 research questions,
each with all three steps. No tool names. Step 3 must name a reader who
is not your advisor.

**Reading (for next week):** Chamberlin, "The Method of Multiple Working Hypotheses" (1890, Science,
~6 pages). The case for entertaining competing explanations instead of
falling in love with one.

---

### Week 3 — What don't you know? (Sep 17)

*Completed.* See `sessions/week03-sep17.md`.

Step 2 of the three-step sentence is the research question. Three tests:
it names what you don't know, it has more than one possible answer, and
evidence could change the answer. Common problems: too broad, foregone
conclusion, tool-centric, restating Step 1.

**Workshop:** Sharpen Step 2 into a standalone research question.

Research questions took the whole session; hypotheses, Chamberlin, and
scope moved to Week 4. Many questions came out as hypotheses with a
question mark on the end.

---

### Week 4 — From question to hypothesis (Sep 24)

*Completed.* Slides: `docs/week04-slides.html`.

Read back last week's research questions. Tell a question from a
hypothesis-with-a-question-mark (yes/no? already expect yes? names the
answer?) and work backward: keep the hypothesis, write the question it
answers, list three possible answers. Then hypotheses: a proposed answer,
specific and testable; what would make you wrong; Chamberlin on multiple
working hypotheses, then xkcd 1838 (Machine Learning) on confirmation
bias: the intellectual child with a computer attached. Scope moved to
Week 5 (decided Sep 24); the deck ends on the research question +
hypothesis pair.

**Workshops:** (1) Question or hypothesis? Label last week's sentence, write
the question it answers, list three possible answers. (2) Propose an answer:
one hypothesis, what would make you wrong, a competing hypothesis, and an
experiment that distinguishes them.

**Deliverable due next session: Research question (revised) + hypothesis
pair.** Becca gives written feedback.

---

## Phase 2: The Investigation (Weeks 5–7)

### Week 5 — Scope: what are you not claiming? (Oct 1)

Slides: `docs/week05-slides.html`.

Scope: the four-part scope paragraph (in, out, why the boundary
is there, what evidence or assumption sets it). Claiming EF5 when your
results apply to EF2-3 is not ambitious, it is indefensible. Claiming you
validated the flat-to-3D translation when you demonstrated replication is
not generous, it is imprecise.

**Note from Week 4 (Sep 24):** scope both the research question and the
hypothesis. They are different processes. Question scope comes from the gap
and who cares about the answer; hypothesis scope comes from where your
evidence can tell your answer apart from the competing one.

Then stress-test it through committee questions. The boundary is where
you show what you know: a question past your line usually checks whether
you understand the other side, not whether you'll do it. Talk about it in
the conditional (predict, mechanism, literature, cost) without signing up
("I could add that"). Answer: reason past the line, anchor the line, name
the cost. A real request for more work: engage, then follow up with your
advisor; don't agree in the room. If a push shows a boundary has no
reason, the boundary moves.

**Workshops:** (1) Scope paragraph, once for the question and once for the
hypothesis (paragraph or table). (2) Map your boundary: research
question as a bubble, each hypothesis as its own circle inside it,
brainstorm committee questions and place each where it lands (inside the
bubble but outside every hypothesis = question covers it, evidence
doesn't; outside = not this work). Answer the hardest:
reason, anchor, cost.

"What does your tool compute?" (model as instrument) was dropped (decided
Oct 1).

**Deliverable due: Research question (revised) + hypothesis pair.** Scope
paragraph (question + hypothesis) due Week 6.

---

### Week 6 — Telling a research story (Oct 8)

Slides: `docs/week06-slides.html`. Adapted from Ardon Shorr, "Telling
Research Stories" (Princeton, Spring 2020; source in OneDrive
`archivedDocs/Princeton/Courses/2020Spring/Slides & Handouts/3 Stories`).
Start of presentation work, aimed at the Oct 15 5-minute pitches.

Invert the pyramid: lead with the result, not the background. Say what each
detail means. The story template (Goal, Obstacle, Approach, Result, Benefit),
chained as "we want X, but Y" (Radiolab's Haber story, then the URM
tornado retrofit question and hypotheses A/B/C from Week 5). The storymap's U-shape, and the broken path that stays on
"here's what I did." Name the obstacle precisely (Swan, "Motives in
Research"). Ties back: Goal = Step 3, first Obstacle = research question,
Approach = competing hypotheses + how you tell them apart, Result and
Benefit stay inside the scope (check against the scope paragraph and
boundary map). Click-to-reveal builds as in Week 5.

**Example talk (added Oct 7):** after the half-life workshop, a 5-minute
annotated example talk (six slides plus a debrief). Each slide is 80% talk,
20% meta panel: a mini U-shape storymap showing where the slide sits, plus
notes tying it to this week's concepts. The left arm of the U is drawn as a
staircase (goal, but, narrower goal, but, ... research question) to show the
"we want X, but Y" chain digging in. Setting is Saanchi's Mayfield
historic-masonry work, fictionalized: the numbers are illustrative and the
slides say so.

**Workshops:** (1) Build your storymap, all five elements. (2) Half-life
your message: 60, 30, 15, 8 seconds with a partner (Aurbach et al. 2018).

**Deliverable due: Scope paragraph (question + hypothesis).** Turn the
storymap into a 5-minute pitch for next session (Oct 15).

**Bumped (decided Oct 1), placement TBD:** Designing computational
experiments. You do not "run the model." You design experiments. An
experiment has a hypothesis, controlled variables, a measurable outcome, and
a criterion for what counts as support or refutation. A parameter sweep is
not an experiment unless you can say what you expect to see and what it
would mean if you see something else. An ablation study is not optional. It
is how you prove each component of your method earns its place.
**Workshop:** Design one computational experiment: the hypothesis, what you
vary, what you hold constant, what you measure, and what result would change
your conclusion.

---

### Week 7 — 5-minute pitches (Oct 15)

Decided Oct 8. Everyone gives a 5-minute pitch built from their Week 6
storymap (the U-shape), then gets feedback. About 5 min + 6 min feedback
each; if it runs long, the last one or two go first on Oct 22. No result
yet: state the expected result and mark it as expected.

**Feedback, in storymap terms:** Is the goal clear, and who cares? Do the
"but"s dig down to a research question? Competing hypotheses, and a way to
tell them apart? A result, or the broken "here's what I did" path? Benefit
inside the scope? The 8-second version?

The old Week 7 topic ("What counts as evidence?") and the experimental
design deliverable are dropped as standalone items; evidence comes up in
the feedback on hypotheses.

---

## Phase 3: Talks and Questions (Weeks 8–14)

### Weeks 8–13 — Practice talks and questions (Oct 22 – Dec 3)

Left open on purpose (decided Oct 8): the rest of the semester is giving
talks and asking / answering questions, with the format set week to week
based on what the Oct 15 pitches show. No session Thanksgiving week
(Thu Nov 26).

Ideas from the original plan to pull from as needed: one-sentence findings
(rank the headline), figures with a one-sentence caption, a slide-by-slide
outline of the December talk, full draft talks with the group playing
committee, and committee-style questions in the voice of each member
(Paul: what does the loading represent physically; Nate: is the
computational strategy feasible; Orsolya: who uses this and what decisions
does it support; Maggie: what data do you wish you had).

---

### Week 14 — Committee presentations (Dec 8)

Carol and Marcio: comprehensive exam retake.
Yishuang: committee meeting.

---

## Suggested readings

Short, high-impact pieces. Assign one per week during Phases 1-2, then
shift to presentation work in Phase 3.

| Week | Reading | Why |
|------|---------|-----|
| 2 (in-session) | Heilmeier's Catechism (DARPA, 1 page) | Reference handout — the right questions to ask |
| 2→3 | Chamberlin, "The Method of Multiple Working Hypotheses" (Science 1890, ~6 pp) | The case for competing explanations over a single ruling theory |
| TBD | Feynman, "Cargo Cult Science" (1974, ~5 pp) | Intellectual honesty: the difference between doing science and imitating it |
| TBD | Whitesides, "Writing a Paper" (Adv. Materials 2004, ~4 pp) | Building from an outline, not from accumulated text |
| 5–6 | Selected chapter from research design book (Becca assigns) | Experimental design principles |
| TBD | Selected chapter from "How to Write an Impactful Research Paper" | Connecting evidence to the written argument |
| 7 | Popper, *The Myth of the Framework* (1994), Ch. 8 "Models, Instruments, and Truth" | A model is an instrument for testing a theory, not the theory or the world; a converged run is not evidence |
| 12–13 | Popper, *The Myth of the Framework*, Ch. 2 (title essay) | Rational discussion across frameworks is possible and most fruitful when the frameworks differ; prep for questions from committee members in other disciplines |
| 10 | Selected sections from the scientific graphics book | Making results visible |

Other resources Becca may want to pull from:
- Booth, Colomb, Williams — "The Craft of Research" (especially Ch. 3-5 on questions and arguments)
- Heard — "The Scientist's Guide to Writing"
- Tufte — "The Visual Display of Quantitative Information" (for figures)
- Olson — "Houston, We Have a Narrative" (for research storytelling)
- Popper — "The Myth of the Framework: In Defence of Science and Rationality"
  (ed. Notturno, Routledge 1994). Chapters and where they fit:
  - Ch. 1 "The Rationality of Scientific Revolutions" (conjecture and
    error elimination; bold, refutable hypotheses): would have paired with
    Week 4 alongside Chamberlin. Use as a callback in Week 7.
  - Ch. 2 "The Myth of the Framework": Weeks 12–13, committee questioning
    across disciplines (Paul, Nate, Orsolya, Maggie).
  - Ch. 4 "Science: Problems, Aims, Responsibilities" (science starts from
    problems, not observations or tools): would have fit Weeks 2–3.
  - Ch. 8 "Models, Instruments, and Truth": Week 7 (evidence), or the
    bumped computational-experiments session; also the dropped "what does
    your tool compute?" topic.

---

## Deliverable checkpoints

| Date | What is due | Feedback from |
|------|-------------|---------------|
| Oct 1 (Week 5) | Research question (revised) + hypothesis pair | Becca, written |
| Oct 8 (Week 6) | Scope paragraph (question + hypothesis) | Becca, written |
| Oct 15 (Week 7) | 5-minute pitch | Group + Becca, live |
| Oct 22 – Dec 3 | Practice talks, set week to week | Group + Becca, live |
| Dec 8 (Week 14) | Committee presentation | Full committee |

---

## What this course is NOT

This is not a writing course, a software tutorial, or a presentation
coaching session. Those are downstream. This is about learning to think
like a scientist: to ask questions instead of performing tasks, to design
experiments instead of running models, to synthesize findings instead of
reporting activities, and to know — in your own words — what every piece
of your work does and why it matters.
