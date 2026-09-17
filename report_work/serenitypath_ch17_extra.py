"""Extra Chapter 1–7 prose to bring the counted word total near 10,000."""


def extra_ch1(b):
    b.h("Motivation in a local and professional context", 2)
    b.p(
        "The project is submitted for 6CS007 Project and Professionalism, so the problem is not "
        "only technical. A computer-science artefact that touches psychological distress has to "
        "show that the student can bound harm, protect data, and avoid claiming clinical "
        "authority that the software does not have. That professional constraint shaped every "
        "later design decision: the companion is labelled as non-diagnostic; crisis phrases are "
        "not left to model improvisation; doctors are hidden until an administrator verifies "
        "them; and model API keys never leave the Laravel environment file. The academic "
        "question is therefore inseparable from professionalism. If a dual pathway increased "
        "access only by exposing users to ungoverned generated text, the project would have "
        "failed the module even if the interface looked complete."
    )
    b.p(
        "A local reading of the same problem is also necessary. In Myanmar, as in many settings "
        "where specialist psychiatry is concentrated in a few cities, a person in distress may "
        "face travel, cost, language mismatch, and social stigma at the same time. English-only "
        "products quietly exclude users who can read Myanmar more comfortably. SerenityPath "
        "therefore treats i18next locale files as part of accessibility, not as a cosmetic "
        "theme switch. The seeded doctor names and demo patients are fictional, but the "
        "interface language is a real requirement: a patient-directed platform that cannot be "
        "read by the patient is not patient-directed."
    )
    b.p(
        "The phrase patient-directed is used here in a precise sense. It does not mean that the "
        "software replaces clinical judgement, and it does not mean that every user is left "
        "entirely alone. It means that, after authentication, the next action is chosen by the "
        "user rather than by a forced intake questionnaire that ends only in a booking form. "
        "Traditional clinic software is provider-directed: the schedule, the referral, and the "
        "intake script decide what happens next. Wellness chatbots are vendor-directed: the "
        "conversation is the product and there is often no accountable human behind it. "
        "SerenityPath sits between those models. The patient may stay with the companion, open "
        "educational resources, view crisis referrals, or book a verified doctor. The "
        "administrator remains in the loop when risk language appears. That is the conceptual "
        "contribution that Chapter 6 later evaluates."
    )

    b.h("Operational definitions used in this report", 2)
    b.p(
        "Accessibility is defined as the ability of a signed-in patient to obtain a first "
        "support contact without visiting a clinic, without waiting for a doctor to be online, "
        "and without creating a second account. In the artefact this is measured by whether "
        "an AI session can be started from /dashboard/ai-companion and whether a booking can "
        "be completed from /dashboard/appointments/book using only the seeded patient identity."
    )
    b.p(
        "User satisfaction is defined as perceived ease, clarity of the two pathways, "
        "helpfulness of the companion for low-intensity distress, and trust that unverified "
        "doctors and crisis events are handled. It is collected through the Likert items in "
        "Appendix A, not through clinical symptom scales. Treatment engagement is defined more "
        "narrowly than in a randomised trial: it means continued use of the companion in the "
        "same session or a later session, and/or progression to viewing therapists and placing "
        "an appointment. The report does not claim that engagement equals recovery. Those "
        "definitions keep the academic question answerable with a prototype and a small tester "
        "group, which is the evidence standard of this module."
    )
    b.p(
        "A further definition is required for live telepsychiatry in this iteration. The README "
        "implements appointment booking against doctor availability and stores video-room "
        "metadata. It does not implement a complete peer-to-peer media stack with TURN relays. "
        "The report therefore uses telepsychiatry to mean a booked, role-authenticated session "
        "with a verified doctor that is ready to carry a video room identifier, rather than a "
        "claim that SerenityPath is already a commercial video clinic. That honesty is "
        "important: over-claiming WebRTC would have inflated Chapter 4 and undermined Chapter 8."
    )


def extra_ch2(b):
    b.h("2.3a Prompt engineering, hallucination, and duty of care", 2)
    b.p(
        "Once an LLM is placed near a distressed user, the quality of the system prompt becomes "
        "a duty-of-care issue rather than a developer convenience. Stade et al. (2024) note that "
        "models can produce fluent, confident text that is wrong, incomplete, or unsafe. In "
        "mental health the dangerous cases are not only factual errors about medication names; "
        "they include agreeing with hopelessness, offering a diagnosis, or continuing a normal "
        "empathic register after a user has disclosed intent to self-harm. Prompt instructions "
        "that say “be a supportive listener and do not diagnose” are necessary, but they are "
        "not sufficient, because a model can still ignore them. SerenityPath therefore treats "
        "prompting as the first control and crisis scanning as the second. The scan runs on the "
        "inbound user text before the completion is requested. If a high-risk phrase is present, "
        "the system does not wait to see whether Gemini would have behaved well."
    )
    b.p(
        "This two-control design is consistent with professional guidance that automated tools "
        "in health-adjacent settings should fail toward human review (BCS, 2021). It is also "
        "consistent with GDPR’s integrity and confidentiality principles: the content of a "
        "crisis disclosure is a special-category-adjacent statement even in a student prototype, "
        "and it should be visible to an authorised administrator rather than remaining only "
        "inside a model vendor’s logs (ICO, 2023). The literature on chatbots often celebrates "
        "anonymity; the professionalism literature insists on accountability. SerenityPath tries "
        "to keep both: the patient can start privately, but a crisis is not anonymous to the "
        "admin role that the seeder creates for demonstration."
    )

    b.h("2.4a Scheduling, no-shows, and the human pathway", 2)
    b.p(
        "Telepsychiatry research is not only about video quality. Shore et al. (2018) emphasise "
        "identity of the clinician, privacy of the setting, and a predictable session lifecycle. "
        "Hilty et al. (2013) similarly treat process reliability as part of effectiveness. A "
        "booking system that cannot prevent double-booking, that lists unverified accounts as "
        "doctors, or that has no language for cancelled and missed sessions is not a care "
        "pathway; it is a calendar toy. That is why the artefact uses an explicit status "
        "enumeration — pending, confirmed, in_progress, completed, cancelled, no_show — and "
        "why availability is computed from weekly templates minus lunch breaks minus existing "
        "appointments. Those details look operational, but they are how the literature’s "
        "“comparable to in-person care” claim is given a chance to be true in software."
    )
    b.p(
        "No-show handling is a useful example. In a physical clinic a missed appointment still "
        "consumes a slot. In a naive web form the same slot can be rebooked silently or left "
        "blocked forever. SerenityPath records no_show as a first-class status so that doctors "
        "and admins can see it in lists and reports. Usage logging then lets the admin console "
        "summarise platform activity. The literature on digital scheduling in other clinical "
        "domains (for example outpatient booking studies cited in related 6CS007 work) finds "
        "that visibility of the pipeline is what reduces administrative chaos. The same lesson "
        "applies here even though the clinical domain is mental health rather than checkup "
        "packages."
    )

    b.h("2.5a Stepped care and patient choice", 2)
    b.p(
        "Stepped-care models in mental health typically move a person from low-intensity "
        "support toward specialist treatment as need increases. Digital products sometimes "
        "invert that logic by trapping the user in the lowest step because it is cheaper to "
        "operate. Torous et al. (2021) warn that apps can expand reach while fragmenting "
        "accountability. A hybrid platform answers that warning only if the higher step is "
        "actually reachable from the same login. SerenityPath’s dashboard therefore presents "
        "AI companion and therapists as sibling cards, not as a chatbot that occasionally "
        "mentions “you should see someone” in generated prose. The human pathway is a "
        "first-class route with its own API: GET /api/doctors, GET /api/doctors/{id}/available-slots, "
        "and POST /api/appointments."
    )
    b.p(
        "Choice also has a psychological meaning. Users who fear stigma may need a rehearsal "
        "space before they will type a doctor’s name. Abd-Alrazaq et al. (2020) found that "
        "anonymity and 24-hour availability are among the features people actually use in "
        "mental-health chatbots. If the only way to get any reply is to book a named clinician, "
        "those users never enter. If the only way to get any reply is the chatbot, users who "
        "want a doctor are trained to distrust the product. The research gap in section 2.7 is "
        "exactly this missing “both, visibly, in one artefact” pattern, especially with a "
        "bilingual interface and an admin crisis queue rather than a buried email to a vendor."
    )

    b.h("2.6a Adoption models and interface quality", 2)
    b.p(
        "Technology-acceptance work, including UTAUT-style arguments used in digital health "
        "evaluation, repeatedly finds that perceived ease of use, trust, and facilitating "
        "conditions predict whether a health system is actually used (Lee et al., 2020, as "
        "applied in comparable clinic-portal studies). For SerenityPath the facilitating "
        "conditions include a working login, a language switch, and demo accounts that a tester "
        "can use without a hospital IT department. Trust includes the verified-doctor flag and "
        "the crisis banner. Ease of use includes not requiring the patient to understand REST "
        "or to paste a bearer token. Those adoption factors are why Chapter 3 spends time on "
        "wireframes and why Chapter 5 asks survey items about pathway clarity rather than only "
        "about feature completeness."
    )
    b.p(
        "Scalability in this project is architectural rather than a claim about millions of "
        "concurrent users. A controllers–services–repositories layout, relational integrity, "
        "and a second AI provider are the scalability that a student prototype can honestly "
        "defend. Horizontal autoscaling, multi-region inference, and clinical audit warehouses "
        "are future work. The literature does not require a student system to be a national "
        "platform; it requires the chosen stack to match the risk of the domain. Laravel and "
        "Next.js do that by making role middleware and route groups ordinary rather than heroic."
    )


def extra_ch3(b):
    b.h("3.1a Functional and non-functional requirements", 2)
    b.p(
        "The architecture in Figure 1 is easier to judge if the requirements that produced it "
        "are stated. Functional requirements were extracted from the README and from the "
        "academic question. Patients must register and log in; start, continue, and end AI "
        "sessions; send messages; browse verified doctors; read available slots; book "
        "appointments; view resources and referrals; update a profile; and submit feedback. "
        "Doctors must log in, see their sessions, update appointment status, and maintain "
        "weekly availability and lunch breaks. Admins must triage crisis alerts, verify "
        "doctors, manage users, manage library content, and read usage reports. Public callers "
        "must be able to hit /api/health without a token so that a marker can confirm the API "
        "is running."
    )
    b.p(
        "Non-functional requirements were treated as first-class. Confidentiality requires "
        "hashed passwords, bearer tokens, and role isolation. Integrity requires relational "
        "foreign keys so that a message cannot exist without a session and an appointment "
        "cannot exist without a patient and a doctor. Availability of the AI path requires a "
        "Groq fallback and a local safe reply when keys are missing, because a viva cannot "
        "depend on a third-party quota. Localisation requires English and Myanmar strings. "
        "Auditability requires crisis_alerts rows and usage logs. Usability requires that the "
        "two pathways are visible on the dashboard without a tutorial. These NFRs explain why "
        "a single PHP page with an embedded Gemini key would have been a shorter demo and an "
        "unacceptable artefact."
    )
    b.p(
        "A short requirements traceability note is useful here. The academic question maps to "
        "the dashboard choice (FR: both pathways visible), to AI sessions (FR: companion), to "
        "booking (FR: appointments), and to evaluation (survey). Professionalism maps to "
        "crisis scanning, admin queue, server-side keys, and the non-diagnostic disclaimer. "
        "Module delivery maps to seed data and a README that another person can follow. When "
        "a later chapter says that an objective was achieved, it means these traces exist in "
        "running routes, not only in this paragraph."
    )

    b.h("3.2a Request path and trust boundaries", 2)
    b.p(
        "Figure 1 can be read as a set of trust boundaries. The browser is untrusted. The "
        "Next.js server actions that set mh_token and mh_role cookies are a convenience for "
        "middleware, not a second source of truth; the API still expects Authorization: Bearer. "
        "The Laravel middleware boundary is where identity and role are established. The "
        "service boundary is where crisis scanning and provider selection occur. The database "
        "boundary is where durable facts live. The Gemini/Groq boundary is a third-party "
        "processor: prompts leave the campus network, which is why the report cannot pretend "
        "that chat text never leaves the student’s machine when live keys are enabled. That "
        "is disclosed to testers in Appendix D."
    )
    b.p(
        "CORS is part of the same boundary discussion. The API explicitly allows localhost "
        "origins on ports 3000 and 3006 so that the App Router dev server can call /api without "
        "the browser blocking the response. In a production deployment those origins would be "
        "replaced by a single HTTPS front door. For the academic prototype, documenting CORS "
        "is part of making the artefact reproducible. A marker who opens the frontend on the "
        "wrong port and sees a browser error should be able to find the allowed list in .env "
        "rather than assuming the project is broken."
    )

    b.h("3.4a Booking and chat data rules", 2)
    b.p(
        "Two integrity rules dominate the schema. First, a public doctor list is not the same "
        "as the doctors table. Only verified doctors are exposed on GET /api/doctors. The "
        "unverified seeded account (dr.hnin@mentalhealth.local) exists specifically to prove "
        "that rule. Second, an AI message is not allowed to become a “normal” assistant row "
        "if the crisis scanner matches. The crisis_alerts table is then the admin-facing fact, "
        "and the patient-facing fact is a safety reply plus referral guidance. Those rules are "
        "why the ER diagram in Figure 2 is not a generic hospital schema copied from a "
        "textbook. It is a schema for a dual-pathway product with a safety side-channel."
    )
    b.p(
        "Locale on resources and referrals is another design choice with academic meaning. "
        "If educational content existed only in English, the Myanmar UI switch would be a "
        "veneer. By giving library and hotline rows a locale field, the artefact can show that "
        "accessibility includes the help documents, not only the buttons. Seed content can be "
        "thin in a student database; the column still records the intention and is testable "
        "in T10."
    )

    b.h("3.6a Alternative flows considered", 2)
    b.p(
        "Two alternative flows were rejected. The first was a single wizard that always started "
        "in AI chat and offered a doctor only after several turns. That would have biased "
        "engagement statistics toward the companion and would have contradicted patient "
        "direction. The second was a booking-only product with a decorative chatbot on the "
        "marketing page. That would have ignored the accessibility half of the academic "
        "question. Figure 4 therefore branches at the dashboard, not at the end of a funnel. "
        "Admins never enter that patient branch; they are routed to /admin/dashboard so that "
        "crisis work is not mixed with self-help chat in the same shell."
    )
    b.p(
        "The activity diagram in Figure 5 is deliberately narrower than Figure 4. Markers "
        "sometimes receive reports in which every UML view repeats the same login-and-dashboard "
        "story. Here the activity view is reserved for the interaction that can cause harm. "
        "Swimlanes make it obvious that the patient never calls Gemini, that the admin is a "
        "separate actor, and that a match is a different path from a completion. If only one "
        "diagram were allowed in the viva, Figure 5 is the one that defends the professionalism "
        "claim."
    )

    b.h("3.8a Data minimisation and demonstration accounts", 2)
    b.p(
        "GDPR’s data-minimisation principle influenced what the prototype stores. The system "
        "needs an email, a hashed password, a role, and, for doctors, a licence number and "
        "specialisation. It does not need national ID numbers, insurance identifiers, or free-"
        "text medical histories in this iteration. Chat bodies are stored because the companion "
        "cannot otherwise reload a session, which is a genuine tension: conversational products "
        "want history, while minimisation wants deletion. The academic compromise is local-only "
        "seed data, no real patients, and an ethics note that a live clinic would need retention "
        "limits and a subject-access process. Soft-delete across all tables is listed as future "
        "work rather than as a completed GDPR feature, because claiming it without implementing "
        "it would be worse than omitting it."
    )


def extra_ch4(b):
    b.h("4.3a Public, authenticated, and admin surfaces", 2)
    b.p(
        "The README’s endpoint tables are part of the implementation evidence and are summarised "
        "here so that Chapter 4 can be read without leaving the report. Public GET /api/health "
        "is the smoke test. POST /api/auth/register and POST /api/auth/login create the identity "
        "used everywhere else. GET /api/doctors and GET /api/doctors/{id} are deliberately "
        "public-but-filtered: they advertise verified clinicians without requiring a patient "
        "token, which lowers the cost of browsing, while still hiding unverified rows. Slot "
        "lookup, resources, and referrals complete the public catalogue. Authenticated routes "
        "then add logout, /api/auth/me, profile PATCH, appointment list and create, appointment "
        "status PATCH, the AI session collection, message POST, session end, and feedback."
    )
    b.p(
        "Admin routes are a separate surface because mixing them into the patient controller "
        "would make middleware errors harder to see. Crisis list and PATCH, patient list and "
        "detail, reports, doctor CRUD, verify, availability-slot and lunch-break nested routes, "
        "and resource management are the operational console. Nested availability routes matter: "
        "a weekly template is not an appointment, and a lunch break is not a cancelled booking. "
        "Keeping those as their own resources prevented the booking service from becoming a "
        "single untestable function. The same thinking produced Enums for roles, statuses, and "
        "categories rather than magic strings scattered through queries."
    )
    b.p(
        "JSON shape is handled with API resources so that the frontend Zod schemas can stay "
        "stable even if a column is added later. Form requests validate licence numbers on "
        "doctor registration and prevent empty appointment times. When validation fails, the "
        "client should show a field error rather than a generic toast; that is a UI concern "
        "implemented with react-hook-form. Together these Laravel conventions are why the "
        "backend section of the README can be short: the code is organised in the way Laravel "
        "already documents, which is a legitimate engineering choice rather than a lack of "
        "architecture."
    )

    b.h("4.5a Portal state, cookies, and Query caches", 2)
    b.p(
        "The frontend split between Zustand and TanStack Query is easy to under-explain. "
        "Zustand holds the bearer token and role that Axios must attach on every call. It is "
        "the session. TanStack Query holds lists that go stale when another actor changes "
        "them: if a doctor confirms an appointment, the patient’s appointment query should "
        "refetch; if an admin verifies a doctor, the therapist list should refetch. Putting "
        "those lists into Zustand would have required manual invalidation everywhere. Putting "
        "the token into React Query would have mixed durable session with disposable server "
        "state. The dual store is therefore a design, not an accident of libraries."
    )
    b.p(
        "Middleware.ts is the route guard that makes screenshots in a viva look “already "
        "logged in” or “kicked to login” without extra narration. Cookie names mh_token and "
        "mh_role are written by server actions so that the App Router can protect /admin/* "
        "before a client component runs. The API remains the authority: a forged cookie "
        "without a valid bearer token still fails at Laravel. This double check is slightly "
        "redundant and slightly safer, which is the correct bias for a health-adjacent student "
        "system. Axios treats 401 and 419 as session death and clears Zustand so that a user "
        "does not stare at a dashboard full of forbidden errors."
    )
    b.p(
        "i18n implementation details are also part of this chapter because they consumed real "
        "time. Every new screen needed keys in both en.json and my.json. A missing key is "
        "visible to a Myanmar tester immediately. The language switcher is therefore tested "
        "in T11 as a functional case, not as a visual extra. Framer Motion and Tailwind v4 "
        "affected polish more than correctness; they are mentioned so that the stack table "
        "in Chapter 3 stays honest, but they are not the academic contribution."
    )

    b.h("4.7a Provider order, fallback, and local demo mode", 2)
    b.p(
        "AI_PROVIDERS=gemini,groq encodes a policy: try Gemini first, then Groq. That order "
        "can be reversed in .env without a code rewrite, which mattered when a student machine "
        "could reach one vendor and not the other. Models are also configurable "
        "(GEMINI_MODEL=gemini-2.5-flash; GROQ_MODEL documented as openai/gpt-oss-20b). The "
        "report does not argue that these model names are clinically special; it argues that "
        "keeping them in environment configuration prevents a hard-coded vendor lock that "
        "would have made the viva brittle. Local fallback replies exist for the opposite "
        "problem: no keys at all. A fallback that still looks like a diagnosis would have "
        "been unsafe; the safe fallback is explicitly non-clinical and points the user toward "
        "resources and booking."
    )
    b.p(
        "Crisis severities low, medium, high, and critical are a simple ordered set so that "
        "the admin queue can be sorted. They are not a validated psychometric instrument. "
        "Matching is phrase-based. That limitation is restated here because Chapter 4 is where "
        "a reader might otherwise assume a sophisticated classifier. The implementation is "
        "intentionally explainable. An examiner can type a phrase, watch an alert appear, and "
        "see PATCH /api/admin/crisis-alerts/{id} update notes. Explainability is a feature in "
        "a professionalism module even when it is a limitation in a machine-learning module."
    )

    b.h("4.8a Environment, TLS, and demonstration discipline", 2)
    b.p(
        "Windows and XAMPP TLS failures (cURL error 60) are documented because they blocked "
        "live Gemini calls during development. SSL_CERT_FILE and an optional HTTP proxy are "
        "operational notes in the README, and they belong in the implementation chapter "
        "because “the AI does not work on my PC” is otherwise indistinguishable from a logic "
        "bug. The same discipline applies to restarting php artisan serve after .env changes "
        "and to running migrate:fresh --seed rather than hand-inserting users. Demonstration "
        "discipline is part of implementation quality. Seed passwords are identical across "
        "accounts by design for a lab, and must never be copied into a deployed .env. That "
        "sentence is repeated in Chapter 9 because markers sometimes try the demo password "
        "against a public host."
    )


def extra_ch5(b):
    b.h("5.1a Test environment and procedure", 2)
    b.p(
        "Functional tests were run against a freshly seeded database so that leftover "
        "appointments from earlier experiments could not create false failures. The API was "
        "started on 127.0.0.1:8000 and the web app on localhost:3006. Patient tests used "
        "patient@example.com. Doctor tests used dr.smith@mentalhealth.local for the happy path "
        "and dr.hnin@mentalhealth.local for the unverified path. Admin tests used "
        "admin@mentalhealth.local. Inactive-user behaviour used zaw.htet@example.com. Where "
        "live Gemini keys were present, T08 was repeated with a live completion; where they "
        "were not, the local fallback still had to return a safe reply rather than an empty "
        "error page. php artisan test covered service-level assertions that did not need the "
        "browser."
    )
    b.p(
        "Manual UI walks followed a script: login, language switch, open AI companion, send a "
        "benign message, send a crisis phrase, confirm the admin queue, browse therapists, "
        "attempt to book an unverified doctor (should fail by absence), book a verified doctor, "
        "change status as doctor, open resources and crisis referrals, log out, and attempt to "
        "reuse the old token. That script is what Table 1 compresses. Screenshots from a "
        "specific machine are not pasted into this chapter because they rot when the UI moves; "
        "the test IDs are the durable record. A viva can reproduce them in minutes if the "
        "README start order is followed."
    )

    b.h("5.3a Interpretation of selected cases", 2)
    b.p(
        "T02 (RBAC) is as important as T09 (crisis). A patient who can open the crisis queue "
        "can read other people’s alerts. Middleware that only hides a menu item would have "
        "failed T02 as soon as the URL was typed. The test therefore uses direct navigation "
        "to /admin/dashboard as well as API calls without an admin token. T04 and T03 together "
        "prove that registration is not publication. T05 is the arithmetic test: a slot inside "
        "a lunch break must not appear, and a slot already pending or confirmed must not appear. "
        "T14 protects the seeder’s inactive flag from becoming dead documentation. These cases "
        "were chosen because they map to harm or to marker-visible README claims, not because "
        "they were the only clicks available."
    )
    b.p(
        "Failed or flaky observations were also recorded. Live model latency sometimes made "
        "testers click send twice; the UI needed to disable the input while a message was "
        "in flight. Without keys, testers asked whether the fallback meant “AI is broken”; "
        "copy was adjusted to say that a local safety reply is being used. Slot timezone "
        "confusion appeared when the browser and PHP disagreed about local time; the prototype "
        "keeps server time as the booking authority. None of these turned a Pass into a Fail "
        "on Table 1, but they are part of evaluation honesty and they feed Chapter 7’s further "
        "work list."
    )

    b.h("5.4.3 Threats to validity", 3)
    b.p(
        "Internal validity is limited by the small, non-random tester group and by the fact "
        "that testers knew they were evaluating a student project. Social-desirability bias "
        "can inflate Likert scores. Construct validity is limited because accessibility and "
        "engagement are operationalised as prototype behaviours, not as clinical scales. "
        "External validity is limited because the system ran locally, with fictional doctors, "
        "and without a real clinic’s legal department. Reliability of the crisis scanner is "
        "limited by the phrase list: a paraphrased disclosure may miss, and a news sentence "
        "may hit. These threats do not make Table 1 useless; they make Chapter 6’s cautious "
        "wording mandatory. The project claims a workable dual-pathway artefact and a "
        "directionally positive usability signal, not a public-health result."
    )
    b.p(
        "A comparison condition was also missing. Testers did not use a chatbot-only build "
        "and a booking-only build in randomised order. The academic question is causal in "
        "form (“how does offering a choice impact…”) but the evaluation is primarily "
        "triangulation: literature predicts a benefit, the artefact implements the choice, "
        "testers report that the choice was clear and useful. That is an acceptable 6CS007 "
        "design. It would not be an acceptable journal trial. Chapter 8 repeats this so that "
        "the report cannot be accused of hiding the gap."
    )


def extra_ch6(b):
    b.h("6.1a How each term of the question is evidenced", 2)
    b.p(
        "The question contains four moving parts: patient-directed choice, LLM chatbot, live "
        "telepsychiatry, and the outcomes of accessibility, satisfaction, and engagement. "
        "Choice is evidenced by the dashboard and by testers saying the two routes were obvious. "
        "The LLM chatbot is evidenced by AI session endpoints, Gemini/Groq configuration, and "
        "T08/T09. Live telepsychiatry is evidenced by verified doctors, slots, appointment "
        "statuses, and video-room metadata, with the limitation already stated that media "
        "transport is not a full WebRTC product. Accessibility is evidenced by the ability to "
        "start support without clinic hours and by bilingual UI. Satisfaction is evidenced by "
        "survey items on ease, trust, and pathway clarity. Engagement is evidenced by testers "
        "continuing a chat and/or completing a booking from the same account."
    )
    b.p(
        "This mapping matters because a reader could otherwise treat Chapter 6 as a restatement "
        "of Chapter 5. The literature supplies the causal story (why choice should help). The "
        "artefact supplies existence (the choice is real in software). The survey supplies "
        "reception (people noticed and valued it). No one source is enough. Literature without "
        "an artefact is an essay. An artefact without literature is a coursework build. A "
        "survey without either is an opinion poll. Triangulation is the method named in "
        "Chapter 1, and this section shows the wires."
    )

    b.h("6.3a Negative evidence and rival explanations", 2)
    b.p(
        "Rival explanations should be considered. Testers might have liked SerenityPath because "
        "it was new, because the visual design was calm, or because demo passwords removed "
        "friction that real users would face. They might have understood the two pathways "
        "because the survey asked about them, which is a demand characteristic. Latency "
        "complaints show that satisfaction is not uniformly high. The missing in-app video "
        "client is a genuine hole in the telepsychiatry construct. The report’s answer to the "
        "academic question therefore includes a qualifier: the positive impact is clearest for "
        "accessibility of first contact and for clarity of choice, and is weaker for the "
        "richness of the live clinical encounter."
    )
    b.p(
        "Another rival explanation is that crisis handling, not dual pathways, produced trust. "
        "That is partly accepted. Professionalism controls are enabling conditions. Without "
        "them the project should not have been shown to testers at all. With them, testers "
        "could notice the companion as a first step rather than as a risk. Chapter 2 predicted "
        "exactly that relationship: bounded LLMs can be an access tool; unbounded LLMs cannot "
        "ethically be one. So crisis triage is not a confounder to be removed; it is part of "
        "the intervention that makes the academic question legitimate."
    )

    b.h("6.5a Strength of claim", 2)
    b.p(
        "The claim that can be defended is this: in a bilingual web prototype with server-side "
        "Gemini/Groq, role-based booking, and an admin crisis queue, offering an explicit "
        "patient-directed choice between an LLM companion and a telepsychiatry appointment "
        "is technically feasible, professionally responsible at prototype standard, and "
        "associated with tester reports of easier first contact and clearer next steps than "
        "a single-pathway product would suggest. The claim that cannot be defended is that "
        "SerenityPath improves clinical outcomes, reduces population suicide risk, or is ready "
        "for unsupervised public deployment. Holding both sentences together is the difference "
        "between a Project and Professionalism report and a marketing page."
    )


def extra_ch7(b):
    b.h("7.1a Contribution restated for assessment", 2)
    b.p(
        "For assessment purposes the contribution can be restated in one paragraph. The "
        "software artefact SerenityPath demonstrates a patient-directed hybrid mental-health "
        "web platform whose two pathways are implemented, not merely described. The AI pathway "
        "is a session-based companion with provider fallback and deterministic crisis "
        "interception. The human pathway is verified-doctor booking with availability "
        "templates, lunch breaks, status lifecycle, and video-room metadata. Cross-cutting "
        "features — English/Myanmar localisation, usage reports, educational resources, and "
        "referrals — make the product look like a platform rather than two disconnected "
        "demos. The academic contribution is the evaluated argument that this choice structure "
        "addresses accessibility and engagement barriers identified in the literature, within "
        "the limits of a student prototype."
    )
    b.p(
        "Aims 1–4 in Table 2 are therefore not a ritual checklist. Aim 1 is the platform. Aim 2 "
        "is the dashboard choice. Aim 3 is the governed LLM. Aim 4 is Chapters 5 and 6. If a "
        "marker only has time to inspect one vertical slice, the recommended slice is: seed "
        "login as patient, send a crisis phrase, inspect the admin queue, then book dr.smith "
        "from an available slot. That slice touches professionalism, the academic question, "
        "and the README in a single demonstration."
    )

    b.h("7.3a Implications for similar student projects", 2)
    b.p(
        "A practical implication for other dual-pathway health projects is to decide the trust "
        "boundaries before choosing a JavaScript animation library. Another is to seed an "
        "unverified doctor and an inactive patient on day one, because those rows test rules "
        "that happy-path screenshots never show. A third is to write the academic question so "
        "that a prototype can actually answer it: access and perceived satisfaction are "
        "answerable; “does AI therapy work?” is not, at this scale. Those implications are "
        "what Chapter 7 should leave behind besides a summary of files and frameworks."
    )
    b.p(
        "The directions in section 7.4 are ordered by professionalism rather than by visual "
        "impressiveness. In-app video would make the telepsychiatry construct stronger, but "
        "Playwright tests around crisis posting would make the existing construct safer to "
        "change. A clinic partnership would make the survey stronger, but only after ethics "
        "review. Classifier-assisted triage would reduce phrase-list misses, but only with a "
        "human still in the admin queue. The project ends by refusing to swap those priorities "
        "for a more glamorous backlog."
    )
