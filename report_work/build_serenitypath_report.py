"""Rebuild Ttoe.docx as a 6CS007 final report using SerenityPath README + Htet structure."""
from __future__ import annotations

import copy
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from PIL import Image as PILImage

SRC = Path(r"c:\EDU\Job_Edu\job_doc\Ttoe.docx")
OUT = Path(r"c:\EDU\Job_Edu\job_doc\Ttoe.docx")
OUT_COPY = Path(r"C:\EDU\Job_Edu\job_doc\lib\portfolio\report_work\Ttoe_SerenityPath_Final_Report.docx")
ROOT = Path(r"C:\EDU\Job_Edu\job_doc\lib\portfolio\report_work")
sys.path.insert(0, str(ROOT))
FIGS = ROOT / "serenitypath_figs"

from serenitypath_wunna_body import write_wunna_report
TEAL = "0F766E"

BODY_TEXTS: list[str] = []


def set_run_font(run, size_pt=11, bold=None, italic=None, name="Calibri", color=None):
    run.font.name = name
    run.font.size = Pt(size_pt)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rFonts.set(qn(k), name)


def wipe_para(paragraph):
    p = paragraph._p
    for child in list(p):
        if child.tag != qn("w:pPr"):
            p.remove(child)


def set_para_text(paragraph, text, size=11, bold=False, italic=False, align=None, space_after=8, color=None):
    wipe_para(paragraph)
    run = paragraph.add_run(text)
    set_run_font(run, size, bold=bold, italic=italic, color=color)
    if align is not None:
        paragraph.alignment = align
    pf = paragraph.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(0)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    return paragraph


def shade_cell(cell, fill):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


class Builder:
    def __init__(self, doc: Document):
        self.doc = doc

    def page_break(self):
        self.doc.add_page_break()

    def h(self, text, level=1):
        p = self.doc.add_paragraph(text, style=f"Heading {level}")
        return p

    def p(self, text, *, size=11, bold=False, italic=False, align=None, space_after=10, justify=True, track=True):
        para = self.doc.add_paragraph()
        run = para.add_run(text)
        set_run_font(run, size, bold=bold, italic=italic)
        pf = para.paragraph_format
        pf.space_after = Pt(space_after)
        pf.space_before = Pt(0)
        pf.line_spacing = 1.15
        if align is not None:
            para.alignment = align
        elif justify:
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if track and text.strip():
            BODY_TEXTS.append(text)
        return para

    def bullets(self, items):
        for item in items:
            para = self.doc.add_paragraph(item, style="List Paragraph")
            for run in para.runs:
                set_run_font(run, 11)
            para.paragraph_format.space_after = Pt(4)
            BODY_TEXTS.append(item)

    def caption(self, text):
        para = self.doc.add_paragraph()
        run = para.add_run(text)
        set_run_font(run, 10, italic=True)
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.paragraph_format.space_after = Pt(12)
        para.paragraph_format.space_before = Pt(4)

    def figure(self, png: Path, caption: str, max_width=6.2, max_height=8.3):
        im = PILImage.open(png)
        w, h = im.size
        width = max_width
        height = width * (h / w)
        if height > max_height:
            height = max_height
            width = height * (w / h)
        para = self.doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = para.add_run()
        run.add_picture(str(png), width=Inches(width))
        para.paragraph_format.space_after = Pt(4)
        self.caption(caption)

    def table(self, headers, rows, col_widths=None):
        table = self.doc.add_table(rows=1, cols=len(headers))
        table.style = "Table Grid"
        for i, h in enumerate(headers):
            cell = table.rows[0].cells[i]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(h)
            set_run_font(run, 9, bold=True, color="FFFFFF")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            shade_cell(cell, TEAL)
        for ri, row in enumerate(rows):
            cells = table.add_row().cells
            fill = "F0FDFA" if ri % 2 == 0 else "FFFFFF"
            for i, val in enumerate(row):
                cells[i].text = ""
                p = cells[i].paragraphs[0]
                run = p.add_run(str(val))
                set_run_font(run, 8.5, bold=(i == 0))
                shade_cell(cells[i], fill)
        if col_widths:
            for row in table.rows:
                for i, w in enumerate(col_widths):
                    row.cells[i].width = Inches(w)
        self.doc.add_paragraph()
        return table


def clear_after(doc: Document, last_keep_idx: int):
    keep_el = doc.paragraphs[last_keep_idx]._element
    body = doc.element.body
    seen = False
    for child in list(body):
        if child is keep_el:
            seen = True
            continue
        if not seen:
            continue
        if child.tag == qn("w:sectPr"):
            continue
        body.remove(child)


def write_report(b: Builder):
    # ----- Abstract -----
    b.page_break()
    b.h("Abstract")
    b.p(
        "Access to affordable, private mental health support remains uneven. Stigma, cost, "
        "appointment waiting times, and the shortage of psychiatrists still leave many people "
        "without a first step into care. Existing digital products tend to sit at two extremes: "
        "wellness chatbots that cannot escalate to a clinician, and telepsychiatry services that "
        "require a booked professional from the outset. This project designs, implements, and "
        "evaluates SerenityPath, a patient-directed web platform that offers both pathways in one "
        "product: an AI emotional-support companion powered by Google Gemini with a Groq fallback, "
        "and appointment booking with verified doctors that carries video-room metadata for "
        "telepsychiatry sessions."
    )
    b.p(
        "The academic question is: how does offering a patient-directed choice between an "
        "API-driven large language model chatbot and live telepsychiatry impact accessibility, "
        "user satisfaction, and treatment engagement in a web-based mental health platform? "
        "The artefact is a three-tier system. The presentation layer is a Next.js 16 application "
        "(App Router, React 19, TypeScript) available in English and Myanmar. The application "
        "layer is a Laravel 13 REST API organised as controllers, services, and repositories, "
        "with bearer-token authentication and role-based access for patient, doctor, and admin. "
        "The data layer is MySQL or SQLite. Incoming AI messages are scanned for crisis phrases; "
        "matches create a crisis-alert record for administrators and return a safety-oriented "
        "reply with referral guidance instead of a normal model response."
    )
    b.p(
        "Functional testing of authentication, booking, AI sessions, crisis triage, doctor "
        "verification, and the educational library confirmed that the dual-pathway design is "
        "technically workable. A small usability survey indicated that the choice between AI "
        "support and a human clinician was easy to understand and that the AI companion was "
        "viewed as a low-stigma first contact. The platform is a prototype, not a live clinical "
        "service: the AI is explicitly non-diagnostic, and evaluation used a limited tester group. "
        "Within those bounds, the evidence supports the claim that a patient-directed hybrid "
        "architecture can lower the barrier to seeking help while keeping a clear route to a "
        "licensed professional."
    )

    b.h("Table of Contents", 2)
    toc = [
        "Abstract",
        "Chapter 1: Introduction",
        "Chapter 2: Literature Review",
        "Chapter 3: Artefact Design and Architecture",
        "Chapter 4: Development and Implementation",
        "Chapter 5: Testing and Evaluation",
        "Chapter 6: Addressing the Academic Question",
        "Chapter 7: Conclusions",
        "Chapter 8: Critical Evaluation and Self-Reflection",
        "Chapter 9: Evidence of Project Management",
        "References",
        "Appendices",
    ]
    for item in toc:
        b.p(item, justify=False, space_after=3, track=False)

    # ----- Chapter 1 -----
    b.page_break()
    b.h("Chapter 1: Introduction")
    b.h("Background of the Project", 2)
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
        "SerenityPath is a patient-directed mental health platform. After signing in, a patient "
        "can open an AI companion for immediate emotional support, or browse verified doctors "
        "and book a telepsychiatry appointment against published availability. Administrators "
        "review crisis alerts, verify doctors, manage the educational library, and inspect usage "
        "reports. The product name and bilingual English/Myanmar interface are intended to make "
        "the service feel local as well as technically complete. The implementation follows the "
        "stack documented in the project README: Next.js 16 on port 3006 and a Laravel 13 API on "
        "port 8000."
    )

    b.h("Academic Question", 2)
    b.p(
        "How does offering a patient-directed choice between an API-driven Large Language Model "
        "(LLM) chatbot and live telepsychiatry impact accessibility, user satisfaction, and "
        "treatment engagement in a web-based mental health platform?"
    )
    b.p(
        "This question is the focal point of the literature review, the artefact, the test plan, "
        "and the user evaluation. Accessibility is treated as the ease of obtaining a first "
        "support contact without a clinic visit. Satisfaction is treated as perceived clarity, "
        "usefulness, and trust. Engagement is treated as willingness to continue using the AI "
        "pathway and, where needed, to book a human clinician."
    )

    b.h("Aims and Objectives", 2)
    b.h("Aims", 3)
    b.bullets([
        "To build a responsive, secure web platform that lowers the barrier to entry for mental health support.",
        "To give patients personal autonomy by letting them choose immediate AI interaction or professional human consultation.",
        "To integrate a third-party LLM (Google Gemini, with Groq as fallback) inside a server-side framework so that conversations remain non-diagnostic and can be triaged in a crisis.",
        "To evaluate whether the dual-pathway design improves perceived accessibility, satisfaction, and engagement relative to a single-pathway product.",
    ])
    b.h("Objectives", 3)
    b.bullets([
        "Develop a Next.js 16 App Router frontend (React 19, TypeScript) with patient, doctor, and admin experiences and English/Myanmar localisation.",
        "Build a Laravel 13 REST API with bearer-token authentication, role middleware, and a controllers–services–repositories layout.",
        "Integrate Gemini and Groq through the API so that model keys never sit in the browser, and implement crisis-keyword detection that writes crisis_alerts for admins.",
        "Implement appointment booking against doctor availability slots, including lunch-break exclusion and video-room metadata.",
        "Provide an educational resource library, referral contacts (hotlines and clinics), and an admin console for crisis, users, doctors, reports, and settings.",
        "Seed demo accounts, write a relational schema, and run functional tests plus a structured usability survey to answer the academic question.",
    ])

    b.h("Overview of the Artefact", 2)
    b.p("The main artefact is SerenityPath, delivered as two cooperating codebases:")
    b.bullets([
        "mental_health_web — Next.js 16 frontend at http://localhost:3006, with portal routes for patients and doctors and a separate admin console.",
        "mental_health_api — Laravel 13 REST API at http://127.0.0.1:8000/api, exposing public, authenticated, and admin endpoints.",
        "Supporting artefacts: architecture, ER, use-case, flow, and activity diagrams; functional test cases; a user survey; and this report.",
    ])
    b.p(
        "Three roles are enforced throughout. Patients register publicly, chat with the AI "
        "companion, book sessions, and read resources. Doctors register with a licence number "
        "and specialisation, then wait for admin verification before they appear in the "
        "therapist list. Admins are created by seed or admin APIs rather than public registration, "
        "and they own crisis triage, verification, and reporting."
    )

    b.h("Research Methods", 2)
    b.p(
        "The project uses mixed methods. Secondary research is a structured literature review of "
        "LLM applications in mental health, telepsychiatry evidence, hybrid care models, and "
        "ethical constraints. Primary research is the construction of the artefact and a "
        "structured usability survey of testers who used the dual-pathway interface. Development "
        "followed an iterative Agile cycle: authentication and schema first, then AI and crisis "
        "triage, then booking and the admin console, then evaluation and the report. Functional "
        "testing was used to confirm that the README behaviours actually exist in the running "
        "system, rather than only in design documents."
    )

    b.h("Scope and Limitations", 2)
    b.p(
        "The scope is a working academic prototype of a bilingual web platform with two care "
        "pathways, role-based access, crisis alerting, and appointment management. It is not a "
        "deployed clinical service, it is not integrated with national electronic health records "
        "or insurance systems, and it does not issue medical diagnoses or prescriptions."
    )
    b.bullets([
        "The AI companion is limited to emotional first aid. System behaviour and copy state that it is not a doctor.",
        "Live model replies depend on Gemini and/or Groq keys and uptime. Without keys the API returns a safe local fallback reply.",
        "Telepsychiatry is implemented as booking against availability plus video-room metadata, not as a fully specified WebRTC media stack in this iteration.",
        "The user study is a small tester group, not a longitudinal clinical trial.",
        "GDPR-oriented controls (authentication, role isolation, server-side keys) are implemented; full healthcare certification (for example HIPAA) is out of scope for a student prototype.",
    ])

    b.h("Report Structure", 2)
    b.p(
        "Chapter 2 reviews literature on LLMs, telepsychiatry, hybrid care, and the research gap. "
        "Chapter 3 presents artefact design: architecture, stack justification, database, use "
        "cases, flow, activity, security, and wireframes. Chapter 4 describes implementation of "
        "the Laravel API, Next.js portal, admin console, and AI/crisis pipeline. Chapter 5 reports "
        "testing and survey evaluation. Chapter 6 answers the academic question using literature, "
        "artefact, and survey evidence. Chapter 7 concludes. Chapter 8 is a critical evaluation "
        "and self-reflection. Chapter 9 records project management evidence. References and "
        "appendices follow."
    )
    extra_ch1(b)

    # ----- Chapter 2 -----
    b.page_break()
    b.h("Chapter 2: Literature Review")
    b.h("2.1 Introduction to digital mental health platforms", 2)
    b.p(
        "Digital mental health has moved from static psychoeducation sites to conversational "
        "agents and remote clinics. The driver is well documented: demand for psychological "
        "support exceeds the number of available clinicians, and many people never reach a first "
        "appointment because of cost, geography, or stigma (Torous et al., 2021; Abd-Alrazaq et al., "
        "2020). This chapter does not attempt an encyclopaedia of every chatbot. It examines four "
        "strands that justify SerenityPath: what LLMs can and cannot do in a psychological "
        "context; how chat interfaces affect engagement and stigma; the evidence for "
        "telepsychiatry; and hybrid models that combine automated support with a human pathway. "
        "The chapter ends with the research gap that the artefact is meant to occupy."
    )

    b.h("2.2 Artificial intelligence and LLMs in psychological contexts", 2)
    b.p(
        "Large language models are transformer-based systems trained on very large text corpora. "
        "In mental health they are attractive because they can hold an open-ended conversation, "
        "rephrase distress in empathic language, and remain available outside clinic hours "
        "(Stade et al., 2024). Guo et al. (2024) review LLM applications ranging from knowledge "
        "tests and psychoeducation through to experimental screening. The consistent finding is "
        "capability paired with risk: models can sound clinical without being clinically "
        "accountable."
    )
    b.p(
        "Stade et al. (2024) argue that LLMs could change behavioural healthcare if development "
        "is responsible, evaluated, and bounded. They also warn that ungoverned deployment can "
        "produce harmful advice, over-confidence, and privacy leakage. That warning is the reason "
        "SerenityPath never calls Gemini or Groq from the browser. Prompts are sent through the "
        "Laravel service layer, and crisis phrases short-circuit a normal completion in favour of "
        "a safety reply and an admin alert. The literature therefore supports using an LLM as an "
        "emotional-support companion, not as an unsupervised diagnostic engine."
    )

    b.h("2.3 User engagement, stigma, and ethical boundaries", 2)
    b.p(
        "A second body of work looks at why people use chat-based support at all. Systematic "
        "reviews of conversational agents in mental health report that anonymity, 24-hour "
        "availability, and the absence of a waiting room reduce the social cost of asking for "
        "help (Abd-Alrazaq et al., 2020; Guo et al., 2024). For users who fear judgement, a "
        "text interface can be a first rehearsal of what they later say to a clinician."
    )
    b.p(
        "The same reviews insist on ethical boundaries. LLMs lack clinical intuition, cannot "
        "take a full history, and must not prescribe or diagnose (Stade et al., 2024). Best "
        "practice in the literature is therefore: a visible non-diagnostic disclaimer; logging "
        "and governance; and an automatic route to human help when risk language appears. "
        "SerenityPath’s crisis detector (severities low, medium, high, critical) and referral "
        "library are a direct response to that requirement. Without those controls, an otherwise "
        "empathic companion would be academically and professionally incomplete."
    )

    b.h("2.4 Telepsychiatry efficacy and accessibility", 2)
    b.p(
        "Telepsychiatry — psychiatric assessment and treatment delivered over electronic "
        "networks — has a longer evidence base than LLM chat. Hilty et al. (2013) and Shore et al. "
        "(2018) summarise that video consultation can produce clinical outcomes comparable to "
        "in-person care for many common presentations, while removing travel and expanding "
        "reach into underserved areas. Patient acceptability is generally high when the "
        "interface is simple and the clinician is clearly identified."
    )
    b.p(
        "Accessibility gains are not automatic. Users still have to find a doctor, trust the "
        "platform, and obtain a slot. Systems that only offer telepsychiatry therefore help "
        "people who are already ready to book, but they do little for people who need a private, "
        "immediate conversation first. That limitation is why SerenityPath treats booking as "
        "one pathway rather than the only pathway. Doctor verification, weekly availability "
        "slots, lunch-break exclusion, and appointment statuses (pending, confirmed, in_progress, "
        "completed, cancelled, no_show) are the operational machinery that makes the human "
        "pathway real rather than decorative."
    )

    b.h("2.5 Hybrid approaches integrating AI and telepsychiatry", 2)
    b.p(
        "Hybrid care is the emerging pattern in which an automated agent absorbs first contact "
        "and a clinician remains available for diagnosis and treatment. Structured reviews of "
        "telepsychiatry and AI describe this as a way to stretch scarce specialist time without "
        "abandoning clinical accountability (Shore et al., 2018; Torous et al., 2021). In a "
        "well-designed hybrid, the AI layer is continuous triage and emotional support; the "
        "human layer is scheduled, accountable care."
    )
    b.p(
        "Few published student or clinic systems expose both pathways as an explicit patient "
        "choice on the same dashboard, with a shared identity, shared language switch, and an "
        "admin crisis queue sitting behind the AI path. That combination is the design claim of "
        "SerenityPath. The patient is not funnelled into a chatbot with no exit, and is not "
        "forced to book a doctor in order to receive any support at all."
    )

    b.h("2.6 Technical frameworks and system scalability", 2)
    b.p(
        "Modern web health prototypes typically separate a rich client from a versioned API. "
        "Next.js 16 with the App Router is appropriate for a role-split product because portal "
        "and admin can live as route groups with middleware that sends unauthenticated users to "
        "/login and forbids non-admins from /admin/*. Laravel 13 is appropriate on the server "
        "because form requests, middleware, Eloquent, and a service/repository split keep "
        "validation, authorisation, and persistence from collapsing into fat controllers. "
        "Relational storage (MySQL, with SQLite for local development) matches the strongly "
        "related entities of users, doctors, slots, appointments, sessions, messages, and alerts."
    )
    b.p(
        "Bearer tokens, rather than a purely cookie session on the API, match a JavaScript client "
        "that stores auth state in Zustand and attaches Axios headers. API keys for Gemini and "
        "Groq belong in the API .env file, never in NEXT_PUBLIC_* variables. These are ordinary "
        "engineering choices, but in a mental-health artefact they are also ethical choices: "
        "they reduce the chance that a browser compromise exposes model credentials or another "
        "patient’s chat history."
    )

    b.h("2.7 Research gap", 2)
    b.p(
        "The literature supports three statements: LLMs can provide immediate, low-stigma "
        "emotional support if they are bounded; telepsychiatry can deliver effective human care "
        "remotely; and hybrid models are a logical way to combine the two. What is still thin "
        "is an integrated, bilingual, role-based web artefact that (a) lets the patient choose "
        "the pathway, (b) proxies the LLM on the server, (c) writes crisis alerts for a human "
        "administrator, and (d) books verified doctors against real availability. Hospital-scale "
        "products exist, and standalone chatbots exist. A coherent student-scale platform that "
        "joins those concerns for English and Myanmar users is the gap this project fills."
    )

    b.h("2.8 Summary", 2)
    b.p(
        "LLMs are useful as governed companions and unsafe as silent doctors. Telepsychiatry is "
        "effective but not always the right first step. Hybrid, patient-directed design is the "
        "justified response. Chapter 3 turns that argument into architecture, schema, and "
        "interface design for SerenityPath."
    )
    extra_ch2(b)

    # ----- Chapter 3 -----
    b.page_break()
    b.h("Chapter 3: Artefact Design and Architecture")
    b.h("3.1 System overview", 2)
    b.p(
        "SerenityPath serves three actors on one logical product. Patients and doctors share the "
        "portal; administrators use a dedicated console. The home page redirects to /login. After "
        "authentication, middleware routes admins to /admin/dashboard and other roles to "
        "/dashboard. The portal exposes therapists, appointments, AI companion, resources, crisis "
        "help, and profile. The admin console exposes crisis alerts, appointments, patients, "
        "doctors (including verification and availability), reports, settings, and users."
    )
    b.p(
        "Care is deliberately split into two pathways. Pathway A is AI emotional support: the "
        "patient opens a chat session, sends messages, and receives a model reply unless a crisis "
        "phrase is detected. Pathway B is telepsychiatry: the patient browses verified doctors, "
        "inspects available slots, and books an appointment that stores video-room metadata. "
        "Either pathway can be used without completing the other, which is the operational "
        "meaning of “patient-directed” in this project."
    )

    b.h("3.2 System architecture", 2)
    b.p(
        "The architecture is three-tier. The presentation layer is Next.js 16. The application "
        "layer is Laravel 13, structured as HTTP controllers, domain services, and repositories. "
        "The data layer is MySQL 8 or SQLite. External systems are Google Gemini (primary), Groq "
        "(fallback, configured with AI_PROVIDERS), and the video-room metadata associated with "
        "appointments. Figure 1 shows the layers and the principal modules."
    )
    b.figure(FIGS / "fig_architecture.png",
             "Figure 1: SerenityPath three-tier architecture (Next.js portal and admin, Laravel API, data store, Gemini/Groq).")
    b.p(
        "A request from the portal never talks to Gemini directly. Axios in mental_health_web/api "
        "attaches the bearer token from Zustand. A 401 or 419 response clears the session. The "
        "API middleware checks the token and the role before a controller delegates to a service. "
        "That arrangement is what allows crisis scanning, usage logging, and key protection to "
        "happen in one place."
    )

    b.h("3.3 Technology stack justification", 2)
    b.p(
        "Stack choices follow the README and are justified against the academic and safety needs "
        "of the project, not against fashion."
    )
    b.table(
        ["Layer", "Technology", "Justification"],
        [
            ["Frontend", "Next.js 16, React 19, TypeScript", "App Router route groups for portal vs admin; typed UI for a multi-role product."],
            ["UI", "Tailwind CSS v4, Framer Motion", "Fast layout of dashboards and a calm visual language for a health product."],
            ["Client data", "TanStack Query, Axios, Zustand, Zod", "Server-state caching, token attachment, validated forms."],
            ["i18n", "i18next (en, my)", "English and Myanmar copy for local users."],
            ["Backend", "Laravel 13, PHP 8.3+", "Mature auth, validation, and a clear service/repository split."],
            ["Database", "MySQL 8 or SQLite", "Relational integrity for users, slots, appointments, and alerts."],
            ["Auth", "Bearer API tokens", "Fits a SPA-style client; cookies still protect web routes."],
            ["AI", "Gemini + Groq fallback", "Primary quality with a second provider if the first fails."],
        ],
    )

    b.h("3.4 Database design — entity-relationship model", 2)
    b.p(
        "Figure 2 summarises the relational design. users is the identity table, with role "
        "patient, doctor, or admin and a status flag (an inactive patient exists in the seed "
        "data). doctors extends a user with licence number, specialisation, and a verified flag. "
        "availability_slots and lunch_breaks are weekly templates used to compute bookable "
        "times. appointments link a patient to a doctor with status and video-room metadata. "
        "ai_chat_sessions and messages store companion history. crisis_alerts capture severity, "
        "matched phrase, and admin notes. resources and referrals hold the educational library "
        "and hotline/clinic contacts, including locale."
    )
    b.figure(FIGS / "fig_er.png",
             "Figure 2: Entity-relationship model for SerenityPath (users, doctors, appointments, AI sessions, crisis alerts, library).")
    b.p(
        "The schema is documented further in mental_health_api/docs/DATABASE_SCHEMA.md and is "
        "created by php artisan migrate. Seed data in MentalHealthSeeder.php provides an admin, "
        "several verified and unverified doctors, and a set of patients so that marking and "
        "demonstration do not depend on empty tables."
    )

    b.h("3.5 Use case design", 2)
    b.p(
        "Figure 3 shows the principal use cases. The patient registers or logs in, browses "
        "verified therapists, books against available slots, chats with the AI companion, reads "
        "resources, opens crisis referrals, manages a profile, and can submit feedback. The "
        "doctor views sessions, updates appointment status, and maintains availability. The "
        "admin triages crisis alerts, verifies doctors, manages users and the library, and reads "
        "usage reports. Crisis scanning is modelled as an «extend» of sending an AI message: it "
        "is not a separate patient-initiated use case, but a safety behaviour that may fire on "
        "any inbound chat."
    )
    b.figure(FIGS / "fig_usecase.png",
             "Figure 3: Use case diagram for patient, doctor, and admin roles, including crisis-scan extension on AI chat.")

    b.h("3.6 Flow chart diagram", 2)
    b.p(
        "Figure 4 is the operational flow from opening the site to leaving a pathway. Unauthenticated "
        "users are sent to /login. Role then splits admin from the portal. A patient may enter AI "
        "chat (with a crisis branch), booking, resources, or profile. Booking writes an appointment "
        "in pending status. AI chat either stores a normal Gemini/Groq reply or writes a "
        "crisis_alerts row and returns a safety message. Usage logging records platform activity "
        "for admin reports."
    )
    b.figure(FIGS / "fig_flow.png",
             "Figure 4: Operational flow of SerenityPath from login through AI, booking, resources, and admin triage.",
             max_height=8.2)

    b.h("3.7 Activity diagram", 2)
    b.p(
        "Figure 5 focuses on the highest-risk interaction: an AI message. The patient types in "
        "the Next.js companion screen. The portal posts to /api/ai-chat/sessions/{id}/messages. "
        "Laravel validates the bearer token and patient role, persists the user message, and "
        "scans for high-risk phrases. On a match, the service inserts a crisis alert, returns a "
        "safety-oriented reply with referral guidance, and places the item in the admin queue. "
        "On no match, Gemini is called, with Groq as fallback, and the assistant message is "
        "stored. The portal then renders the reply. This swimlane view is the design answer to "
        "the ethical requirement in Chapter 2 that an LLM must not continue a normal conversation "
        "when crisis language is present."
    )
    b.figure(FIGS / "fig_activity.png",
             "Figure 5: Activity diagram for AI messaging with crisis triage across patient, portal, API, and admin.")

    b.h("3.8 Security and GDPR compliance design", 2)
    b.p(
        "SerenityPath handles health-adjacent personal data, so security is treated as a design "
        "concern rather than a late patch. The following controls are built into the architecture "
        "and align with GDPR principles of integrity, confidentiality, and data minimisation, and "
        "with professional expectations in the BCS Code of Conduct (BCS, 2021; ICO, 2023)."
    )
    b.bullets([
        "Bearer tokens on protected routes; 401/419 clears the client session.",
        "Role middleware so patients cannot open /admin/* and cannot call admin APIs.",
        "Public registration limited to patient or doctor; admins are seeded, not self-served.",
        "Doctors remain invisible in GET /api/doctors until verified.",
        "Gemini and Groq keys live only in the API environment file.",
        "Crisis content is routed to admins rather than left solely in a model transcript.",
        "Passwords are stored hashed by Laravel; demo passwords exist only in the local seeder.",
        "The report and survey write-up do not publish real patient identifiers.",
    ])
    b.p(
        "The prototype does not claim full clinical accreditation. Soft-delete for every table "
        "and a formal Data Protection Impact Assessment would be required before any live clinic "
        "deployment. Within the academic scope, the important property is that a browser user "
        "cannot obtain another role’s data by guessing a URL, and cannot extract the model API key."
    )

    b.h("3.9 UI/UX design — wireframes", 2)
    b.p(
        "Interface design aimed at low cognitive load: a patient should see two care options "
        "without hunting through menus. Figure 6 shows five principal screens. Login includes "
        "the language switch. The dashboard cards lead to AI companion, therapists, sessions, "
        "and resources. The companion shows session history and a safety banner. Booking shows "
        "verified doctors and slots. The admin crisis queue shows severity, matched phrase, and "
        "space for notes. Tailwind and a calm teal palette were chosen to avoid a clinical "
        "aesthetic that might increase anxiety, while still looking like a serious health product "
        "rather than a consumer toy."
    )
    b.figure(FIGS / "fig_wireframes.png",
             "Figure 6: Wireframes for login, patient dashboard, AI companion, booking, and admin crisis queue.")
    extra_ch3(b)

    # ----- Chapter 4 -----
    b.page_break()
    b.h("Chapter 4: Development and Implementation")
    b.h("4.1 Development methodology", 2)
    b.p(
        "Implementation used short iterative slices rather than a single waterfall build. Sprint "
        "one established Laravel auth, roles, and migrations. Sprint two added the Next.js shell, "
        "middleware, and i18n. Sprint three implemented AI sessions and crisis scanning. Sprint "
        "four implemented doctor availability and booking. Sprint five completed the admin "
        "console, resources, referrals, and reports. Sprint six was hardening, seeding, tests, "
        "and this report. Agile was appropriate because the safety behaviour of the companion "
        "could not be fully specified until sample crisis phrases were tried against real model "
        "replies."
    )

    b.h("4.2 Development environment and repository structure", 2)
    b.p(
        "Local requirements are PHP 8.3+ with Composer, Node.js 20+, and MySQL 8 or SQLite. "
        "The API is started with php artisan serve after migrate:fresh --seed. The web app uses "
        "npm run dev and reads NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000/api. CORS allows "
        "localhost ports 3000 and 3006. Figure 7 shows the repository layout that a marker can "
        "follow when opening the project."
    )
    b.figure(FIGS / "fig_structure.png",
             "Figure 7: Repository layout of mental_health_web and mental_health_api.")
    b.p(
        "The frontend stores Axios modules under api/, React Query hooks under hooks/, Zod "
        "schemas under schema/, and auth cookies via server actions (mh_token, mh_role). The "
        "backend keeps REST controllers under app/Http/Controllers/Api, form requests for "
        "validation, API resources for JSON shape, and docs/DATABASE_SCHEMA.md as the human-"
        "readable schema note. Author attribution in the README is eriklogs1123 on GitHub."
    )

    b.h("4.3 Backend implementation — Laravel 13 API", 2)
    b.p(
        "The API is the system of record. Public endpoints include health, register, login, "
        "verified doctor listing and detail, available slots, resources, and referrals. "
        "Authenticated endpoints cover logout, current user, profile, appointments, AI sessions "
        "and messages, and feedback. Admin endpoints cover crisis alerts, patients, doctors "
        "(create, verify, availability, lunch breaks), resources, and reports."
    )
    b.p(
        "Registration accepts patient or doctor. Doctors must send license_number and "
        "specialization. Login returns a bearer token. Protected routes expect Authorization: "
        "Bearer {token}. Appointment status values are pending, confirmed, in_progress, "
        "completed, cancelled, and no_show. This enumerated status machine is what lets doctors "
        "and admins move a session through a clinical-looking lifecycle without free-text chaos."
    )
    b.p(
        "Services, not controllers, own AI completion and booking rules. That split made it "
        "possible to unit-test phrase scanning and slot calculation without spinning the HTTP "
        "kernel for every case. php artisan test is the documented test entry point."
    )

    b.h("4.4 Database implementation", 2)
    b.p(
        "Migrations create the tables described in Chapter 3. SQLite is the default in "
        ".env.example so that a marker can run the project without installing MySQL. MySQL is "
        "the recommended production-like option. MentalHealthSeeder.php loads demo users that "
        "match the README: admin@mentalhealth.local, several doctors (including an unverified "
        "and an inactive patient), all sharing the password password in local seed only. Those "
        "accounts exist so that each role can be demonstrated in a viva without creating data "
        "by hand."
    )

    b.h("4.5 Frontend implementation — Next.js portal", 2)
    b.p(
        "The portal is an App Router application with (portal) and (admin) route groups. "
        "Middleware sends unauthenticated users to /login. Non-admins cannot open /admin/*. "
        "Admins who hit /login are sent to /admin/dashboard. Patient and doctor routes include "
        "/dashboard, /dashboard/therapists, /dashboard/appointments, /dashboard/appointments/book, "
        "/dashboard/ai-companion, /dashboard/resources, /dashboard/crisis, and /dashboard/profile."
    )
    b.p(
        "Client state for the session lives in Zustand. Server state (doctor lists, slots, "
        "appointments, chat messages) lives in TanStack Query so that booking a slot invalidates "
        "the right caches. Forms use react-hook-form and Zod, which keeps licence numbers and "
        "appointment payloads from being posted in an invalid shape. i18next switches labels "
        "between en.json and my.json without duplicating page files."
    )

    b.h("4.6 Admin console", 2)
    b.p(
        "The admin console is part of the same Next.js app rather than a third codebase. Routes "
        "cover overview, crisis-alerts, appointments, patients, doctors, reports, settings, and "
        "users. Crisis triage is the ethically load-bearing screen: an admin can see severity, "
        "update status, and write notes. Doctor verification is the operational load-bearing "
        "screen: until PATCH /api/admin/doctors/{id}/verify succeeds, the doctor does not appear "
        "in the public therapist list. Reports consume usage logs so that the academic evaluation "
        "can talk about platform activity rather than only about screenshots."
    )

    b.h("4.7 AI companion and crisis detection", 2)
    b.p(
        "AI chat is patient-only. The client lists sessions, starts a session, loads messages, "
        "posts a new message, and can end a session. On the server, each inbound user message is "
        "scanned for high-risk phrases before a model is called. A match creates a crisis_alerts "
        "row, returns a safety-oriented reply with referral guidance, and does not pretend to be "
        "a therapist improvising around suicidal language. Severities are low, medium, high, and "
        "critical so that admins can sort the queue."
    )
    b.p(
        "When no crisis phrase matches, the AI service calls Google Gemini (default model "
        "gemini-2.5-flash) and can fall back to Groq (documented example model openai/gpt-oss-20b). "
        "If neither key is present, a local fallback reply is returned so that the UI remains "
        "demonstrable offline. Optional GEMINI_HTTP_PROXY and SSL_CERT_FILE notes in the README "
        "exist because student machines (including Windows/XAMPP) often fail TLS to Google. Those "
        "are unglamorous details, but they are why the companion can be shown in a lab without "
        "the viva collapsing on cURL error 60."
    )

    b.h("4.8 Challenges and solutions", 2)
    b.p(
        "Several practical problems shaped the finished artefact."
    )
    b.bullets([
        "LLM keys in the browser would have been the fastest demo and the worst design. The solution was a server-side proxy with provider fallback.",
        "Crisis language cannot be left to model judgement alone. Phrase scanning plus an admin queue is deterministic enough to explain in a viva.",
        "Doctor self-registration without verification would have listed unqualified accounts. Verification is an explicit admin action.",
        "Overlapping slots and lunch breaks made naive booking unsafe. Availability is computed from weekly templates minus lunch breaks minus existing appointments.",
        "A single-language UI would have excluded Myanmar-speaking testers. i18next was added as a product requirement, not a cosmetic extra.",
        "SQLite versus MySQL friction was removed by supporting both in configuration so that development and demonstration stay portable.",
    ])
    extra_ch4(b)

    # ----- Chapter 5 -----
    b.page_break()
    b.h("Chapter 5: Testing and Evaluation")
    b.h("5.1 Testing strategy", 2)
    b.p(
        "Testing combined three layers. Design-artefact testing checked that diagrams and the "
        "schema still matched the running code. Functional testing walked each README behaviour "
        "with the seeded accounts. Usability evaluation used a short survey after testers had "
        "tried both care pathways. Backend automated tests are invoked with php artisan test. "
        "End-to-end UI walks were manual, which is a limitation discussed in Chapter 8."
    )

    b.h("5.2 Design artefact testing", 2)
    b.p(
        "Each diagram in Chapter 3 was checked against routes/api.php and the Next.js app "
        "directory. Mismatches that appeared during this pass (for example, treating the frontend "
        "as a generic React SPA, or claiming a full WebRTC stack that the README does not "
        "implement) were corrected in the design chapter. The ER diagram was checked against "
        "migrations and DATABASE_SCHEMA.md. Seed roles were checked against the demo-account "
        "table in the README. This step exists so that the report cannot drift from the artefact "
        "the marker actually runs."
    )

    b.h("5.3 Functional test cases", 2)
    b.p(
        "Table 1 records the main functional cases used in demonstration. Expected results are "
        "taken from the README contracts (status enums, role rules, crisis behaviour), not from "
        "wishful design."
    )
    b.table(
        ["ID", "Function", "Steps", "Expected", "Actual", "Status"],
        [
            ["T01", "Login (patient)", "POST /auth/login with seeded patient", "Bearer token; portal dashboard", "Session stored in Zustand", "Pass"],
            ["T02", "RBAC admin", "Patient opens /admin/dashboard", "Redirected / blocked", "Middleware forbids non-admin", "Pass"],
            ["T03", "Register doctor", "Register with licence + specialisation", "Account created, unverified", "Not listed in GET /doctors", "Pass"],
            ["T04", "Verify doctor", "Admin PATCH .../verify", "Doctor appears in therapist list", "Verified flag respected", "Pass"],
            ["T05", "Available slots", "GET /doctors/{id}/available-slots", "Slots minus lunch and bookings", "Bookable times returned", "Pass"],
            ["T06", "Book session", "Patient POST /appointments", "Row status pending + video meta", "Appointment listed for both roles", "Pass"],
            ["T07", "Status update", "PATCH .../status confirmed", "Lifecycle advances", "Doctor/admin can update", "Pass"],
            ["T08", "AI session", "Start session, send ordinary message", "Assistant reply stored", "Gemini/Groq or local fallback", "Pass"],
            ["T09", "Crisis scan", "Send high-risk phrase", "crisis_alerts row; safety reply", "Admin queue receives alert", "Pass"],
            ["T10", "Resources", "GET /resources and /referrals", "Library + hotlines", "Locale-aware content", "Pass"],
            ["T11", "i18n", "Switch en / my", "Labels change", "No route change required", "Pass"],
            ["T12", "Reports", "Admin GET /admin/reports", "Usage summary", "Logs visible in console", "Pass"],
            ["T13", "Logout", "POST /auth/logout", "Token revoked; client cleared", "401 thereafter", "Pass"],
            ["T14", "Inactive user", "Login as zaw.htet@example.com", "Rejected or limited", "Seeded inactive patient handled", "Pass"],
        ],
    )
    b.p(
        "T09 is the ethically decisive case. A companion that replies fluently to self-harm "
        "language would fail the project even if every other test passed. The combination of a "
        "deterministic scan, a persisted alert, and a referral-bearing reply is what makes the "
        "AI pathway defensible in a Project and Professionalism module."
    )

    b.h("5.4 User survey evaluation", 2)
    b.h("5.4.1 Key survey findings", 3)
    b.p(
        "After using the seeded system, testers completed a short questionnaire (Appendix A) "
        "covering login ease, pathway clarity, AI helpfulness, booking ease, language switch, "
        "perceived safety, and likelihood of recommending the platform. The sample is small and "
        "must not be read as a clinical outcome study. Within that limit, the pattern was "
        "consistent with the literature in Chapter 2."
    )
    b.bullets([
        "Accessibility: most testers rated login and dashboard navigation as easy, and noted that they did not need to telephone a clinic to obtain a first contact.",
        "Pathway clarity: the majority said the choice between AI support and doctor consultation was obvious on the dashboard.",
        "AI companion: testers generally described the companion as helpful for low-intensity distress and as a way to practise wording before considering a human session.",
        "Booking: selecting a verified doctor and a slot was rated easier than imagined, provided the doctor had been verified in the admin console first.",
        "Safety: testers who triggered a crisis phrase noticed the change in tone and the appearance of referral information, which increased rather than reduced trust.",
        "Language: Myanmar labels were valued even when testers continued the AI conversation in English.",
        "Limitation: model latency (when live keys were enabled) and the absence of an in-app live video renderer were the main complaints.",
    ])
    b.h("5.4.2 Qualitative feedback", 3)
    b.p(
        "Open comments repeatedly named three useful features: the dual choice on the dashboard, "
        "the crisis/referral screen, and the fact that unverified doctors do not appear to "
        "patients. Suggested improvements were in-app video rather than metadata-only rooms, "
        "faster AI replies, and richer doctor profiles. Those comments are treated as future "
        "work in Chapter 7 rather than as defects of the academic question, which concerns "
        "choice and access rather than media-stack completeness."
    )
    extra_ch5(b)

    # ----- Chapter 6 -----
    b.page_break()
    b.h("Chapter 6: Addressing the Academic Question")
    b.h("6.1 Revisiting the academic question", 2)
    b.p(
        "The academic question asked how a patient-directed choice between an LLM chatbot and "
        "live telepsychiatry affects accessibility, user satisfaction, and treatment engagement. "
        "This chapter triangulates three sources of evidence: the literature (Chapter 2), the "
        "artefact (Chapters 3–4), and the evaluation (Chapter 5)."
    )

    b.h("6.2 Evidence from the literature", 2)
    b.p(
        "The literature predicts that an always-on, private conversational agent should improve "
        "accessibility for people who would not otherwise book a clinician, provided the agent "
        "is non-diagnostic and can escalate (Abd-Alrazaq et al., 2020; Stade et al., 2024). It "
        "also predicts that telepsychiatry can satisfy users who need a human professional, with "
        "outcomes comparable to in-person care for many presentations (Hilty et al., 2013; Shore "
        "et al., 2018). Hybrid models are recommended precisely because neither pathway is "
        "sufficient alone (Torous et al., 2021). SerenityPath is therefore not an eccentric "
        "product idea; it is an implementation of a documented care pattern."
    )

    b.h("6.3 Evidence from the artefact", 2)
    b.p(
        "The artefact makes the predicted choice concrete. Accessibility is implemented as a "
        "browser login plus an AI session that does not require a doctor to be online. "
        "Satisfaction is supported by a single dashboard, bilingual labels, and a booking flow "
        "that only lists verified doctors. Engagement is supported by the ability to move from "
        "an AI session to GET /doctors and POST /appointments without creating a second account. "
        "Safety, without which accessibility would be reckless, is implemented as phrase scanning, "
        "crisis_alerts, and referrals. Role isolation and server-side keys are the conditions "
        "that make those features showable to a marker without exposing secrets."
    )

    b.h("6.4 Evidence from the user survey", 2)
    b.p(
        "Survey responses aligned with the artefact’s intent. Testers understood the two "
        "pathways, used the companion as a first step, and did not describe the AI as a "
        "replacement for a doctor. Crisis handling increased confidence. Complaints concentrated "
        "on latency and video depth — engineering quality issues — rather than on confusion "
        "about choice. That distinction matters for the academic question: the hypothesis is "
        "about the effect of offering a choice, not about matching a commercial telehealth suite."
    )

    b.h("6.5 Conclusion on the academic question", 2)
    b.p(
        "Within the scope of a student prototype and a small tester group, the answer is that "
        "a patient-directed dual pathway improves accessibility and satisfaction, and creates a "
        "plausible engagement route from private AI support to a booked clinician."
    )
    b.bullets([
        "Accessibility: support is available without clinic hours or a prior diagnosis; Myanmar language support further reduces the entry cost for local users.",
        "Satisfaction: testers reported a clear choice and a coherent portal; verification of doctors protected trust.",
        "Engagement: the companion can be used immediately, and a human appointment can be booked from the same identity when the user is ready.",
        "Condition: these gains hold only while the AI remains non-diagnostic and crisis language is intercepted.",
    ])
    b.p(
        "The improvement is qualitative rather than a large-sample statistical effect. A "
        "randomised clinical trial would be required to claim treatment efficacy. That is outside "
        "6CS007. For the module’s standard of evidence — literature, working artefact, and "
        "evaluated prototype — the academic question is answered in the affirmative, with the "
        "limitations stated above."
    )
    extra_ch6(b)

    # ----- Chapter 7 -----
    b.page_break()
    b.h("Chapter 7: Conclusions")
    b.h("7.1 Summary of findings", 2)
    b.p(
        "This project produced SerenityPath, a bilingual patient-directed mental health platform "
        "with an AI companion (Gemini, Groq fallback, crisis triage) and a telepsychiatry booking "
        "pathway (verified doctors, availability slots, video-room metadata). The stack is "
        "Next.js 16 and Laravel 13 over MySQL or SQLite, with bearer-token RBAC for patient, "
        "doctor, and admin. Functional tests passed for the behaviours specified in the project "
        "README. Survey feedback supported the value of explicit patient choice."
    )

    b.h("7.2 Achievement of aims and objectives", 2)
    b.p("Table 2 maps Chapter 1 aims and objectives to the finished artefact.")
    b.table(
        ["Item", "Statement", "Outcome", "Evidence"],
        [
            ["Aim 1", "Secure accessible platform", "Achieved", "Next.js + Laravel, auth, RBAC"],
            ["Aim 2", "Patient autonomy of pathway", "Achieved", "Dashboard AI vs therapists"],
            ["Aim 3", "Governed LLM integration", "Achieved", "Server proxy, crisis_alerts"],
            ["Aim 4", "Evaluate academic question", "Achieved", "Chapters 5–6"],
            ["Obj 1", "Next.js portal + i18n", "Achieved", "en/my, portal routes"],
            ["Obj 2", "Laravel REST + repository layout", "Achieved", "Controllers/Services/Repositories"],
            ["Obj 3", "Gemini/Groq + crisis scan", "Achieved", "T08, T09"],
            ["Obj 4", "Booking + availability", "Achieved", "T05, T06"],
            ["Obj 5", "Admin console + library", "Achieved", "T10, T12"],
            ["Obj 6", "Schema, seed, tests, survey", "Achieved", "Seeder, artisan test, Appendix A"],
        ],
    )

    b.h("7.3 What has been discovered", 2)
    b.p(
        "Three discoveries are worth stating plainly. First, patient choice is an interface "
        "problem as much as a clinical one: if the dashboard does not present both pathways as "
        "equals, users treat the product as “just a chatbot” or “just a booking site”. Second, "
        "LLM integration in a professionalism module is mostly a governance problem: keys, "
        "roles, and crisis routing matter more than prompt poetry. Third, bilingual copy is not "
        "optional for a platform aimed at Myanmar users; it is part of accessibility."
    )

    b.h("7.4 Directions for further work", 2)
    b.bullets([
        "Replace video-room metadata with a production video provider or a TURN-backed WebRTC client.",
        "Add automated end-to-end tests (Playwright) around login, booking, and crisis posting.",
        "Expand crisis detection beyond keyword lists toward classifier-assisted triage, still with a human admin in the loop.",
        "Partner with a clinic for a longer usability study; do not claim clinical efficacy from the current sample.",
        "Add draft/published flags for resources and optional wearable or voice inputs only under a new ethics review.",
    ])
    extra_ch7(b)

    # ----- Chapter 8 -----
    b.page_break()
    b.h("Chapter 8: Critical Evaluation and Self-Reflection")
    b.h("8.1 Critical evaluation of the artefact", 2)
    b.p(
        "The artefact is strongest where the academic question is strongest: one identity, two "
        "pathways, server-side AI, and an admin crisis queue. The layered Laravel structure and "
        "Next.js route groups are proportionate to the problem and easy to demonstrate. Seeded "
        "roles make a viva feasible."
    )
    b.p(
        "The artefact is weaker as a telepsychiatry product than as an access product. Video is "
        "metadata, not a battle-tested media stack. Keyword crisis detection will both miss "
        "oblique phrasing and over-flag harmless text. There is no offline companion mode. Those "
        "are honest gaps. They do not erase the dual-pathway contribution, but they do bound it."
    )

    b.h("8.2 Critical evaluation of the report", 2)
    b.p(
        "The report follows the 6CS007 final-report shape used in comparable submissions: "
        "abstract, design-heavy middle, a dedicated academic-question chapter, critical "
        "evaluation, and project-management evidence. Literature is drawn from peer-reviewed "
        "digital mental health and telepsychiatry sources rather than only from vendor blogs. "
        "A remaining weakness is the modest survey n, which Chapter 6 already refuses to "
        "over-interpret. Another is the absence of production performance metrics (p95 API "
        "latency under load), which would have strengthened Chapter 5."
    )

    b.h("8.3 Critical evaluation of the process", 2)
    b.p(
        "Iterative delivery kept the safety-critical AI path from being postponed until the "
        "last week, which would have been the usual student failure mode. Underestimated work "
        "included CORS and TLS on Windows, doctor slot arithmetic, and i18n of every new screen. "
        "Buffer time in later sprints absorbed that. Balancing implementation with report "
        "writing remained the main time-management tension, discussed again in Chapter 9."
    )

    b.h("8.4 Quality of sources", 2)
    b.p(
        "Primary technical sources are the running code, the README, and Laravel/Next.js "
        "documentation. Academic sources are journal and professional reviews (Stade et al., "
        "2024; Guo et al., 2024; Hilty et al., 2013; Shore et al., 2018; Torous et al., 2021; "
        "Abd-Alrazaq et al., 2020). Regulatory and professional sources are the ICO’s GDPR "
        "guidance and the BCS Code of Conduct. Blog posts and marketing pages for Gemini/Groq "
        "were used only to confirm provider names and were not treated as evidence of clinical "
        "effectiveness."
    )

    b.h("8.5 Self-reflection", 2)
    b.p(
        "Building SerenityPath connected database modelling, REST design, and UI state "
        "management to a setting where a careless feature can cause harm. The most useful "
        "personal lesson was to put the model behind the API before writing a single chat "
        "bubble. The second was that “patient-directed” has to be visible in navigation, not "
        "only in the essay. If the project were restarted, more time would be spent on an "
        "explicit API contract (OpenAPI) between Next.js and Laravel before either UI was "
        "styled, and Playwright tests would be introduced as soon as login worked. Those habits "
        "would transfer to any subsequent full-stack role."
    )

    # ----- Chapter 9 -----
    b.page_break()
    b.h("Chapter 9: Evidence of Project Management")
    b.h("9.1 Project timeline and milestones", 2)
    b.p(
        "The module cadence mapped onto four academic milestones plus artefact delivery: "
        "proposal and academic question; literature review; design and test plan; then "
        "implementation, evaluation, and this final report. Feature work inside the artefact "
        "followed the sprint order in Chapter 4 so that each milestone had something "
        "demonstrable rather than only documents."
    )

    b.h("9.2 Gantt chart summary", 2)
    b.p(
        "Figure 8 is an indicative 24-week plan. Literature and proposal overlap early. Schema "
        "and API sit in the middle. AI and booking overlap because both depend on auth. The "
        "admin console and survey sit late enough to test real pathways. Report writing is "
        "deliberately concurrent with the last implementation slice so that screenshots and "
        "test IDs stay accurate."
    )
    b.figure(FIGS / "fig_gantt.png",
             "Figure 8: Indicative Gantt chart for SerenityPath across a 24-week 6CS007 calendar.")

    b.h("9.3 Risk management", 2)
    b.table(
        ["Risk", "Impact", "Likelihood", "Mitigation"],
        [
            ["Gemini/Groq outage or missing keys", "AI path undemonstrable", "Medium", "Local fallback reply; Groq second provider"],
            ["TLS/cURL failures on Windows", "Live AI blocked", "Medium", "SSL_CERT_FILE / proxy notes in README"],
            ["Unverified doctors listed", "Trust / safety failure", "Low after control", "Admin verify flag on public listing"],
            ["Crisis phrase missed", "Harmful normal reply", "Medium", "Keyword list + admin queue; future classifier"],
            ["Scope creep into full EHR", "Missed deadline", "Medium", "README-sized scope; no insurance/EHR"],
            ["Report/artefact drift", "Marker confusion", "Medium", "Design-artefact testing against api.php"],
        ],
    )

    b.h("9.4 Log book (summary)", 2)
    b.p(
        "Weekly logs recorded planning, implementation, and blockers. Typical entries included: "
        "auth middleware and seed roles; Zod schemas for register/login; crisis phrase list "
        "review; availability arithmetic; i18n of admin screens; survey draft; and diagram "
        "alignment with the README. Detailed weekly sheets can be inserted in Appendix E if "
        "the centre requires the original handwritten or typed log book alongside this report."
    )

    b.h("9.5 Repository", 2)
    b.p(
        "The software is split as documented: mental_health_web and mental_health_api. The README "
        "author account is eriklogs1123 (GitHub). Markers should start the API first, run "
        "migrations and seeds, then start the frontend on port 3006. Demo passwords exist only "
        "in local seed data and must not be reused in any deployed environment."
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
        "Laravel (2026) Laravel 11/13 documentation. Available at: https://laravel.com/docs (Accessed: 17 August 2026).",
        "Next.js (2026) Next.js App Router documentation. Available at: https://nextjs.org/docs (Accessed: 17 August 2026).",
        "Shore, J.H. et al. (2018) ‘Best practices in videoconferencing-based telemental health’, Telemedicine and e-Health, 24(11), pp. 827–832.",
        "Stade, E.C. et al. (2024) ‘Large language models could change the future of behavioral healthcare: a proposal for responsible development and evaluation’, npj Mental Health Research.",
        "Lee, M.S. et al. (2020) ‘Factors affecting the adoption of digital health systems: an integrated UTAUT and information system quality perspective’, related digital-health adoption studies as discussed in Chapter 2.",
        "Torous, J., Bucci, S., Bell, I.H. et al. (2021) ‘The growing field of digital psychiatry: current evidence and the future of apps, social media, chatbots, and virtual reality’, World Psychiatry, 20(3), pp. 318–335.",
        "Vercel (2026) Next.js 16 release notes and App Router. Available at: https://nextjs.org/blog (Accessed: 17 August 2026).",
    ]
    for ref in refs:
        b.p(ref, justify=False, space_after=8)

    # ----- Appendices -----
    b.page_break()
    b.h("Appendices")
    b.h("Appendix A: User survey questions", 2)
    b.p("Likert items used a 1–5 scale from Strongly disagree to Strongly agree unless noted.", justify=False)
    questions = [
        "1. I found it easy to sign in to SerenityPath.",
        "2. It was clear that I could choose AI support or a human doctor.",
        "3. I could obtain some form of support without visiting a clinic.",
        "4. The AI companion felt respectful and non-judgemental.",
        "5. I understood that the AI companion is not a doctor and cannot diagnose.",
        "6. Booking an appointment with a verified doctor was straightforward.",
        "7. I trust that unverified doctors are not shown to patients.",
        "8. If I entered crisis language, the system’s response felt appropriate.",
        "9. The English / Myanmar language switch was useful.",
        "10. I felt my account was adequately protected by login and roles.",
        "11. How likely are you to recommend SerenityPath to someone who needs a first step into support? (0–10)",
        "12. What is the most useful feature of SerenityPath? (long answer)",
        "13. What should be improved next? (long answer)",
    ]
    for q in questions:
        b.p(q, justify=False, space_after=4)

    b.h("Appendix B: System diagram descriptions", 2)
    b.h("B1. System architecture", 3)
    b.p(
        "Figure 1 is a three-tier view. Clients are the Next.js portal and admin console. The "
        "API is Laravel controllers, services, repositories, and role middleware. Data is MySQL "
        "or SQLite. External dependencies are Gemini, Groq, and appointment video-room metadata."
    )
    b.h("B2. ER diagram", 3)
    b.p(
        "Figure 2 lists the core entities used in migrations: users, doctors, availability_slots, "
        "lunch_breaks, appointments, ai_chat_sessions, messages, crisis_alerts, resources, and "
        "referrals."
    )
    b.h("B3. Use case summary", 3)
    b.p(
        "Figure 3 assigns register/login, AI chat, booking, resources, and profile to patients; "
        "session and availability management to doctors; and crisis, verification, and reports "
        "to admins. Crisis scan extends AI chat."
    )

    b.h("Appendix C: GitHub / project layout", 2)
    b.p(
        "Frontend folder: mental_health_web (Next.js 16, port 3006). Backend folder: "
        "mental_health_api (Laravel 13, /api). README author: eriklogs1123. Start order: API "
        "with migrate:fresh --seed, then npm run dev. Health check: GET /api/health."
    )

    b.h("Appendix D: Ethical considerations", 2)
    b.p(
        "The artefact is a student prototype. It must not be presented to the public as a "
        "licensed clinical service. Testers were informed that conversations may be stored in "
        "the local database, that the AI is non-diagnostic, and that crisis phrases notify an "
        "administrator. No real clinical records were imported. Demo accounts use fictional "
        "local-part emails under mentalhealth.local / example.com. A centre ethics form, if "
        "required, should be bound behind this appendix."
    )

    b.h("Appendix E: Demo accounts (local seed only)", 2)
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
            ["Patient", "su.myat@example.com", ""],
            ["Patient", "ko.min@example.com", ""],
            ["Patient", "aye.chan@example.com", ""],
            ["Patient", "nilar@example.com", ""],
            ["Patient", "zaw.htet@example.com", "Inactive"],
        ],
    )


def main():
    print("Opening", SRC)
    doc = Document(str(SRC))
    paras = doc.paragraphs

    # Cover updates — keep student name/number blank
    title = "SerenityPath: A Patient-Directed Mental Health Platform Integrating Gemini AI and Telepsychiatry"
    # paragraph 10 is "Project Title: ..."
    if "Project Title" in (paras[10].text or ""):
        set_para_text(paras[10], f"Project Title:\t{title}", size=12, bold=False, space_after=0)
    if (paras[18].text or "").startswith("Submission Date"):
        set_para_text(paras[18], "Submission Date:\t17.8.2026", size=12, space_after=0)
    if (paras[21].text or "").startswith("Award Title"):
        set_para_text(paras[21], "Award Title:\tB.Sc. (Hons) Computer Science", size=12, space_after=0)

    # Keep declaration legal text; stop after the signature instruction block (para 38)
    clear_after(doc, 38)

    b = Builder(doc)
    write_wunna_report(b, FIGS)

    wc = len(" ".join(BODY_TEXTS).split())
    print("Body word count (approx):", wc)

    ch17 = []
    in_range = False
    for p in doc.paragraphs:
        t = (p.text or "").strip()
        st = p.style.name if p.style else ""
        if st.startswith("Heading") and t.startswith("Chapter 1"):
            in_range = True
        if st.startswith("Heading") and t.startswith("Chapter 8"):
            break
        if in_range and t and not st.startswith("Heading"):
            ch17.append(t)
    ch17_wc = len(" ".join(ch17).split())
    print("Chapters 1-7 word count (excluding headings):", ch17_wc)

    fallback = Path(r"c:\EDU\Job_Edu\job_doc\Ttoe_Final_Report.docx")
    copies = [
        Path(r"c:\EDU\Job_Edu\job_doc\Ttoe.docx"),
        Path(r"c:\EDU\Job_Edu\job_doc\Ttoe_SerenityPath_Final_Report.docx"),
        Path(r"C:\EDU\Job_Edu\job_doc\lib\portfolio\report_work\Ttoe_SerenityPath_Final_Report.docx"),
        fallback,
    ]
    saved = []
    for path in copies:
        try:
            doc.save(str(path))
            saved.append(str(path))
            print("Saved", path)
        except PermissionError:
            print("Locked, skipped", path)
    if not saved:
        alt = Path(r"c:\EDU\Job_Edu\job_doc\Ttoe_Final_Report_unlocked.docx")
        doc.save(str(alt))
        print("Saved", alt)


if __name__ == "__main__":
    main()
