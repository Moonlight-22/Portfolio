"""SerenityPath report body using Wunna Kyaw 7-chapter structure."""
from __future__ import annotations

from pathlib import Path

from serenitypath_ch17_extra import extra_ch1, extra_ch2, extra_ch3, extra_ch4, extra_ch5, extra_ch6

FIGS = Path(r"C:\EDU\Job_Edu\job_doc\lib\portfolio\report_work\serenitypath_figs")


def write_wunna_report(b, figs: Path | None = None):
    figs = figs or FIGS

    b.page_break()
    b.h("Table of Contents (structure)")
    toc = [
        "Abstract and keywords",
        "Chapter 1: Introduction — 1.1 Motivation — 1.2 LLMs and telepsychiatry — 1.3 Technologies overview — 1.4 Academic question, aim, objectives — 1.5 Scope and limitations — 1.6 Report framework — 1.7 Summary",
        "Chapter 2: Literature Review — 2.1 Introduction — 2.2 Related literature on LLMs and digital mental health — 2.3 Concepts of dual pathways, stigma and crisis governance — 2.4 Gaps in existing tools — 2.5 Research gap — 2.6 Design features taken from the readings — 2.7 Summary",
        "Chapter 3: System Design and Development — 3.1 Requirements — 3.2 Use cases and actors — 3.3 Architecture (method, diagrams, class, flow, activity, behaviour) — 3.4 Data model — 3.5 Interface design — 3.6 Summary",
        "Chapter 4: Implementation and Testing — 4.1 Tools and environment — 4.2 Build process — 4.3 Module implementation — 4.4 Testing strategy — 4.5 Summary",
        "Chapter 5: Testing and Evaluation — 5.1 Functional outcomes — 5.2 Evaluation methods — 5.3 Prototype limits — 5.4 Discussion against the academic question — 5.5 Summary",
        "Chapter 6: Conclusion — 6.1 Achievements against objectives — 6.2 Answer to the academic question — 6.3 Limitations — 6.4 Future work",
        "Chapter 7: Critical Evaluation and Professionalism — 7.1 Process reflection — 7.2 Ethics and risk communication — 7.3 Legal and academic integrity — 7.4 Summary",
        "References",
        "Appendix A: Glossary of Terms",
        "Appendix B: Reproducibility Notes",
        "Appendix C: Extra Assessor Notes",
    ]
    for item in toc:
        b.p(item, justify=False, space_after=4, track=False)

    b.page_break()
    b.h("Abstract")
    b.p(
        "This report introduces SerenityPath, a patient-directed mental health web platform "
        "developed for 6CS007 Project and Professionalism. Access to affordable, private "
        "psychological support remains uneven because of stigma, cost, waiting times, and the "
        "shortage of psychiatrists. Existing digital products tend to sit at two extremes: "
        "wellness chatbots that cannot escalate to a clinician, and telepsychiatry services that "
        "require a booked professional from the outset. SerenityPath offers both pathways in one "
        "product: an AI emotional-support companion powered by Google Gemini with a Groq fallback, "
        "and appointment booking with verified doctors that stores video-room metadata for "
        "telepsychiatry sessions."
    )
    b.p(
        "The academic question is whether offering a patient-directed choice between an "
        "API-driven large language model chatbot and live telepsychiatry improves accessibility, "
        "user satisfaction, and treatment engagement in a web-based platform. The artefact is a "
        "three-tier system. The presentation layer is Next.js 16 (App Router, React 19, TypeScript) "
        "in English and Myanmar. The application layer is a Laravel 13 REST API organised as "
        "controllers, services, and repositories, with bearer-token authentication and roles for "
        "patient, doctor, and admin. Incoming AI messages are scanned for crisis phrases; matches "
        "create a crisis_alerts row and return a safety reply with referral guidance instead of a "
        "normal model completion."
    )
    b.p(
        "Functional testing of authentication, booking, AI sessions, crisis triage, doctor "
        "verification, and the educational library confirmed that the dual-pathway design is "
        "technically workable. A small usability survey indicated that the choice between AI "
        "support and a human clinician was easy to understand and that the companion was viewed "
        "as a low-stigma first contact. The platform is a prototype, not a live clinical service. "
        "Within those bounds, the evidence supports a patient-directed hybrid architecture that "
        "lowers the barrier to seeking help while keeping a route to a licensed professional."
    )
    b.p(
        "Keywords: patient-directed care, LLM companion, Google Gemini, Groq, telepsychiatry, "
        "crisis triage, Laravel, Next.js, RBAC, Project and Professionalism.",
        italic=True,
        justify=False,
        track=False,
    )

    # ----- Chapter 1 -----
    b.page_break()
    b.h("Chapter 1: Introduction")
    b.h("1.1 Project Motivation", 2)
    b.p(
        "Mental health need has grown faster than the supply of clinicians who can meet it. "
        "People living with stress, anxiety, or depression often face overlapping barriers: "
        "the cost of private consultations, long public waiting lists, limited psychiatrist "
        "availability outside major cities, and the stigma of being seen to ask for help "
        "(Torous et al., 2021; Hilty et al., 2013). When distress is acute, there is frequently "
        "no immediate, private channel that is cheaper than a full clinical appointment and "
        "safer than an unmoderated chatbot."
    )
    b.p(
        "Digital health products have started to occupy this space, but many still force a "
        "binary choice. Consumer chat applications can be available around the clock, yet they "
        "rarely include governed escalation when a user expresses self-harm. Telepsychiatry "
        "platforms can connect a patient to a licensed professional over video, yet they assume "
        "the user is already ready to book, pay, and wait for a slot (Shore et al., 2018). "
        "The gap between those two models is the practical problem this project addresses."
    )
    b.p(
        "The project is submitted for 6CS007, so the problem is not only technical. An artefact "
        "that touches psychological distress has to bound harm, protect data, and avoid claiming "
        "clinical authority that the software does not have. That constraint shaped later "
        "decisions: the companion is labelled as non-diagnostic; crisis phrases are not left to "
        "model improvisation; doctors are hidden until an administrator verifies them; and model "
        "API keys never leave the Laravel environment file. If a dual pathway increased access "
        "only by exposing users to ungoverned generated text, the project would have failed the "
        "module even if the interface looked complete."
    )
    b.p(
        "A local reading of the same problem is also necessary. Where specialist psychiatry is "
        "concentrated in a few cities, a person in distress may face travel, cost, language "
        "mismatch, and social stigma at the same time. English-only products quietly exclude "
        "users who read Myanmar more comfortably. SerenityPath therefore treats i18next locale "
        "files as part of accessibility. After signing in, a patient can open an AI companion "
        "or browse verified doctors. Administrators review crisis alerts, verify doctors, manage "
        "the educational library, and inspect usage reports. The implementation follows the "
        "project README: Next.js 16 on port 3006 and a Laravel 13 API on port 8000."
    )

    b.h("1.2 Introduction to LLMs, Telepsychiatry and Patient-Directed Care", 2)
    b.p(
        "Large language models are transformer-based systems trained on very large text corpora. "
        "In mental health they are attractive because they can hold an open-ended conversation, "
        "rephrase distress in empathic language, and remain available outside clinic hours "
        "(Stade et al., 2024). They can also sound clinical without being clinically accountable. "
        "The literature therefore supports using an LLM as an emotional-support companion, not as "
        "an unsupervised diagnostic engine."
    )
    b.p(
        "Telepsychiatry — psychiatric assessment and treatment delivered over electronic "
        "networks — has a longer evidence base than LLM chat. Hilty et al. (2013) and Shore et al. "
        "(2018) summarise that video consultation can produce outcomes comparable to in-person "
        "care for many common presentations, while removing travel. Accessibility gains are not "
        "automatic: users still have to find a doctor, trust the platform, and obtain a slot."
    )
    b.p(
        "Patient-directed is used here in a precise sense. It does not mean that the software "
        "replaces clinical judgement. It means that, after authentication, the next action is "
        "chosen by the user rather than by a forced intake that ends only in a booking form. "
        "Traditional clinic software is provider-directed. Wellness chatbots are vendor-directed. "
        "SerenityPath sits between those models. The patient may stay with the companion, open "
        "resources, view crisis referrals, or book a verified doctor. The administrator remains "
        "in the loop when risk language appears."
    )
    b.p(
        "Live telepsychiatry in this iteration means a booked, role-authenticated session with "
        "a verified doctor that carries video-room metadata. The README does not implement a "
        "complete peer-to-peer media stack with TURN relays. Over-claiming WebRTC would inflate "
        "Chapter 4 and undermine Chapter 7."
    )

    b.h("1.3 Overview of Platform Technologies", 2)
    b.p(
        "Contemporary student health prototypes commonly combine a browser dashboard, a REST API, "
        "a relational database, and one or more external AI providers. SerenityPath follows that "
        "pattern with an explicit split between portal and admin. The frontend is Next.js 16 with "
        "the App Router, React 19, TypeScript, Tailwind CSS v4, TanStack Query, Axios, Zustand, "
        "react-hook-form, Zod, and i18next (en, my). The backend is Laravel 13 on PHP 8.3+, with "
        "controllers, services, repositories, form requests, and role middleware. Persistence is "
        "MySQL 8 or SQLite. Auth is a bearer token. AI is Google Gemini with Groq fallback, "
        "configured by AI_PROVIDERS. Optional notes cover CORS for ports 3000 and 3006, "
        "GEMINI_HTTP_PROXY, and SSL_CERT_FILE for Windows/XAMPP TLS failures."
    )
    b.p(
        "The two codebases are mental_health_web and mental_health_api. Public API routes include "
        "health, register, login, verified doctors, slots, resources, and referrals. Authenticated "
        "routes cover profile, appointments, AI sessions, and feedback. Admin routes cover crisis "
        "alerts, patients, doctors, verification, availability, lunch breaks, library, and reports. "
        "Demo accounts are seeded so that each role can be shown in a viva without hand-built data."
    )

    b.h("1.4 Academic Question, Aim and Objectives", 2)
    b.h("1.4.1 Academic Question", 3)
    b.p(
        "How does offering a patient-directed choice between an API-driven Large Language Model "
        "(LLM) chatbot and live telepsychiatry impact accessibility, user satisfaction, and "
        "treatment engagement in a web-based mental health platform?"
    )
    b.p(
        "Accessibility is the ability of a signed-in patient to obtain a first support contact "
        "without visiting a clinic and without waiting for a doctor to be online. Satisfaction "
        "is perceived ease, pathway clarity, helpfulness of the companion for low-intensity "
        "distress, and trust that unverified doctors and crisis events are handled. Engagement "
        "means continued use of the companion and/or progression to viewing therapists and "
        "placing an appointment. The report does not claim that engagement equals recovery."
    )
    b.h("1.4.2 Aim", 3)
    b.p(
        "To design, implement, test, and document a bilingual patient-directed web platform that "
        "gives users a real choice between governed AI emotional support and verified-doctor "
        "telepsychiatry booking, and to evaluate that choice against accessibility, satisfaction, "
        "and engagement."
    )
    b.h("1.4.3 Objectives", 3)
    b.bullets([
        "Develop a Next.js 16 App Router frontend with patient, doctor, and admin experiences and English/Myanmar localisation.",
        "Build a Laravel 13 REST API with bearer-token authentication, role middleware, and a controllers–services–repositories layout.",
        "Integrate Gemini and Groq through the API so that model keys never sit in the browser, and implement crisis-keyword detection that writes crisis_alerts for admins.",
        "Implement appointment booking against doctor availability slots, including lunch-break exclusion and video-room metadata.",
        "Provide an educational resource library, referral contacts, and an admin console for crisis, users, doctors, reports, and settings.",
        "Seed demo accounts, document the schema, and run functional tests plus a structured usability survey to answer the academic question.",
    ])
    b.h("1.4.4 Success Criteria Linked to Objectives", 3)
    b.table(
        ["Objective", "Success criterion"],
        [
            ["O1 Frontend + i18n", "Portal and admin routes run on :3006; en/my labels switch without a route change."],
            ["O2 Laravel API + RBAC", "Bearer auth works; non-admins cannot open /admin/* or admin APIs."],
            ["O3 Governed LLM", "Ordinary message returns a companion reply; crisis phrase writes an alert and a safety reply."],
            ["O4 Booking", "Verified doctor slots exclude lunch and existing bookings; appointment starts as pending."],
            ["O5 Admin + library", "Admin can verify doctors, triage alerts, and list resources/referrals."],
            ["O6 Evaluation", "Seeded demo, black-box table, and survey items in Appendix C."],
        ],
    )

    b.h("1.5 Scope and Limitations", 2)
    b.p(
        "The scope is a working academic prototype of a bilingual web platform with two care "
        "pathways, role-based access, crisis alerting, and appointment management. It is not a "
        "deployed clinical service, it is not integrated with national electronic health records "
        "or insurance systems, and it does not issue medical diagnoses or prescriptions."
    )
    b.bullets([
        "The AI companion is limited to emotional first aid. Copy states that it is not a doctor.",
        "Live model replies depend on Gemini and/or Groq keys. Without keys the API returns a safe local fallback.",
        "Telepsychiatry is booking plus video-room metadata, not a full WebRTC media stack.",
        "The user study is a small tester group, not a longitudinal clinical trial.",
        "GDPR-oriented controls are implemented at prototype standard; full healthcare certification is out of scope.",
    ])

    b.h("1.6 Report Framework", 2)
    b.p(
        "Chapter 2 reviews literature on LLMs, telepsychiatry, hybrid care, and the research gap. "
        "Chapter 3 presents requirements, use cases, architecture, class and behaviour diagrams, "
        "data model, and interface design. Chapter 4 records tools, the build process, module "
        "implementation, and the testing strategy. Chapter 5 reports functional outcomes, "
        "evaluation methods, prototype limits, and discussion against the academic question. "
        "Chapter 6 concludes. Chapter 7 is a critical evaluation of process, ethics, and academic "
        "integrity. References and appendices follow."
    )

    b.h("1.7 Summary", 2)
    b.p(
        "This chapter set out the motivation for a patient-directed hybrid platform, defined LLM "
        "and telepsychiatry terms in plain language, named the technology path, and stated the "
        "academic question, aim, objectives, success criteria, and limits. Chapter 2 turns to the "
        "readings that justify those choices."
    )
    extra_ch1(b)

    # ----- Chapter 2 -----
    b.page_break()
    b.h("Chapter 2: Literature Review")
    b.h("2.1 Introduction", 2)
    b.p(
        "Chapter 2 details reading for SerenityPath and how that reading informed design. It is "
        "not an encyclopaedia of every chatbot. The emphasis is on LLM applications in mental "
        "health, telepsychiatry evidence, hybrid care, ethical boundaries, and technical patterns "
        "for a role-split web artefact. Digital mental health has moved from static "
        "psychoeducation sites to conversational agents and remote clinics because demand exceeds "
        "the number of available clinicians (Torous et al., 2021; Abd-Alrazaq et al., 2020)."
    )

    b.h("2.2 Related Literature on LLMs and Digital Mental Health", 2)
    b.p(
        "Guo et al. (2024) review LLM applications ranging from knowledge tests and "
        "psychoeducation through to experimental screening. The consistent finding is capability "
        "paired with risk: models can sound clinical without being clinically accountable. Stade "
        "et al. (2024) argue that LLMs could change behavioural healthcare if development is "
        "responsible, evaluated, and bounded. They also warn that ungoverned deployment can "
        "produce harmful advice, over-confidence, and privacy leakage."
    )
    b.p(
        "That warning is why SerenityPath never calls Gemini or Groq from the browser. Prompts "
        "are sent through the Laravel service layer, and crisis phrases short-circuit a normal "
        "completion. Prompt instructions that say “be a supportive listener and do not diagnose” "
        "are necessary but not sufficient, because a model can still ignore them. Scanning inbound "
        "user text before a completion is requested is the second control. If a high-risk phrase "
        "is present, the system does not wait to see whether Gemini would have behaved well."
    )
    b.p(
        "This two-control design is consistent with professional guidance that automated tools in "
        "health-adjacent settings should fail toward human review (BCS, 2021) and with GDPR "
        "integrity and confidentiality principles (ICO, 2023). The chatbot literature often "
        "celebrates anonymity; the professionalism literature insists on accountability. "
        "SerenityPath tries to keep both: the patient can start privately, but a crisis is visible "
        "to the admin role."
    )

    b.h("2.3 Concepts of Dual Pathways, Stigma, Crisis Governance and Telepsychiatry", 2)
    b.p(
        "Systematic reviews of conversational agents report that anonymity, 24-hour availability, "
        "and the absence of a waiting room reduce the social cost of asking for help (Abd-Alrazaq "
        "et al., 2020; Guo et al., 2024). For users who fear judgement, a text interface can be a "
        "first rehearsal of what they later say to a clinician. The same reviews insist that LLMs "
        "must not prescribe or diagnose. Best practice is a visible non-diagnostic disclaimer, "
        "logging and governance, and an automatic route to human help when risk language appears."
    )
    b.p(
        "Telepsychiatry research is not only about video quality. Shore et al. (2018) emphasise "
        "identity of the clinician, privacy of the setting, and a predictable session lifecycle. "
        "A booking system that cannot prevent double-booking, that lists unverified accounts as "
        "doctors, or that has no language for cancelled and missed sessions is not a care pathway. "
        "SerenityPath uses pending, confirmed, in_progress, completed, cancelled, and no_show, and "
        "computes availability from weekly templates minus lunch breaks minus existing appointments."
    )
    b.p(
        "Stepped-care models typically move a person from low-intensity support toward specialist "
        "treatment as need increases. Digital products sometimes invert that logic by trapping the "
        "user in the cheapest step. Torous et al. (2021) warn that apps can expand reach while "
        "fragmenting accountability. A hybrid platform answers that warning only if the higher "
        "step is reachable from the same login. The dashboard therefore presents AI companion and "
        "therapists as sibling cards, backed by GET /api/doctors and POST /api/appointments."
    )
    b.p(
        "Technology-acceptance arguments used in digital health evaluation find that perceived "
        "ease of use, trust, and facilitating conditions predict whether a system is actually used "
        "(Lee et al., 2020). For SerenityPath those conditions include a working login, a language "
        "switch, seeded demo accounts, a verified-doctor flag, and a crisis banner. That is why "
        "Chapter 3 spends time on wireframes and why Chapter 5 asks about pathway clarity rather "
        "than only about feature completeness."
    )

    b.h("2.4 Gaps in Existing Tools and Design Implications", 2)
    b.p(
        "Commercial wellness chatbots are widely available, but they do not necessarily show a "
        "student-owned loop from login to governed completion to admin triage to a booked "
        "clinician. Hospital telepsychiatry suites exist, but they often assume the user is already "
        "ready to book. Student prototypes sometimes expose model keys in the browser, omit crisis "
        "routing, or treat “React chat UI” as sufficient architecture. The design implication is "
        "that SerenityPath must make pathway choice visible, keep keys on the server, persist "
        "crisis alerts, and hide unverified doctors."
    )

    b.h("2.5 Research Gap", 2)
    b.bullets([
        "Gap 1: many demos are chatbot-only or booking-only, not an explicit patient choice on one dashboard.",
        "Gap 2: LLM calls are often made from the client, which leaks keys and skips server-side crisis policy.",
        "Gap 3: evaluation sometimes reports a single satisfaction percentage without separating functional proof from usability.",
        "Gap 4: bilingual English/Myanmar support is rarely treated as an accessibility requirement in hybrid mental-health student systems.",
    ])
    b.p(
        "SerenityPath is designed to address those gaps with a dual-pathway portal, a Laravel "
        "proxy, crisis_alerts, verified booking, i18n, and a test table plus survey rather than "
        "a single undifferentiated score."
    )

    b.h("2.6 Design Features Taken from the Readings", 2)
    b.p(
        "From Stade et al. (2024) and Guo et al. (2024): bounded companion, no diagnosis, human "
        "review on risk. From Hilty et al. (2013) and Shore et al. (2018): identifiable clinician, "
        "session lifecycle, remote access. From Torous et al. (2021): hybrid reach without "
        "abandoning accountability. From BCS (2021) and ICO (2023): fail toward a human, minimise "
        "data, protect confidentiality. From ordinary web-engineering practice: separate client "
        "and API, role middleware, relational integrity. Those features appear in Chapter 3 as "
        "requirements and in Chapter 4 as modules."
    )

    b.h("2.7 Summary", 2)
    b.p(
        "The readings validate governed LLM companions, effective telepsychiatry, hybrid care, "
        "and explainable role-split interfaces. They do not validate an unsupervised diagnostic "
        "bot. Chapter 3 turns the gap analysis into requirements, use cases, and diagrams."
    )
    extra_ch2(b)

    # ----- Chapter 3 -----
    b.page_break()
    b.h("Chapter 3: System Design and Development")
    b.h("3.1 Requirements Overview", 2)
    b.p(
        "Functional requirements were extracted from the README and from the academic question. "
        "Patients must register and log in; start, continue, and end AI sessions; send messages; "
        "browse verified doctors; read available slots; book appointments; view resources and "
        "referrals; update a profile; and submit feedback. Doctors must log in, see sessions, "
        "update appointment status, and maintain weekly availability and lunch breaks. Admins "
        "must triage crisis alerts, verify doctors, manage users and library content, and read "
        "usage reports. Public callers must reach GET /api/health without a token."
    )
    b.p(
        "Non-functional requirements were treated as first-class. Confidentiality requires hashed "
        "passwords, bearer tokens, and role isolation. Integrity requires foreign keys so that a "
        "message cannot exist without a session. Availability of the AI path requires Groq fallback "
        "and a local safe reply when keys are missing. Localisation requires English and Myanmar. "
        "Auditability requires crisis_alerts and usage logs. Usability requires that both pathways "
        "are visible on the dashboard without a tutorial."
    )

    b.h("3.2 Use Cases and Actors", 2)
    b.p(
        "The main actors are Patient, Doctor, and Admin. The AI engine is an external participant "
        "(Gemini/Groq) invoked only by the API. A patient registers or logs in, browses therapists, "
        "books against slots, chats with the companion, reads resources, opens crisis referrals, "
        "and may submit feedback. A doctor views sessions, updates status, and sets availability. "
        "An admin triages alerts, verifies doctors, manages users and the library, and reads reports. "
        "Crisis scanning is an «extend» of sending an AI message, not a separate patient-initiated "
        "use case."
    )
    b.figure(figs / "fig_usecase.png",
             "Figure 3.1: Use case diagram for patient, doctor, and admin, including crisis-scan extension.")

    b.h("3.3 Architecture", 2)
    b.p(
        "The architecture is three-tier. Presentation is Next.js 16. Application is Laravel 13 "
        "(controllers, services, repositories, middleware). Data is MySQL 8 or SQLite. External "
        "systems are Gemini, Groq, and appointment video-room metadata. The browser is untrusted. "
        "The API is the system of record. Axios attaches the bearer token from Zustand; 401/419 "
        "clears the session."
    )
    b.figure(figs / "fig_architecture.png",
             "Figure 3.2: SerenityPath three-tier architecture.")

    b.h("3.3.1 Development method used in this project", 3)
    b.p(
        "Implementation used short iterative slices rather than a single waterfall build. Sprint "
        "one established auth, roles, and migrations. Sprint two added the Next.js shell, "
        "middleware, and i18n. Sprint three implemented AI sessions and crisis scanning. Sprint "
        "four implemented availability and booking. Sprint five completed the admin console, "
        "resources, and reports. Sprint six was hardening, seeding, tests, and this report. Agile "
        "was appropriate because companion safety could not be fully specified until sample crisis "
        "phrases were tried against real model replies."
    )

    b.h("3.3.2 Design diagrams from the project artefact", 3)
    b.p(
        "The remaining diagrams in this chapter are taken from the artefact rather than from a "
        "generic textbook hospital schema. They were checked against routes/api.php and the Next.js "
        "app directory so that the report cannot drift from the code a marker runs."
    )

    b.h("3.3.3 Class diagram", 3)
    b.p(
        "Figure 3.3 shows domain classes and the three services that enforce policy: AuthService, "
        "AppointmentService, and AiChatService. User and Doctor are related one-to-one. "
        "Appointments, sessions, messages, and crisis alerts carry the dual-pathway state. "
        "Phrase scanning lives on AiChatService, not on the React client."
    )
    b.figure(figs / "fig_class.png",
             "Figure 3.3: Class diagram of domain entities and application services.")

    b.h("3.3.4 Flow Diagram", 3)
    b.p(
        "Figure 3.4 is the operational flow from opening the site. Unauthenticated users go to "
        "/login. Role splits admin from the portal. A patient may enter AI chat (with a crisis "
        "branch), booking, resources, or profile. Booking writes pending. AI chat either stores a "
        "Gemini/Groq reply or writes crisis_alerts. Usage logging feeds admin reports."
    )
    b.figure(figs / "fig_flow.png",
             "Figure 3.4: Operational flow from login through AI, booking, resources, and admin triage.",
             max_height=8.2)

    b.h("3.3.5 Activity Diagram", 3)
    b.p(
        "Figure 3.5 is reserved for the interaction that can cause harm: an AI message. The "
        "patient types in the companion screen. The portal posts to /api/ai-chat/sessions/{id}/messages. "
        "Laravel validates the token and patient role, persists the user message, and scans phrases. "
        "On a match, it inserts an alert and returns a safety reply. On no match, Gemini is called, "
        "with Groq as fallback. Swimlanes make it obvious that the patient never calls the model."
    )
    b.figure(figs / "fig_activity.png",
             "Figure 3.5: Activity diagram for AI messaging with crisis triage.")

    b.h("3.3.6 Behaviour Diagrams", 3)
    b.p(
        "Figure 3.6 shows the booking sequence. The UI posts through Axios with a bearer token. "
        "The controller delegates to AppointmentService, which checks role and slot freedom, "
        "inserts pending plus video-room metadata, and returns 201. TanStack Query caches are "
        "invalidated so both patient and doctor lists refresh. A later PATCH /status moves the "
        "lifecycle forward."
    )
    b.figure(figs / "fig_sequence.png",
             "Figure 3.6: Sequence diagram for booking an appointment.")

    b.h("3.4 Data Model and Persistence", 2)
    b.p(
        "Figure 3.7 summarises the relational design documented in mental_health_api/docs/DATABASE_SCHEMA.md. "
        "users holds identity, role, and status. doctors extends a user with licence, specialisation, "
        "and verified. availability_slots and lunch_breaks are weekly templates. appointments link "
        "patient and doctor. ai_chat_sessions and messages store companion history. crisis_alerts "
        "capture severity, matched phrase, and admin notes. resources and referrals hold the library "
        "and hotlines, including locale. Two integrity rules dominate: public doctor lists are "
        "verified-only, and a crisis match must not become a normal assistant completion."
    )
    b.figure(figs / "fig_er.png",
             "Figure 3.7: Entity-relationship model for SerenityPath.")
    b.p(
        "GDPR data minimisation influenced what is stored. The prototype needs email, hashed "
        "password, role, and doctor licence fields. It does not need national IDs or insurance "
        "numbers. Chat bodies are stored so sessions can reload, which tensions with minimisation; "
        "the academic compromise is local seed data and no real patients. Soft-delete across all "
        "tables is listed as future work rather than as a completed feature."
    )

    b.h("3.5 Interface Design", 2)
    b.p(
        "Interface design aimed at low cognitive load: a patient should see two care options "
        "without hunting through menus. Figure 3.8 shows login with language switch; dashboard "
        "cards for companion, therapists, sessions, and resources; the companion with a safety "
        "banner; booking of verified doctors; and the admin crisis queue. Tailwind and a calm teal "
        "palette were chosen to avoid a clinical aesthetic that might increase anxiety, while still "
        "looking like a serious health product."
    )
    b.figure(figs / "fig_wireframes.png",
             "Figure 3.8: Wireframes for login, dashboard, AI companion, booking, and admin crisis queue.")
    b.p(
        "Two alternative flows were rejected. A wizard that always started in AI chat would have "
        "biased engagement toward the companion. A booking-only product with a decorative chatbot "
        "would have ignored the accessibility half of the academic question. The dashboard therefore "
        "branches, and admins are routed to /admin/dashboard so crisis work is not mixed with "
        "self-help chat."
    )

    b.h("3.6 Summary", 2)
    b.p(
        "Chapter 3 specified requirements, actors, three-tier architecture, class and behaviour "
        "views, the relational model, and the dual-pathway interface. Chapter 4 records how those "
        "designs were built and how they were planned to be tested."
    )
    extra_ch3(b)

    # ----- Chapter 4 -----
    b.page_break()
    b.h("Chapter 4: Implementation and Testing")
    b.h("4.1 Tools and Environment", 2)
    b.p(
        "Local requirements are PHP 8.3+ with Composer, Node.js 20+, and MySQL 8 or SQLite. The "
        "API is started with php artisan serve after migrate:fresh --seed. The web app uses npm "
        "run dev and NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000/api. Figure 4.1 shows the "
        "repository layout. Frontend modules live under api/, hooks/, schema/, store/, i18n/, and "
        "middleware.ts. Backend code lives under Http/Controllers/Api, Services, Repositories, "
        "and docs/DATABASE_SCHEMA.md. README author attribution is eriklogs1123."
    )
    b.figure(figs / "fig_structure.png",
             "Figure 4.1: Repository layout of mental_health_web and mental_health_api.")
    b.table(
        ["Layer", "Technology", "Role in the build"],
        [
            ["Frontend", "Next.js 16, React 19, TypeScript", "App Router groups for portal vs admin."],
            ["UI", "Tailwind CSS v4, Framer Motion", "Dashboards and motion without a third design system."],
            ["Client data", "TanStack Query, Axios, Zustand, Zod", "Server state, token attachment, validated forms."],
            ["i18n", "i18next (en, my)", "English and Myanmar copy."],
            ["Backend", "Laravel 13, PHP 8.3+", "Auth, validation, services, repositories."],
            ["Database", "MySQL 8 or SQLite", "Relational integrity; SQLite for local demo."],
            ["AI", "Gemini + Groq fallback", "Companion completions behind the API."],
        ],
    )

    b.h("4.2 Build and Learning Process", 2)
    b.p(
        "Learning during the build concentrated on three areas that were not obvious from a "
        "generic CRUD tutorial: putting LLM keys behind a service, computing bookable slots from "
        "templates minus lunch minus existing rows, and keeping i18n keys in both locale files "
        "whenever a screen was added. Windows TLS failures (cURL error 60) required SSL_CERT_FILE "
        "notes. CORS had to list ports 3000 and 3006. php artisan serve must be restarted after "
        ".env changes. Those operational details are part of implementation quality because a viva "
        "cannot distinguish “AI is broken” from a missing certificate."
    )

    b.h("4.3 Module Implementation", 2)
    b.h("4.3.1 Authentication, RBAC and session handling", 3)
    b.p(
        "Registration accepts patient or doctor. Doctors must send license_number and "
        "specialization. Login returns a bearer token. Protected routes expect Authorization: "
        "Bearer {token}. Admins are seeded, not self-registered. Middleware.ts sends unauthenticated "
        "users to /login, blocks non-admins from /admin/*, and sends admins who hit /login to "
        "/admin/dashboard. Cookies mh_token and mh_role help the App Router, but Laravel remains "
        "the authority. Zustand holds the session; Axios clears it on 401/419."
    )
    b.h("4.3.2 AI companion, providers and crisis scan", 3)
    b.p(
        "AI chat is patient-only: list sessions, start, load messages, post a message, end session. "
        "Each inbound user message is scanned before a model is called. A match creates crisis_alerts "
        "(severity low, medium, high, critical), returns a safety reply with referrals, and does not "
        "improvise around self-harm language. Otherwise the service tries Gemini (default "
        "gemini-2.5-flash) then Groq. If neither key is present, a local non-clinical fallback is "
        "returned so the UI remains demonstrable. AI_PROVIDERS encodes order in .env rather than in "
        "hard-coded vendor lock."
    )
    b.h("4.3.3 Appointments, availability and video-room metadata", 3)
    b.p(
        "GET /api/doctors/{id}/available-slots computes bookable times. POST /api/appointments "
        "creates pending rows with video-room metadata. PATCH .../status moves pending, confirmed, "
        "in_progress, completed, cancelled, and no_show. Nested admin routes manage weekly slots "
        "and lunch breaks as their own resources so booking logic does not become one untestable "
        "function. Enums avoid magic strings."
    )
    b.h("4.3.4 Admin console, library and reports", 3)
    b.p(
        "The admin console is the same Next.js app. Crisis PATCH updates status and notes. Doctor "
        "verify is the operational gate: until it succeeds, GET /api/doctors hides the account. "
        "Resources and referrals are locale-aware. Reports consume usage logs so evaluation can "
        "talk about platform activity rather than only screenshots."
    )
    b.h("4.3.5 Portal state, forms and i18n", 3)
    b.p(
        "TanStack Query holds lists that go stale when another actor changes them. Zustand holds "
        "the token. Forms use react-hook-form and Zod. i18next switches en.json and my.json without "
        "duplicating page files. A missing Myanmar key is immediately visible to a local tester, "
        "which is why language switching is a functional test rather than a visual extra."
    )

    b.h("4.4 Testing Strategy: Planned Versus Done", 2)
    b.p(
        "Testing combined design-artefact checks, php artisan test at service level, manual "
        "black-box walks on a fresh seed, and a short usability survey. Automated end-to-end UI "
        "frameworks were planned later and are recorded as future work rather than as completed."
    )
    b.h("4.4.1 Unit and script checks", 3)
    b.p(
        "php artisan test is the documented entry point for service-level assertions (phrase "
        "scanning and slot calculation) that do not need the browser. migrate:fresh --seed is the "
        "script that returns the database to a known demo state before a walkthrough."
    )
    b.h("4.4.2 Black-box testing", 3)
    b.p(
        "Black-box cases used seeded accounts only. Patient tests used patient@example.com, doctor "
        "tests used dr.smith@mentalhealth.local and unverified dr.hnin@mentalhealth.local, admin "
        "tests used admin@mentalhealth.local, and inactive-user behaviour used zaw.htet@example.com. "
        "Table 5.1 in Chapter 5 records the outcomes. Expected results were taken from README "
        "contracts, not from wishful design."
    )
    b.h("4.4.3 Integration testing", 3)
    b.p(
        "Integration walks chained login, language switch, AI message, crisis phrase, admin queue, "
        "therapist browse, booking, doctor status change, resources, logout, and reuse of an old "
        "token. Direct navigation to /admin/dashboard as a patient was used so that hiding a menu "
        "item could not fake RBAC."
    )
    b.h("4.4.4 Pathway and crisis evaluation", 3)
    b.p(
        "Unlike a trading project’s accuracy tables, this artefact is not scored on clinical "
        "sensitivity/specificity of a diagnostic model. The analogous “accuracy” checks are: crisis "
        "phrases produce alerts; ordinary phrases produce companion replies; unverified doctors "
        "do not appear; lunch-break slots do not appear. Those are binary contract tests."
    )
    b.h("4.4.5 Usability and demo checks", 3)
    b.p(
        "After the scripted walk, testers completed Appendix C items on login ease, pathway "
        "clarity, companion helpfulness, booking, language, safety, and recommendation likelihood. "
        "The sample is small and is not a clinical outcome study."
    )
    b.h("4.4.6 Artefact testing proof summary", 3)
    b.p(
        "Proof that the report matches the artefact is the combination of Figure 3.x diagrams "
        "checked against api.php, the seed table in Appendix C, GET /api/health, and Table 5.1. "
        "Where live Gemini keys were absent, T08 still had to return a safe fallback rather than "
        "an empty error page."
    )

    b.h("4.5 Summary", 2)
    b.p(
        "Chapter 4 implemented auth, AI, booking, admin, and i18n on the documented stack, and "
        "set a testing strategy that Chapter 5 now reports as outcomes."
    )
    extra_ch4(b)

    # ----- Chapter 5 -----
    b.page_break()
    b.h("Chapter 5: Testing and Evaluation")
    b.h("5.1 Functional Outcomes", 2)
    b.p(
        "Table 5.1 records the main black-box cases. T09 is ethically decisive: a companion that "
        "replies fluently to self-harm language would fail the project even if every other test "
        "passed. T02 is equally important: a patient who can open the crisis queue can read other "
        "people’s alerts."
    )
    b.table(
        ["ID", "Function", "Steps", "Expected", "Actual", "Status"],
        [
            ["T01", "Login (patient)", "POST /auth/login seeded patient", "Bearer token; portal", "Zustand session", "Pass"],
            ["T02", "RBAC admin", "Patient opens /admin/dashboard", "Blocked", "Middleware forbids", "Pass"],
            ["T03", "Register doctor", "Licence + specialisation", "Created, unverified", "Hidden from GET /doctors", "Pass"],
            ["T04", "Verify doctor", "Admin PATCH .../verify", "Appears in list", "Verified flag", "Pass"],
            ["T05", "Available slots", "GET .../available-slots", "Minus lunch and bookings", "Bookable times", "Pass"],
            ["T06", "Book session", "POST /appointments", "pending + video meta", "Listed both roles", "Pass"],
            ["T07", "Status update", "PATCH .../status", "Lifecycle advances", "Doctor/admin update", "Pass"],
            ["T08", "AI session", "Ordinary message", "Assistant reply stored", "Gemini/Groq or fallback", "Pass"],
            ["T09", "Crisis scan", "High-risk phrase", "Alert + safety reply", "Admin queue", "Pass"],
            ["T10", "Resources", "GET /resources, /referrals", "Library + hotlines", "Locale-aware", "Pass"],
            ["T11", "i18n", "Switch en / my", "Labels change", "No route change", "Pass"],
            ["T12", "Reports", "Admin GET /admin/reports", "Usage summary", "Logs in console", "Pass"],
            ["T13", "Logout", "POST /auth/logout", "Token revoked", "401 thereafter", "Pass"],
            ["T14", "Inactive user", "zaw.htet@example.com", "Rejected or limited", "Seed flag handled", "Pass"],
        ],
    )
    b.p(
        "Flaky observations were recorded without turning Pass into Fail. Live model latency "
        "sometimes caused double-send; the input is disabled while a message is in flight. Without "
        "keys, copy now states that a local safety reply is being used. Server time is the booking "
        "authority when browser and PHP disagree about local time."
    )

    b.h("5.2 Evaluation Methods", 2)
    b.h("5.2.1 Evaluation 1 — functional contract pass rate", 3)
    b.p(
        "Fourteen README-linked cases in Table 5.1 all passed on a fresh seed. This is the analogue "
        "of a hold-out accuracy table in a modelling project: it is a contract with the artefact, "
        "not a claim about population health."
    )
    b.h("5.2.2 Evaluation 2 — crisis and verification gates", 3)
    b.p(
        "The two gates that make dual pathways professionally legitimate were checked separately: "
        "crisis phrases never continue as normal chat, and unverified doctors never appear to "
        "patients. Both gates passed (T09, T03/T04)."
    )
    b.h("5.2.3 Evaluation 3 — usability survey", 3)
    b.p(
        "Testers reported that login and dashboard navigation were easy, that the choice between "
        "AI support and doctor consultation was obvious, that the companion helped for low-intensity "
        "distress, and that crisis tone-change increased trust. Myanmar labels were valued even "
        "when chat continued in English. Complaints concentrated on model latency and the absence "
        "of an in-app live video renderer. Open comments named dual choice, crisis/referral, and "
        "hidden unverified doctors as the most useful features."
    )

    b.h("5.3 Prototype Limits (Clear Reporting)", 2)
    b.p(
        "Internal validity is limited by a small, non-random tester group who knew they were "
        "evaluating a student project. Construct validity is limited because accessibility and "
        "engagement are prototype behaviours, not clinical scales. External validity is limited "
        "because the system ran locally with fictional doctors. Keyword crisis detection will miss "
        "oblique phrasing and over-flag harmless text. There was no randomised chatbot-only versus "
        "booking-only comparison. These limits make Chapter 6’s cautious wording mandatory."
    )

    b.h("5.4 Discussion Against the Academic Question", 2)
    b.p(
        "The literature predicted that a bounded companion would improve first contact and that "
        "telepsychiatry would serve users who need a human professional (Abd-Alrazaq et al., 2020; "
        "Stade et al., 2024; Hilty et al., 2013; Shore et al., 2018; Torous et al., 2021). The "
        "artefact made that choice concrete on one identity. The survey found that testers "
        "understood the two pathways and did not describe the AI as a replacement for a doctor. "
        "Rival explanations — novelty, calm visuals, demo passwords, demand characteristics — are "
        "partly accepted. The positive impact is clearest for accessibility of first contact and "
        "clarity of choice, and weaker for the richness of the live clinical encounter because "
        "video is metadata. Crisis handling is not a confounder to remove; it is part of the "
        "intervention that makes the question legitimate."
    )

    b.h("5.5 Summary", 2)
    b.p(
        "Functional contracts passed. Usability signals were directionally positive. Limits were "
        "stated. Chapter 6 answers the academic question and lists achievements, limitations, and "
        "future work."
    )
    extra_ch5(b)

    # ----- Chapter 6 -----
    b.page_break()
    b.h("Chapter 6: Conclusion")
    b.h("6.1 Achievements Against Objectives", 2)
    b.table(
        ["Item", "Statement", "Outcome", "Evidence"],
        [
            ["Aim", "Patient-directed hybrid platform", "Achieved", "Portal choice + API"],
            ["O1", "Next.js portal + i18n", "Achieved", "en/my, portal routes"],
            ["O2", "Laravel REST + RBAC", "Achieved", "T01, T02, T13"],
            ["O3", "Gemini/Groq + crisis scan", "Achieved", "T08, T09"],
            ["O4", "Booking + availability", "Achieved", "T05, T06, T07"],
            ["O5", "Admin console + library", "Achieved", "T04, T10, T12"],
            ["O6", "Schema, seed, tests, survey", "Achieved", "Seeder, Table 5.1, Appendix C"],
        ],
    )
    b.p(
        "Three discoveries are worth stating. First, patient choice is an interface problem as "
        "much as a clinical one. Second, LLM integration in this module is mostly a governance "
        "problem: keys, roles, and crisis routing matter more than prompt poetry. Third, bilingual "
        "copy is part of accessibility for Myanmar users, not a theme switch."
    )

    b.h("6.2 Answer to the Academic Question", 2)
    b.p(
        "Within a student prototype and a small tester group, offering an explicit patient-directed "
        "choice between a governed LLM companion and a telepsychiatry appointment is technically "
        "feasible, professionally responsible at prototype standard, and associated with tester "
        "reports of easier first contact and clearer next steps. Accessibility improved because "
        "support is available without clinic hours. Satisfaction improved where the two routes "
        "were obvious and unverified doctors were hidden. Engagement is plausible because the "
        "same identity can move from chat to booking. The claim that cannot be defended is that "
        "SerenityPath improves clinical outcomes or is ready for unsupervised public deployment."
    )

    b.h("6.3 Limitations", 2)
    b.bullets([
        "Third-party API latency and quota; local fallback is safe but not a live companion.",
        "Keyword crisis detection is explainable and incomplete.",
        "Video-room metadata is not a production media stack.",
        "Small usability n; no randomised single-pathway control.",
        "No national EHR, insurance, or clinical accreditation.",
    ])

    b.h("6.4 Future Work", 2)
    b.bullets([
        "Replace video-room metadata with a production video provider or TURN-backed WebRTC.",
        "Add Playwright tests around login, booking, and crisis posting.",
        "Classifier-assisted triage with a human still in the admin queue.",
        "Clinic partnership and ethics review for a longer study; do not claim efficacy from the current sample.",
        "Soft-delete, retention limits, and a subject-access process before any live deployment.",
    ])
    extra_ch6(b)

    # ----- Chapter 7 -----
    b.page_break()
    b.h("Chapter 7: Critical Evaluation and Professionalism")
    b.h("7.1 Process Reflection", 2)
    b.p(
        "Iterative delivery kept the safety-critical AI path from being postponed until the last "
        "week. Underestimated work included CORS and TLS on Windows, slot arithmetic, and i18n of "
        "every new screen. Balancing implementation with report writing remained the main tension. "
        "Figure 7.1 is an indicative 24-week plan used to keep milestones visible: proposal, "
        "literature, schema and API, AI and booking, admin and survey, then the report."
    )
    b.figure(figs / "fig_gantt.png",
             "Figure 7.1: Indicative Gantt chart for the 6CS007 calendar.")
    b.p(
        "If the project were restarted, an OpenAPI contract would be written before UI styling, "
        "and Playwright would start as soon as login worked. Seeding an unverified doctor and an "
        "inactive patient on day one would still be done first, because those rows test rules that "
        "happy-path screenshots never show."
    )

    b.h("7.2 Ethics and Risk Communication", 2)
    b.p(
        "Testers were told that conversations may be stored locally, that the AI is not a doctor, "
        "and that crisis phrases notify an administrator. The companion must not be presented to "
        "the public as a licensed clinical service. Demo accounts use fictional local-part emails. "
        "Risk communication in the UI is the safety banner and referral list, not a buried terms "
        "page. Keyword limits are disclosed in Chapters 5 and 6 so that a marker cannot think the "
        "scanner is a validated clinical instrument."
    )

    b.h("7.3 Legal and Academic Integrity", 2)
    b.p(
        "Passwords are hashed. Keys are server-side. Role isolation prevents URL-guessing across "
        "roles. The report and survey do not publish real patient identifiers. Sources for LLM and "
        "telepsychiatry claims are peer-reviewed or professional (Stade et al., 2024; Guo et al., "
        "2024; Hilty et al., 2013; Shore et al., 2018; Torous et al., 2021; Abd-Alrazaq et al., "
        "2020; BCS, 2021; ICO, 2023). Vendor pages were used only to confirm product names. The "
        "declaration sheet at the front of this document is the academic-integrity statement. "
        "Live Gemini/Groq calls send prompt text to a third-party processor; that is disclosed in "
        "Appendix B."
    )

    b.h("7.4 Summary", 2)
    b.p(
        "The artefact is strongest where the academic question is strongest: one identity, two "
        "pathways, server-side AI, and an admin crisis queue. It is weaker as a telepsychiatry "
        "product than as an access product. Process, ethics, and integrity choices were recorded "
        "so that the dual-pathway contribution can be marked without mistaking a prototype for a "
        "clinic."
    )

    # ----- References -----
    b.page_break()
    b.h("References")
    refs = [
        "Abd-Alrazaq, A.A., Alajlani, M., Alalwan, A.A., Bewick, B.M., Gardner, P. and Househ, M. (2020) ‘An overview of the features of chatbots in mental health: a systematic review’, International Journal of Medical Informatics, 132, 103978.",
        "BCS (2021) BCS Code of Conduct. Swindon: BCS, The Chartered Institute for IT.",
        "Google (2026) Gemini API documentation. Available at: https://ai.google.dev/ (Accessed: 17 August 2026).",
        "Groq (2026) Groq API documentation. Available at: https://console.groq.com/docs (Accessed: 17 August 2026).",
        "Guo, Z. et al. (2024) ‘Large language models for mental health applications: systematic review’, JMIR Mental Health.",
        "Hilty, D.M., Ferrer, D.C., Parish, M.B., Johnston, B., Callahan, E.J. and Yellowlees, P.M. (2013) ‘The effectiveness of telemental health: a 2013 review’, Telemedicine and e-Health, 19(6), pp. 444–454.",
        "Information Commissioner’s Office (2023) Guide to the General Data Protection Regulation (GDPR). Available at: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/ (Accessed: 17 August 2026).",
        "Laravel (2026) Laravel documentation. Available at: https://laravel.com/docs (Accessed: 17 August 2026).",
        "Lee, M.S. et al. (2020) Factors affecting the adoption of digital health systems: UTAUT and information-system quality perspectives, as discussed in Chapter 2.",
        "Next.js (2026) Next.js App Router documentation. Available at: https://nextjs.org/docs (Accessed: 17 August 2026).",
        "Shore, J.H. et al. (2018) ‘Best practices in videoconferencing-based telemental health’, Telemedicine and e-Health, 24(11), pp. 827–832.",
        "Stade, E.C. et al. (2024) ‘Large language models could change the future of behavioral healthcare: a proposal for responsible development and evaluation’, npj Mental Health Research.",
        "Torous, J., Bucci, S., Bell, I.H. et al. (2021) ‘The growing field of digital psychiatry: current evidence and the future of apps, social media, chatbots, and virtual reality’, World Psychiatry, 20(3), pp. 318–335.",
    ]
    for ref in refs:
        b.p(ref, justify=False, space_after=8)

    b.page_break()
    b.h("Appendix A: Glossary of Terms")
    glossary = [
        "Bearer token — secret string sent as Authorization: Bearer {token} on protected API routes.",
        "Crisis alert — database row created when an inbound AI message matches a high-risk phrase.",
        "Patient-directed — after login, the user chooses AI support or human booking; neither is a hidden funnel.",
        "RBAC — role-based access control for patient, doctor, and admin.",
        "Video-room metadata — stored identifier for a telepsychiatry session; not a full WebRTC client in this iteration.",
        "Verified doctor — doctor record that an admin has approved for public listing.",
    ]
    for g in glossary:
        b.p(g, justify=False, space_after=6)

    b.h("Appendix B: Reproducibility Notes")
    b.p(
        "Start the API first: cd mental_health_api; composer install; copy .env; php artisan key:generate; "
        "php artisan migrate:fresh --seed; php artisan serve. Then cd mental_health_web; npm install; "
        "set NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000/api; npm run dev. Open http://localhost:3006. "
        "Health check: GET /api/health. Restart php artisan serve after changing .env. Optional Gemini "
        "and Groq keys enable live replies; without them a local fallback is used. CORS must include "
        "port 3006. On Windows cURL error 60, set SSL_CERT_FILE as in the README. Demo password for "
        "every seeded account is password and must not be used on a public host. Live model calls send "
        "prompt text to Google or Groq."
    )

    b.h("Appendix C: Extra Assessor Notes")
    b.h("C1. Demo accounts (local seed only)", 2)
    b.p("Password for every seeded account: password (local development only).", justify=False)
    b.table(
        ["Role", "Email", "Notes"],
        [
            ["Admin", "admin@mentalhealth.local", "Full admin console"],
            ["Doctor", "dr.smith@mentalhealth.local", "Verified"],
            ["Doctor", "dr.aung@mentalhealth.local", "Verified"],
            ["Doctor", "dr.thiri@mentalhealth.local", "Verified"],
            ["Doctor", "dr.win@mentalhealth.local", "Verified"],
            ["Doctor", "dr.hnin@mentalhealth.local", "Unverified"],
            ["Patient", "patient@example.com", "Primary demo patient"],
            ["Patient", "zaw.htet@example.com", "Inactive"],
        ],
    )
    b.h("C2. User survey questions", 2)
    for q in [
        "1. I found it easy to sign in to SerenityPath.",
        "2. It was clear that I could choose AI support or a human doctor.",
        "3. I could obtain some form of support without visiting a clinic.",
        "4. The AI companion felt respectful and non-judgemental.",
        "5. I understood that the AI companion is not a doctor and cannot diagnose.",
        "6. Booking an appointment with a verified doctor was straightforward.",
        "7. I trust that unverified doctors are not shown to patients.",
        "8. If I entered crisis language, the system’s response felt appropriate.",
        "9. The English / Myanmar language switch was useful.",
        "10. How likely are you to recommend SerenityPath as a first step into support? (0–10)",
        "11. What is the most useful feature? (long answer)",
        "12. What should be improved next? (long answer)",
    ]:
        b.p(q, justify=False, space_after=4)
    b.h("C3. Ethics note", 2)
    b.p(
        "This is a student prototype. It must not be presented as a licensed clinical service. "
        "No real clinical records were imported. A centre ethics form, if required, should be bound "
        "behind this appendix."
    )
    b.h("C4. Suggested viva slice", 2)
    b.p(
        "Seed login as patient, send a crisis phrase, inspect the admin queue, then book dr.smith "
        "from an available slot. That slice touches professionalism, the academic question, and "
        "the README in one demonstration."
    )
