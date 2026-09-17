"""SerenityPath report diagrams."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import (
    Circle,
    Ellipse,
    FancyArrowPatch,
    FancyBboxPatch,
    FancyBboxPatch as FBox,
    Polygon,
    Rectangle,
)

ROOT = Path(r"C:\EDU\Job_Edu\job_doc\lib\portfolio\report_work\serenitypath_figs")
ROOT.mkdir(parents=True, exist_ok=True)

TEAL = "#0F766E"
TEAL_FILL = "#CCFBF1"
NAVY = "#134E4A"
SLATE = "#334155"
LINE = "#0F172A"
BLUE = "#1D4ED8"
BLUE_FILL = "#DBEAFE"
AMBER = "#D97706"
AMBER_FILL = "#FEF3C7"
PURPLE = "#6D28D9"
PURPLE_FILL = "#EDE9FE"
ROSE = "#BE123C"
ROSE_FILL = "#FFE4E6"
GREEN = "#047857"
GREEN_FILL = "#D1FAE5"


def save_fig(fig, path: Path, dpi=220):
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white", pad_inches=0.22)
    plt.close(fig)


def arrow(ax, p1, p2, style="-|>", color=LINE, lw=1.15, ls="-", rad=0):
    ax.add_patch(
        FancyArrowPatch(
            p1, p2, arrowstyle=style, mutation_scale=11, lw=lw, color=color,
            linestyle=ls, connectionstyle=f"arc3,rad={rad}" if rad else "arc3,rad=0",
            shrinkA=0, shrinkB=1,
        )
    )


def box(ax, x, y, w, h, text, fc="#F8FAFC", ec=TEAL, fs=8.2, radius=0.10, bold=False, tc=NAVY):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=f"round,pad=0.02,rounding_size={radius}",
        facecolor=fc, edgecolor=ec, lw=1.25, zorder=3,
    ))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=tc, zorder=4, fontweight="bold" if bold else "normal")
    return x + w / 2, y + h / 2


def stick(ax, x, y, label, color=NAVY, scale=0.95):
    r = 0.22 * scale
    ax.add_patch(Circle((x, y + 1.25 * scale), r, fill=False, lw=1.7, ec=color, zorder=5))
    ax.plot([x, x], [y + 1.03 * scale, y + 0.42 * scale], color=color, lw=1.7, zorder=5)
    ax.plot([x - 0.34 * scale, x + 0.34 * scale], [y + 0.82 * scale, y + 0.82 * scale], color=color, lw=1.7)
    ax.plot([x, x - 0.26 * scale], [y + 0.42 * scale, y], color=color, lw=1.7)
    ax.plot([x, x + 0.26 * scale], [y + 0.42 * scale, y], color=color, lw=1.7)
    ax.text(x, y - 0.28 * scale, label, ha="center", va="top", fontsize=10, color=color, fontweight="bold")


def uc(ax, x, y, w, h, text, fs=7.4):
    ax.add_patch(Ellipse((x, y), w, h, facecolor=TEAL_FILL, edgecolor=TEAL, lw=1.25, zorder=3))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=NAVY, zorder=4)


def draw_architecture(path: Path):
    fig, ax = plt.subplots(figsize=(13.6, 8.4))
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.4)
    ax.axis("off")
    ax.text(6.8, 8.12, "SerenityPath three-tier architecture", ha="center", fontsize=14,
            fontweight="bold", color=NAVY)

    # Clients
    ax.add_patch(Rectangle((0.35, 6.35), 12.9, 1.55, fill=False, lw=1.3, ls=(0, (4, 2)), ec=SLATE))
    ax.text(0.5, 7.68, "Presentation layer  —  Next.js 16  (port 3006)", fontsize=9, color=SLATE, fontweight="bold")
    box(ax, 0.6, 6.5, 3.7, 0.95, "Patient / doctor portal\nDashboard · AI companion\nAppointments · Resources", fc=TEAL_FILL, fs=8.0)
    box(ax, 4.95, 6.5, 3.7, 0.95, "Admin console\nCrisis queue · Users\nReports · Settings", fc=PURPLE_FILL, ec=PURPLE, fs=8.0)
    box(ax, 9.3, 6.5, 3.55, 0.95, "i18n  en / my\nZustand auth store\nTanStack Query + Axios", fc=BLUE_FILL, ec=BLUE, fs=8.0)

    arrow(ax, (6.8, 6.5), (6.8, 5.55))
    ax.text(7.05, 6.0, "HTTPS  REST  Bearer token", fontsize=7.4, color=SLATE)

    # API
    ax.add_patch(Rectangle((0.35, 3.55), 12.9, 2.0, fill=False, lw=1.3, ls=(0, (4, 2)), ec=SLATE))
    ax.text(0.5, 5.32, "Application layer  —  Laravel 13 REST API  (port 8000 /api)", fontsize=9, color=SLATE, fontweight="bold")
    box(ax, 0.55, 3.72, 2.95, 1.35, "Controllers\nAuth · Appointments\nAI chat · Admin", fc="#ECFDF5", fs=7.8)
    box(ax, 3.7, 3.72, 2.95, 1.35, "Services\nBusiness logic\nCrisis scan · Booking", fc="#ECFDF5", fs=7.8)
    box(ax, 6.85, 3.72, 2.95, 1.35, "Repositories\nData access\nEloquent models", fc="#ECFDF5", fs=7.8)
    box(ax, 10.0, 3.72, 2.95, 1.35, "Middleware\nBearer auth\nRole: patient / doctor / admin", fc=AMBER_FILL, ec=AMBER, fs=7.6)

    arrow(ax, (3.7, 3.72), (3.7, 2.85))
    arrow(ax, (10.5, 3.72), (10.5, 2.85))

    # Data + external
    ax.add_patch(Rectangle((0.35, 0.28), 6.55, 2.45, fill=False, lw=1.3, ls=(0, (4, 2)), ec=SLATE))
    ax.text(0.5, 2.48, "Data layer", fontsize=9, color=SLATE, fontweight="bold")
    box(ax, 0.55, 0.48, 6.15, 1.85, "MySQL 8  or  SQLite\nusers · doctors · appointments · ai_chat_sessions\nmessages · crisis_alerts · resources · referrals\navailability_slots · lunch_breaks", fc="#FFF7ED", ec=AMBER, fs=8.0)

    ax.add_patch(Rectangle((7.2, 0.28), 6.05, 2.45, fill=False, lw=1.3, ls=(0, (4, 2)), ec=SLATE))
    ax.text(7.35, 2.48, "External services", fontsize=9, color=SLATE, fontweight="bold")
    box(ax, 7.4, 1.38, 5.65, 0.95, "Google Gemini  (primary AI)\nGroq fallback  ·  AI_PROVIDERS=gemini,groq", fc=ROSE_FILL, ec=ROSE, fs=7.8)
    box(ax, 7.4, 0.42, 5.65, 0.82, "Video-room metadata for telepsychiatry\nsessions (appointment booking)", fc=BLUE_FILL, ec=BLUE, fs=7.6)

    save_fig(fig, path)


def draw_er(path: Path):
    fig, ax = plt.subplots(figsize=(14.4, 9.6))
    ax.set_xlim(0, 14.4)
    ax.set_ylim(0, 9.6)
    ax.axis("off")
    ax.text(7.2, 9.32, "SerenityPath entity-relationship model", ha="center", fontsize=14,
            fontweight="bold", color=NAVY)

    def entity(x, y, w, title, fields, header=TEAL):
        row_h = 0.22
        hh = 0.40
        h = hh + len(fields) * row_h + 0.10
        ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor=NAVY, lw=1.05, zorder=3))
        ax.add_patch(Rectangle((x, y + h - hh), w, hh, facecolor=header, edgecolor=NAVY, lw=1.05, zorder=4))
        ax.text(x + w / 2, y + h - hh / 2, title, ha="center", va="center", fontsize=8.2,
                color="white", fontweight="bold", zorder=5)
        ty = y + h - hh - 0.06
        for f in fields:
            ax.text(x + 0.10, ty, f, ha="left", va="top", fontsize=6.6, color=NAVY, family="monospace", zorder=5)
            ty -= row_h
        return x + w / 2, y + h / 2, x, y, w, h

    entity(0.25, 6.55, 3.55, "users", [
        "id PK", "name", "email UNIQUE", "password",
        "role  patient|doctor|admin", "status  active|inactive",
    ], "#0F766E")
    entity(4.15, 6.55, 3.55, "doctors", [
        "id PK  user_id FK", "license_number", "specialization",
        "verified  bool", "bio",
    ], "#1D4ED8")
    entity(8.05, 6.70, 2.95, "availability_slots", [
        "id PK  doctor_id FK", "weekday", "start_time", "end_time",
    ], "#0369A1")
    entity(11.25, 6.70, 2.90, "lunch_breaks", [
        "id PK  doctor_id FK", "weekday", "start_time", "end_time",
    ], "#0369A1")

    entity(0.25, 3.15, 4.15, "appointments", [
        "id PK  patient_id FK  doctor_id FK",
        "starts_at  ends_at", "status  pending|confirmed|...",
        "video_room_meta", "notes",
    ], "#D97706")
    entity(4.75, 3.35, 4.35, "ai_chat_sessions", [
        "id PK  patient_id FK", "started_at  ended_at",
        "status  open|ended",
    ], "#6D28D9")
    entity(9.40, 3.05, 4.70, "messages", [
        "id PK  session_id FK", "role  user|assistant|system",
        "body", "created_at",
    ], "#6D28D9")

    entity(0.25, 0.28, 4.35, "crisis_alerts", [
        "id PK  patient_id FK  session_id FK",
        "severity  low|medium|high|critical",
        "matched_phrase", "status  open|reviewed",
        "admin_notes",
    ], "#BE123C")
    entity(5.00, 0.55, 4.15, "resources", [
        "id PK", "slug UNIQUE", "title", "body", "locale en|my",
    ], "#047857")
    entity(9.55, 0.55, 4.50, "referrals", [
        "id PK", "name", "phone", "type  hotline|clinic",
        "locale en|my",
    ], "#047857")

    # relationships
    arrow(ax, (3.80, 7.55), (4.15, 7.55), color=SLATE, lw=1.0)
    ax.text(3.95, 7.72, "1:1", fontsize=6.5, color=SLATE)
    arrow(ax, (7.70, 7.55), (8.05, 7.55), color=SLATE, lw=1.0)
    ax.text(7.80, 7.72, "1:N", fontsize=6.5, color=SLATE)
    arrow(ax, (10.95, 7.95), (11.25, 7.95), color=SLATE, lw=1.0)
    ax.text(11.05, 8.12, "1:N", fontsize=6.5, color=SLATE)
    arrow(ax, (2.0, 6.55), (2.0, 5.55), color=SLATE, lw=1.0)
    ax.text(2.15, 6.05, "books N", fontsize=6.5, color=SLATE)
    arrow(ax, (5.9, 6.55), (6.6, 5.55), color=SLATE, lw=1.0)
    ax.text(6.55, 6.05, "opens N", fontsize=6.5, color=SLATE)
    arrow(ax, (9.05, 4.55), (9.40, 4.55), color=SLATE, lw=1.0)
    ax.text(9.10, 4.72, "1:N", fontsize=6.5, color=SLATE)
    arrow(ax, (6.8, 3.35), (3.5, 2.15), color=ROSE, lw=1.0)
    ax.text(5.5, 2.85, "may raise", fontsize=6.5, color=ROSE)

    save_fig(fig, path)


def draw_use_case(path: Path):
    fig, ax = plt.subplots(figsize=(14.6, 9.4))
    ax.set_xlim(0, 14.6)
    ax.set_ylim(0, 9.4)
    ax.axis("off")
    ax.text(7.3, 9.12, "SerenityPath use case diagram", ha="center", fontsize=14, fontweight="bold", color=NAVY)

    ax.add_patch(Rectangle((2.55, 0.35), 9.55, 8.45, fill=False, lw=1.55, ec=NAVY))
    ax.text(7.3, 8.52, "SerenityPath", ha="center", fontsize=12, fontweight="bold", color=NAVY)

    stick(ax, 1.15, 6.35, "Patient", TEAL, 0.92)
    stick(ax, 1.15, 3.55, "Doctor", BLUE, 0.92)
    stick(ax, 13.45, 4.85, "Admin", PURPLE, 0.92)

    patient = [
        (4.55, 7.85, "Register / login"),
        (4.55, 6.95, "Browse therapists"),
        (4.55, 6.05, "Book appointment"),
        (4.55, 5.15, "Chat with AI companion"),
        (4.55, 4.25, "View resources"),
        (4.55, 3.35, "Open crisis / referrals"),
        (4.55, 2.45, "Manage profile"),
        (4.55, 1.55, "Submit feedback"),
    ]
    doctor = [
        (7.35, 7.35, "View my sessions"),
        (7.35, 6.35, "Update appointment status"),
        (7.35, 5.35, "Set availability"),
        (7.35, 4.35, "View patient context"),
    ]
    admin = [
        (10.15, 7.55, "Triage crisis alerts"),
        (10.15, 6.55, "Verify doctors"),
        (10.15, 5.55, "Manage users"),
        (10.15, 4.55, "Manage library"),
        (10.15, 3.55, "View usage reports"),
        (10.15, 2.55, "System settings"),
    ]
    for x, y, t in patient:
        uc(ax, x, y, 2.55, 0.72, t, 7.2)
        arrow(ax, (1.55, 7.05), (x - 1.28, y), style="-", color=TEAL, lw=0.85)
    for x, y, t in doctor:
        uc(ax, x, y, 2.55, 0.72, t, 7.0)
        arrow(ax, (1.55, 4.25), (x - 1.28, y), style="-", color=BLUE, lw=0.85)
    for x, y, t in admin:
        uc(ax, x, y, 2.55, 0.72, t, 7.0)
        arrow(ax, (12.85, 5.55), (x + 1.28, y), style="-", color=PURPLE, lw=0.85)

    # include crisis from AI chat
    arrow(ax, (5.82, 5.15), (8.88, 7.55), style="-|>", color=ROSE, lw=1.0, ls=(0, (4, 2)))
    ax.text(7.55, 6.55, "<<extend>>\ncrisis scan", fontsize=6.4, color=ROSE, ha="center", fontstyle="italic")

    save_fig(fig, path)


def draw_flow(path: Path):
    fig, ax = plt.subplots(figsize=(12.2, 15.4))
    ax.set_xlim(0, 12.2)
    ax.set_ylim(0, 15.4)
    ax.axis("off")
    ax.text(6.1, 15.12, "SerenityPath operational flow", ha="center", fontsize=13, fontweight="bold", color=NAVY)

    def oval(x, y, w, h, text, fc=TEAL):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.32",
                                    facecolor=fc, edgecolor=fc, lw=1.1, zorder=3))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9, color="white", fontweight="bold")

    def dia(cx, cy, w, h, text):
        pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
        ax.add_patch(Polygon(pts, closed=True, facecolor=AMBER_FILL, edgecolor=AMBER, lw=1.25, zorder=3))
        ax.text(cx, cy, text, ha="center", va="center", fontsize=8, color=NAVY, fontweight="bold")

    oval(4.55, 14.25, 3.1, 0.52, "START")
    box(ax, 3.55, 13.35, 5.1, 0.62, "Open SerenityPath  →  /login", fc=TEAL_FILL)
    dia(6.1, 12.25, 3.9, 1.05, "Authenticated?")
    box(ax, 8.55, 11.95, 3.15, 0.62, "Redirect to /login", fc=ROSE_FILL, ec=ROSE, fs=7.6)
    dia(6.1, 10.85, 3.9, 1.05, "Role?")
    box(ax, 0.35, 9.35, 3.4, 0.72, "Admin dashboard\ncrisis · users · reports", fc=PURPLE_FILL, ec=PURPLE, fs=7.6)
    box(ax, 4.35, 9.35, 3.5, 0.72, "Patient / doctor portal\n/dashboard", fc=TEAL_FILL, fs=7.8)
    dia(6.1, 8.15, 4.2, 1.05, "Patient action?")

    box(ax, 0.25, 6.55, 2.7, 0.70, "AI companion\nstart / continue chat", fc=PURPLE_FILL, ec=PURPLE, fs=7.3)
    box(ax, 3.20, 6.55, 2.7, 0.70, "Book session\nagainst slots", fc=GREEN_FILL, ec=GREEN, fs=7.3)
    box(ax, 6.15, 6.55, 2.7, 0.70, "Resources /\ncrisis referrals", fc=BLUE_FILL, ec=BLUE, fs=7.3)
    box(ax, 9.15, 6.55, 2.75, 0.70, "Profile /\nappointments list", fc=AMBER_FILL, ec=AMBER, fs=7.3)

    dia(1.60, 5.25, 2.55, 0.95, "Crisis\nphrase?")
    box(ax, 0.25, 3.85, 2.7, 0.70, "Safety reply +\ncrisis_alerts row", fc=ROSE_FILL, ec=ROSE, fs=7.2)
    box(ax, 0.25, 2.85, 2.7, 0.62, "Gemini / Groq reply", fc=PURPLE_FILL, ec=PURPLE, fs=7.3)

    box(ax, 3.20, 5.15, 2.7, 0.62, "Select doctor + slot", fc=GREEN_FILL, ec=GREEN, fs=7.3)
    box(ax, 3.20, 4.15, 2.7, 0.62, "POST /appointments", fc=GREEN_FILL, ec=GREEN, fs=7.3)
    box(ax, 3.20, 3.15, 2.7, 0.62, "Status: pending", fc=GREEN_FILL, ec=GREEN, fs=7.3)

    box(ax, 6.15, 5.15, 2.7, 0.62, "GET /resources\nGET /referrals", fc=BLUE_FILL, ec=BLUE, fs=7.2)
    box(ax, 9.15, 5.15, 2.75, 0.62, "PATCH /auth/profile\nor list sessions", fc=AMBER_FILL, ec=AMBER, fs=7.1)

    box(ax, 3.35, 1.55, 5.5, 0.62, "Usage log written  ·  continue in portal", fc=TEAL_FILL, fs=8.0)
    oval(4.55, 0.45, 3.1, 0.52, "END")

    arrow(ax, (6.1, 14.25), (6.1, 13.97))
    arrow(ax, (6.1, 13.35), (6.1, 12.77))
    arrow(ax, (8.05, 12.25), (8.55, 12.26))
    ax.text(8.15, 12.48, "no", fontsize=7, color=SLATE)
    arrow(ax, (6.1, 11.73), (6.1, 11.37))
    ax.text(5.35, 11.55, "yes", fontsize=7, color=SLATE)
    arrow(ax, (4.35, 10.85), (2.05, 10.07))
    ax.text(2.7, 10.55, "admin", fontsize=7, color=PURPLE)
    arrow(ax, (6.1, 10.33), (6.1, 10.07))
    ax.text(6.3, 10.45, "patient/doctor", fontsize=7, color=TEAL)
    arrow(ax, (6.1, 9.35), (6.1, 8.67))

    arrow(ax, (4.3, 7.75), (1.6, 7.25))
    arrow(ax, (5.5, 7.65), (4.55, 7.25))
    arrow(ax, (6.7, 7.65), (7.5, 7.25))
    arrow(ax, (7.9, 7.75), (10.5, 7.25))

    arrow(ax, (1.6, 6.55), (1.6, 5.72))
    arrow(ax, (1.6, 4.78), (1.6, 4.55))
    ax.text(1.85, 5.25, "yes", fontsize=6.5, color=ROSE)
    arrow(ax, (0.45, 5.25), (0.45, 3.16), color=PURPLE)
    arrow(ax, (0.45, 3.16), (1.6, 3.16), color=PURPLE)
    ax.text(0.15, 4.2, "no", fontsize=6.5, color=PURPLE, rotation=90)

    arrow(ax, (4.55, 6.55), (4.55, 5.77))
    arrow(ax, (4.55, 5.15), (4.55, 4.77))
    arrow(ax, (4.55, 4.15), (4.55, 3.77))
    arrow(ax, (7.5, 6.55), (7.5, 5.77))
    arrow(ax, (10.52, 6.55), (10.52, 5.77))

    arrow(ax, (1.6, 2.85), (4.0, 1.86))
    arrow(ax, (4.55, 3.15), (5.4, 2.17))
    arrow(ax, (7.5, 5.15), (6.9, 2.17))
    arrow(ax, (10.52, 5.15), (8.2, 1.86))
    arrow(ax, (6.1, 1.55), (6.1, 0.97))

    save_fig(fig, path)


def draw_activity(path: Path):
    fig, ax = plt.subplots(figsize=(13.4, 8.8))
    ax.set_xlim(0, 13.4)
    ax.set_ylim(0, 8.8)
    ax.axis("off")
    ax.text(6.7, 8.52, "Activity: AI message with crisis triage", ha="center", fontsize=13, fontweight="bold", color=NAVY)

    # swimlanes
    lanes = [
        (0.25, "Patient", TEAL_FILL, TEAL),
        (3.50, "Next.js portal", BLUE_FILL, BLUE),
        (6.75, "Laravel API", AMBER_FILL, AMBER),
        (10.00, "Admin", PURPLE_FILL, PURPLE),
    ]
    for x, title, fc, ec in lanes:
        ax.add_patch(Rectangle((x, 0.35), 3.15, 7.85, facecolor=fc, edgecolor=ec, lw=1.15, alpha=0.35))
        ax.text(x + 1.57, 7.95, title, ha="center", fontsize=10, fontweight="bold", color=ec)

    box(ax, 0.45, 6.85, 2.75, 0.55, "Type message", fc="white", fs=8)
    box(ax, 3.70, 6.85, 2.75, 0.55, "POST /messages", fc="white", fs=8)
    box(ax, 6.95, 6.85, 2.75, 0.55, "Validate Bearer +\npatient role", fc="white", fs=7.5)
    box(ax, 6.95, 5.85, 2.75, 0.55, "Scan crisis phrases", fc="white", fs=8)

    ax.add_patch(Polygon([(8.32, 5.45), (9.55, 4.85), (8.32, 4.25), (7.10, 4.85)],
                         closed=True, facecolor=AMBER_FILL, edgecolor=AMBER, lw=1.2, zorder=3))
    ax.text(8.32, 4.85, "Match?", ha="center", va="center", fontsize=8, fontweight="bold")

    box(ax, 6.95, 3.25, 2.75, 0.62, "Insert crisis_alerts\n+ safety reply", fc=ROSE_FILL, ec=ROSE, fs=7.4)
    box(ax, 6.95, 2.25, 2.75, 0.55, "Gemini / Groq reply", fc="white", fs=8)
    box(ax, 10.20, 3.25, 2.75, 0.62, "Crisis queue\nreview + notes", fc=PURPLE_FILL, ec=PURPLE, fs=7.4)
    box(ax, 3.70, 1.15, 2.75, 0.55, "Render reply +\nreferrals if crisis", fc="white", fs=7.5)
    box(ax, 0.45, 1.15, 2.75, 0.55, "Read support\nor helplines", fc="white", fs=7.6)

    arrow(ax, (3.20, 7.12), (3.70, 7.12))
    arrow(ax, (6.45, 7.12), (6.95, 7.12))
    arrow(ax, (8.32, 6.85), (8.32, 6.40))
    arrow(ax, (8.32, 5.85), (8.32, 5.45))
    arrow(ax, (8.32, 4.25), (8.32, 3.87))
    ax.text(8.55, 4.15, "yes", fontsize=7, color=ROSE)
    arrow(ax, (7.10, 4.70), (8.32, 2.80), color=GREEN)
    ax.text(6.85, 3.55, "no", fontsize=7, color=GREEN)
    arrow(ax, (9.70, 3.56), (10.20, 3.56), color=ROSE)
    arrow(ax, (8.32, 3.25), (5.05, 1.70))
    arrow(ax, (8.32, 2.25), (5.05, 1.55))
    arrow(ax, (3.70, 1.42), (3.20, 1.42))

    save_fig(fig, path)


def _phone(ax, x, y, w, h, title, rows, header=TEAL):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.18",
                                facecolor="white", edgecolor=NAVY, lw=1.4, zorder=2))
    ax.add_patch(Rectangle((x, y + h - 0.70), w, 0.70, facecolor=header, zorder=3))
    ax.text(x + w / 2, y + h - 0.35, title, ha="center", va="center", fontsize=8.5,
            color="white", fontweight="bold", zorder=4)
    ty = y + h - 0.95
    for label, sub in rows:
        ax.add_patch(FancyBboxPatch((x + 0.12, ty - 0.62), w - 0.24, 0.68,
                                    boxstyle="round,pad=0.02,rounding_size=0.08",
                                    facecolor="#F8FAFC", edgecolor="#CBD5E1", lw=0.8, zorder=3))
        ax.text(x + 0.22, ty - 0.18, label, fontsize=7.2, color=NAVY, fontweight="bold", zorder=4)
        ax.text(x + 0.22, ty - 0.42, sub, fontsize=6.4, color=SLATE, zorder=4)
        ty -= 0.78
    ax.add_patch(Rectangle((x + w * 0.35, y + 0.12), w * 0.30, 0.08, facecolor=NAVY, zorder=3))


def draw_wireframes(path: Path):
    fig, ax = plt.subplots(figsize=(14.8, 8.6))
    ax.set_xlim(0, 14.8)
    ax.set_ylim(0, 8.6)
    ax.axis("off")
    ax.text(7.4, 8.28, "SerenityPath UI wireframes (portal and admin)", ha="center",
            fontsize=13, fontweight="bold", color=NAVY)

    _phone(ax, 0.25, 0.45, 2.7, 7.55, "Login", [
        ("Email", "patient@example.com"),
        ("Password", "••••••••"),
        ("Sign in", "Bearer token stored"),
        ("Language", "English  |  Myanmar"),
    ], TEAL)
    _phone(ax, 3.15, 0.45, 2.7, 7.55, "Dashboard", [
        ("AI companion", "24/7 emotional support"),
        ("Therapists", "Verified doctors"),
        ("My sessions", "pending / confirmed"),
        ("Resources", "Library + helplines"),
    ], TEAL)
    _phone(ax, 6.05, 0.45, 2.7, 7.55, "AI companion", [
        ("Session list", "Start new chat"),
        ("User message", "I feel anxious today"),
        ("Assistant", "Supportive, non-diagnostic"),
        ("Safety banner", "If crisis → referrals"),
    ], PURPLE)
    _phone(ax, 8.95, 0.45, 2.7, 7.55, "Book session", [
        ("Doctor card", "Dr Smith  ·  verified"),
        ("Available slots", "From weekly template"),
        ("Confirm", "POST /appointments"),
        ("Status", "pending → confirmed"),
    ], GREEN)
    _phone(ax, 11.85, 0.45, 2.7, 7.55, "Admin crisis", [
        ("Alert queue", "severity + phrase"),
        ("Patient link", "session context"),
        ("Update status", "reviewed / notes"),
        ("Reports", "usage summary"),
    ], ROSE)

    save_fig(fig, path)


def draw_gantt(path: Path):
    fig, ax = plt.subplots(figsize=(12.8, 6.6))
    tasks = [
        ("Proposal & academic question", 0, 3, TEAL),
        ("Literature review", 2, 6, BLUE),
        ("Requirements & stack choice", 5, 3, PURPLE),
        ("Database schema & migrations", 7, 3, AMBER),
        ("Laravel API (auth, RBAC)", 8, 5, TEAL),
        ("AI companion + crisis scan", 11, 5, ROSE),
        ("Appointments & availability", 12, 5, GREEN),
        ("Next.js portal + i18n", 10, 8, BLUE),
        ("Admin console", 15, 4, PURPLE),
        ("Testing & user survey", 18, 4, AMBER),
        ("Final report & submission", 20, 4, NAVY),
    ]
    ax.set_xlim(0, 24)
    ax.set_ylim(-0.6, len(tasks) + 0.8)
    ax.invert_yaxis()
    ax.set_xlabel("Project week", fontsize=9, color=SLATE)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([t[0] for t in tasks], fontsize=8.5)
    ax.set_xticks(range(0, 25, 2))
    ax.grid(axis="x", linestyle=":", color="#CBD5E1")
    ax.set_title("SerenityPath project Gantt chart (indicative 24-week plan)", fontsize=12,
                 fontweight="bold", color=NAVY, pad=10)
    for i, (_, start, dur, c) in enumerate(tasks):
        ax.barh(i, dur, left=start, height=0.55, color=c, edgecolor="white", linewidth=0.6)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    save_fig(fig, path)


def draw_structure(path: Path):
    fig, ax = plt.subplots(figsize=(13.2, 8.2))
    ax.set_xlim(0, 13.2)
    ax.set_ylim(0, 8.2)
    ax.axis("off")
    ax.text(6.6, 7.88, "Repository layout", ha="center", fontsize=14, fontweight="bold", color=NAVY)

    def folder(x, y, w, h, title, lines, ec=TEAL):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.10",
                                    facecolor="white", edgecolor=ec, lw=1.3, zorder=3))
        ax.add_patch(Rectangle((x, y + h - 0.48), w, 0.48, facecolor=ec, zorder=4))
        ax.text(x + w / 2, y + h - 0.24, title, ha="center", va="center", fontsize=9,
                color="white", fontweight="bold", zorder=5)
        ty = y + h - 0.68
        for line in lines:
            ax.text(x + 0.16, ty, line, ha="left", va="top", fontsize=7.4, color=NAVY,
                    family="monospace", zorder=5)
            ty -= 0.28

    folder(0.30, 0.35, 6.15, 7.20, "mental_health_web  (Next.js 16)", [
        "app/                 App Router pages",
        "  (portal)/          patient & doctor UI",
        "  (admin)/           admin console",
        "api/                 Axios modules",
        "actions/             auth cookies",
        "components/          UI + layouts",
        "hooks/               React Query",
        "store/               Zustand auth",
        "schema/              Zod",
        "i18n/                en.json / my.json",
        "middleware.ts        route protection",
    ], TEAL)
    folder(6.75, 0.35, 6.15, 7.20, "mental_health_api  (Laravel 13)", [
        "app/Http/Controllers/Api/",
        "app/Http/Middleware/     Bearer + roles",
        "app/Http/Requests/       validation",
        "app/Services/            AI, booking, admin",
        "app/Repositories/",
        "app/Models/  app/Enums/",
        "database/migrations/",
        "database/seeders/",
        "docs/DATABASE_SCHEMA.md",
        "routes/api.php",
        "php artisan test",
    ], AMBER)
    save_fig(fig, path)


def class_box(ax, x, y, w, title, attrs, methods, header="#0F766E"):
    row_h = 0.20
    header_h = 0.38
    pad = 0.08
    attr_h = max(len(attrs), 1) * row_h + pad
    meth_h = max(len(methods), 1) * row_h + pad
    h = header_h + attr_h + meth_h
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor=NAVY, lw=1.05, zorder=3))
    ax.add_patch(Rectangle((x, y + h - header_h), w, header_h, facecolor=header, edgecolor=NAVY, lw=1.05, zorder=4))
    ax.text(x + w / 2, y + h - header_h / 2, title, ha="center", va="center", fontsize=7.4,
            color="white", fontweight="bold", zorder=5)
    y_div = y + meth_h
    ax.plot([x, x + w], [y_div, y_div], color=NAVY, lw=0.7, zorder=4)
    ty = y + h - header_h - 0.05
    for line in attrs or [" "]:
        ax.text(x + 0.08, ty, line, ha="left", va="top", fontsize=6.2, color=NAVY, family="monospace", zorder=5)
        ty -= row_h
    ty = y + meth_h - 0.05
    for line in methods or [" "]:
        ax.text(x + 0.08, ty, line, ha="left", va="top", fontsize=6.2, color=SLATE, family="monospace", zorder=5)
        ty -= row_h
    return x + w / 2, y, y + h


def draw_class(path: Path):
    fig, ax = plt.subplots(figsize=(14.6, 9.8))
    ax.set_xlim(0, 14.6)
    ax.set_ylim(0, 9.8)
    ax.axis("off")
    ax.text(7.3, 9.52, "SerenityPath class diagram (domain + services)", ha="center",
            fontsize=13, fontweight="bold", color=NAVY)

    class_box(ax, 0.25, 6.85, 3.35, "User",
              ["- id: int", "- email: string", "- role: Enum", "- status: Enum"],
              ["+login()", "+updateProfile()"], TEAL)
    class_box(ax, 3.85, 6.70, 3.45, "Doctor",
              ["- user_id: FK", "- licence: string", "- verified: bool"],
              ["+setAvailability()", "+updateStatus()"], BLUE)
    class_box(ax, 7.55, 6.85, 3.35, "Appointment",
              ["- patient_id, doctor_id", "- status: Enum", "- video_room_meta"],
              ["+book()", "+changeStatus()"], AMBER)
    class_box(ax, 11.15, 6.85, 3.20, "AvailabilitySlot",
              ["- doctor_id: FK", "- weekday", "- start, end"],
              ["+computeBookable()"], "#0369A1")

    class_box(ax, 0.25, 3.55, 3.45, "AiChatSession",
              ["- patient_id: FK", "- status: open|ended"],
              ["+start()", "+end()"], PURPLE)
    class_box(ax, 3.95, 3.35, 3.45, "Message",
              ["- session_id: FK", "- role: user|assistant", "- body"],
              ["+create()"], PURPLE)
    class_box(ax, 7.65, 3.35, 3.45, "CrisisAlert",
              ["- session_id, patient_id", "- severity: Enum", "- status, notes"],
              ["+raise()", "+review()"], ROSE)
    class_box(ax, 11.25, 3.70, 3.10, "Resource / Referral",
              ["- slug / name", "- locale: en|my"],
              ["+listPublic()"], GREEN)

    class_box(ax, 0.55, 0.35, 4.15, "<<service>> AuthService",
              ["Bearer token", "role middleware"],
              ["+register()", "+login()", "+logout()"], TEAL)
    class_box(ax, 5.15, 0.35, 4.25, "<<service>> AppointmentService",
              ["slots - lunch - bookings"],
              ["+availableSlots()", "+book()"], GREEN)
    class_box(ax, 9.80, 0.35, 4.40, "<<service>> AiChatService",
              ["Gemini then Groq", "phrase scan first"],
              ["+reply()", "+scanCrisis()"], ROSE)

    arrow(ax, (3.60, 8.3), (3.85, 8.3), color=SLATE, lw=1.0)
    ax.text(3.65, 8.48, "1:1", fontsize=6.4, color=SLATE)
    arrow(ax, (7.30, 8.3), (7.55, 8.3), color=SLATE, lw=1.0)
    ax.text(7.35, 8.48, "1:N", fontsize=6.4, color=SLATE)
    arrow(ax, (3.70, 6.70), (9.0, 5.55), color=SLATE, lw=0.9)
    arrow(ax, (1.95, 6.85), (1.95, 5.85), color=SLATE, lw=0.9)
    arrow(ax, (5.70, 5.55), (7.65, 5.0), color=ROSE, lw=0.9)
    save_fig(fig, path)


def draw_sequence(path: Path):
    fig, ax = plt.subplots(figsize=(13.6, 7.6))
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 7.6)
    ax.axis("off")
    ax.text(6.8, 7.28, "Behaviour: book appointment (sequence)", ha="center",
            fontsize=13, fontweight="bold", color=NAVY)
    actors = [(1.4, "Patient UI"), (4.4, "Axios"), (7.4, "Appointment\nController"), (10.8, "Appointment\nService / DB")]
    for x, name in actors:
        box(ax, x - 1.15, 6.15, 2.3, 0.75, name, fc=TEAL_FILL, fs=7.6, bold=True)
        ax.plot([x, x], [6.15, 0.45], color="#94A3B8", lw=1.1, ls=(0, (3, 2)))

    def msg(y, x1, x2, text, dashed=False):
        arrow(ax, (x1, y), (x2, y), color=NAVY, lw=1.05, ls=(0, (4, 2)) if dashed else "-")
        ax.text((x1 + x2) / 2, y + 0.12, text, ha="center", fontsize=6.6, color=NAVY)

    msg(5.55, 1.4, 4.4, "select doctor + slot")
    msg(4.85, 4.4, 7.4, "POST /api/appointments  Bearer")
    msg(4.15, 7.4, 10.8, "validate role + slot free")
    msg(3.45, 10.8, 7.4, "insert status=pending + video meta", dashed=True)
    msg(2.75, 7.4, 4.4, "201 JSON appointment", dashed=True)
    msg(2.05, 4.4, 1.4, "invalidate Query cache; show list", dashed=True)
    box(ax, 4.7, 0.55, 4.2, 0.55, "Doctor later PATCH /status → confirmed", fc=AMBER_FILL, ec=AMBER, fs=7.4)
    save_fig(fig, path)


def main():
    files = {
        "architecture": ROOT / "fig_architecture.png",
        "er": ROOT / "fig_er.png",
        "usecase": ROOT / "fig_usecase.png",
        "flow": ROOT / "fig_flow.png",
        "activity": ROOT / "fig_activity.png",
        "wireframes": ROOT / "fig_wireframes.png",
        "gantt": ROOT / "fig_gantt.png",
        "structure": ROOT / "fig_structure.png",
        "class": ROOT / "fig_class.png",
        "sequence": ROOT / "fig_sequence.png",
    }
    draw_architecture(files["architecture"])
    draw_er(files["er"])
    draw_use_case(files["usecase"])
    draw_flow(files["flow"])
    draw_activity(files["activity"])
    draw_wireframes(files["wireframes"])
    draw_gantt(files["gantt"])
    draw_structure(files["structure"])
    draw_class(files["class"])
    draw_sequence(files["sequence"])
    print("Wrote", len(files), "figures to", ROOT)


if __name__ == "__main__":
    main()
