"""Build BlogVault academic report from Template_Report.docx + README."""
from __future__ import annotations

import copy
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import (
    Circle,
    Ellipse,
    FancyArrowPatch,
    FancyBboxPatch,
    Polygon,
    Rectangle,
)
from matplotlib.lines import Line2D
from PIL import Image as PILImage

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor, Emu
from docx.text.paragraph import Paragraph

ROOT = Path(r"C:\EDU\Job_Edu\job_doc\lib\portfolio\report_work")
TEMPLATE = Path(r"c:\Users\User\Downloads\Telegram Desktop\Template_Report.docx")
OUT_PRIMARY = Path(r"c:\Users\User\Downloads\Telegram Desktop\BlogVault_Report.docx")
OUT_COPY = ROOT / "BlogVault_Report.docx"

TEAL = "#0F766E"
TEAL_FILL = "#CCFBF1"
AMBER = "#D97706"
AMBER_FILL = "#FEF3C7"
NAVY = "#1E293B"
SLATE = "#334155"
LINE = "#0F172A"
EXT = "#7C3AED"
INC = "#0369A1"


def save_fig(fig, path: Path, dpi=220):
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor="white", pad_inches=0.25)
    plt.close(fig)


def arrow(ax, p1, p2, style="-|>", color=LINE, lw=1.15, ls="-", rad=0):
    ax.add_patch(
        FancyArrowPatch(
            p1,
            p2,
            arrowstyle=style,
            mutation_scale=11,
            lw=lw,
            color=color,
            linestyle=ls,
            connectionstyle=f"arc3,rad={rad}" if rad else "arc3,rad=0",
            shrinkA=0,
            shrinkB=1,
        )
    )


def stick_figure(ax, x, y, scale=1.0, label="User"):
    r = 0.28 * scale
    ax.add_patch(Circle((x, y + 1.55 * scale), r, fill=False, lw=1.8, ec=NAVY, zorder=5))
    ax.plot([x, x], [y + 1.27 * scale, y + 0.55 * scale], color=NAVY, lw=1.8, zorder=5)
    ax.plot([x - 0.42 * scale, x + 0.42 * scale], [y + 1.05 * scale, y + 1.05 * scale], color=NAVY, lw=1.8, zorder=5)
    ax.plot([x, x - 0.32 * scale], [y + 0.55 * scale, y], color=NAVY, lw=1.8, zorder=5)
    ax.plot([x, x + 0.32 * scale], [y + 0.55 * scale, y], color=NAVY, lw=1.8, zorder=5)
    ax.text(x, y - 0.35 * scale, label, ha="center", va="top", fontsize=11, color=NAVY, fontweight="bold")


def use_case_ellipse(ax, x, y, w, h, text, fs=8.2):
    e = Ellipse((x, y), w, h, facecolor=TEAL_FILL, edgecolor=TEAL, lw=1.35, zorder=3)
    ax.add_patch(e)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=NAVY, zorder=4, fontweight="medium")
    return x, y, w, h


def dashed_rel(ax, p1, p2, label, color, label_off=(0, 0.16)):
    arrow(ax, p1, p2, style="-|>", color=color, lw=1.05, ls=(0, (5, 2.4)))
    ax.text(
        (p1[0] + p2[0]) / 2 + label_off[0],
        (p1[1] + p2[1]) / 2 + label_off[1],
        label,
        fontsize=6.5,
        color=color,
        ha="center",
        fontstyle="italic",
        zorder=6,
        bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9),
    )


def draw_use_case(path: Path):
    fig, ax = plt.subplots(figsize=(14.2, 9.2))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 9.2)
    ax.axis("off")

    ax.add_patch(Rectangle((2.7, 0.45), 11.15, 8.4, fill=False, lw=1.7, ec=NAVY))
    ax.text(8.25, 8.58, "BlogVault", ha="center", va="center", fontsize=14, fontweight="bold", color=NAVY)

    stick_figure(ax, 1.25, 3.7, scale=1.12)

    # Primary (left column inside system)
    prim = {
        "create": (4.85, 7.85, "Create post"),
        "edit": (4.85, 6.55, "Edit post"),
        "list": (4.85, 5.25, "View post list"),
        "detail": (4.85, 3.95, "View post detail"),
        "search": (4.85, 2.65, "Search posts"),
        "delete": (4.85, 1.35, "Delete post"),
    }
    for key, (x, y, t) in prim.items():
        use_case_ellipse(ax, x, y, 2.7, 0.82, t, fs=8.6)
        arrow(ax, (1.85, 4.75), (x - 1.36, y), style="-", color=SLATE, lw=1.0)

    # Secondary (right columns)
    sec = {
        "gallery": (8.55, 7.85, "Attach gallery\nphoto"),
        "camera": (11.7, 7.85, "Capture in-app\ncamera photo"),
        "save": (10.15, 6.55, "Save to SQLite\n(blogvault.db)"),
        "mdelete": (8.55, 5.45, "Multi-select\ndelete"),
        "mupload": (11.7, 4.95, "Multi-select\nPinterest upload"),
        "share": (8.55, 3.55, "Share via\nACTION_SEND"),
        "pin": (11.7, 2.95, "Upload to\nPinterest"),
    }
    for x, y, t in sec.values():
        use_case_ellipse(ax, x, y, 2.45, 0.92, t, fs=7.7)

    # Create / Edit optional media + required save
    dashed_rel(ax, (6.2, 7.85), (7.32, 7.85), "<<extend>>", EXT)
    dashed_rel(ax, (6.2, 8.05), (10.48, 8.12), "<<extend>>", EXT, (0, 0.18))
    dashed_rel(ax, (6.2, 6.55), (7.32, 7.55), "<<extend>>", EXT, (0.15, 0.05))
    dashed_rel(ax, (6.2, 6.72), (10.48, 7.58), "<<extend>>", EXT, (0.4, 0.05))
    dashed_rel(ax, (6.2, 7.65), (8.95, 6.9), "<<include>>", INC, (0.35, -0.02))
    dashed_rel(ax, (6.2, 6.55), (8.92, 6.55), "<<include>>", INC)

    # List optional multi-select
    dashed_rel(ax, (6.2, 5.25), (7.32, 5.45), "<<extend>>", EXT)
    dashed_rel(ax, (6.2, 5.05), (10.48, 4.95), "<<extend>>", EXT, (0.55, -0.22))

    # Detail optional share / pinterest
    dashed_rel(ax, (6.2, 3.95), (7.32, 3.55), "<<extend>>", EXT)
    dashed_rel(ax, (6.2, 3.75), (10.48, 2.95), "<<extend>>", EXT, (0.55, -0.22))

    ax.text(
        8.25,
        0.18,
        "Solid line = association     Dashed purple = optional <<extend>>     Dashed blue = required <<include>>",
        ha="center",
        fontsize=7.4,
        color=SLATE,
    )
    save_fig(fig, path)


def rounded(ax, x, y, w, h, text, fc="#F8FAFC", ec=TEAL, fs=8.0, radius=0.12, bold=False):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle=f"round,pad=0.02,rounding_size={radius}",
            facecolor=fc,
            edgecolor=ec,
            lw=1.25,
            zorder=3,
        )
    )
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fs,
        color=NAVY,
        zorder=4,
        fontweight="bold" if bold else "normal",
        wrap=True,
    )
    return x + w / 2, y + h / 2


def diamond(ax, cx, cy, w, h, text, fs=7.8):
    pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=AMBER_FILL, edgecolor=AMBER, lw=1.3, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, color=NAVY, zorder=4, fontweight="bold")
    return cx, cy


def oval_term(ax, x, y, w, h, text, fc=TEAL, tc="white"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.35",
                                facecolor=fc, edgecolor=fc, lw=1.2, zorder=3))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9, color=tc,
            fontweight="bold", zorder=4)
    return x + w / 2, y + h / 2


def draw_flow_chart(path: Path):
    fig, ax = plt.subplots(figsize=(12.4, 15.2))
    ax.set_xlim(0, 12.4)
    ax.set_ylim(0, 15.2)
    ax.axis("off")

    ax.text(6.2, 14.95, "BlogVault operational flow", ha="center", fontsize=13, fontweight="bold", color=NAVY)

    oval_term(ax, 4.7, 14.15, 3.0, 0.55, "START")
    rounded(ax, 3.9, 13.25, 4.6, 0.62, "Open BlogVault (MainActivity)", fc=TEAL_FILL)
    rounded(ax, 3.55, 12.35, 5.3, 0.62, "Load posts from SQLite  (blogvault.db / messages)", fc=TEAL_FILL)
    rounded(ax, 3.7, 11.45, 5.0, 0.62, "Display home list  (RecyclerView cards)", fc=TEAL_FILL)
    diamond(ax, 6.2, 10.35, 4.4, 1.15, "User action?")

    # four branches
    rounded(ax, 0.25, 8.85, 2.7, 0.7, "Create / Edit\n(+ FAB or Edit)", fc="#ECFDF5", ec="#059669", fs=7.6)
    rounded(ax, 3.25, 8.85, 2.7, 0.7, "View detail\n(tap a post)", fc="#EFF6FF", ec="#2563EB", fs=7.6)
    rounded(ax, 6.25, 8.85, 2.7, 0.7, "Search\n(menu keyword)", fc="#FFF7ED", ec="#EA580C", fs=7.6)
    rounded(ax, 9.25, 8.85, 2.9, 0.7, "Multi-select\n(long-press posts)", fc="#F5F3FF", ec="#7C3AED", fs=7.6)

    arrow(ax, (6.2, 14.15), (6.2, 13.87))
    arrow(ax, (6.2, 13.25), (6.2, 12.97))
    arrow(ax, (6.2, 12.35), (6.2, 12.07))
    arrow(ax, (6.2, 11.45), (6.2, 10.92))

    arrow(ax, (4.3, 10.0), (1.6, 9.55))
    arrow(ax, (5.5, 9.85), (4.6, 9.55))
    arrow(ax, (6.9, 9.85), (7.6, 9.55))
    arrow(ax, (8.1, 10.0), (10.7, 9.55))

    ax.text(2.6, 10.05, "create", fontsize=6.5, color="#059669")
    ax.text(4.55, 10.18, "view", fontsize=6.5, color="#2563EB")
    ax.text(7.55, 10.18, "search", fontsize=6.5, color="#EA580C")
    ax.text(9.55, 10.05, "select", fontsize=6.5, color="#7C3AED")

    # create branch
    diamond(ax, 1.6, 7.75, 2.55, 0.95, "Photo?")
    rounded(ax, 0.15, 6.45, 2.9, 0.62, "Gallery  or  CameraX", fc="#ECFDF5", ec="#059669", fs=7.4)
    rounded(ax, 0.15, 5.55, 2.9, 0.62, "Tap Save", fc="#ECFDF5", ec="#059669", fs=7.6)
    rounded(ax, 0.15, 4.65, 2.9, 0.62, "MessageDao.insert / update", fc="#ECFDF5", ec="#059669", fs=7.2)
    arrow(ax, (1.6, 8.85), (1.6, 8.22))
    arrow(ax, (1.6, 7.28), (1.6, 7.07))
    arrow(ax, (1.6, 6.45), (1.6, 6.17))
    arrow(ax, (1.6, 5.55), (1.6, 5.27))
    ax.text(0.15, 7.75, "no", fontsize=6.4, color=SLATE)
    ax.text(2.55, 7.18, "yes", fontsize=6.4, color=SLATE)
    # no photo -> save directly (left of diamond)
    arrow(ax, (0.55, 7.55), (0.55, 6.17), color="#059669")
    arrow(ax, (0.55, 6.17), (1.6, 6.17), color="#059669")

    # view branch
    diamond(ax, 4.6, 7.75, 2.6, 0.95, "Next\naction?")
    rounded(ax, 3.25, 6.45, 2.7, 0.62, "Share  (any app)", fc="#EFF6FF", ec="#2563EB", fs=7.4)
    rounded(ax, 3.25, 5.55, 2.7, 0.62, "Upload to Pinterest", fc="#EFF6FF", ec="#2563EB", fs=7.4)
    rounded(ax, 3.25, 4.65, 2.7, 0.62, "Delete this post", fc="#EFF6FF", ec="#2563EB", fs=7.4)
    arrow(ax, (4.6, 8.85), (4.6, 8.22))
    arrow(ax, (4.6, 7.28), (4.6, 7.07))
    arrow(ax, (4.6, 6.45), (4.6, 6.17))
    arrow(ax, (4.6, 5.55), (4.6, 5.27))

    # search branch
    rounded(ax, 6.25, 7.45, 2.7, 0.62, "Query title / body\non diskIO thread", fc="#FFF7ED", ec="#EA580C", fs=7.3)
    rounded(ax, 6.25, 6.45, 2.7, 0.62, "Show matching posts", fc="#FFF7ED", ec="#EA580C", fs=7.4)
    rounded(ax, 6.25, 5.55, 2.7, 0.62, "Open a result (detail)", fc="#FFF7ED", ec="#EA580C", fs=7.4)
    arrow(ax, (7.6, 8.85), (7.6, 8.07))
    arrow(ax, (7.6, 7.45), (7.6, 7.07))
    arrow(ax, (7.6, 6.45), (7.6, 6.17))

    # multi-select
    diamond(ax, 10.7, 7.75, 2.55, 0.95, "Upload or\ndelete?")
    rounded(ax, 9.25, 6.45, 2.9, 0.62, "Combine photos\ninto one collage", fc="#F5F3FF", ec="#7C3AED", fs=7.2)
    rounded(ax, 9.25, 5.55, 2.9, 0.62, "ACTION_SEND to\ncom.pinterest", fc="#F5F3FF", ec="#7C3AED", fs=7.2)
    rounded(ax, 9.25, 4.65, 2.9, 0.62, "MessageDao.deleteMany", fc="#F5F3FF", ec="#7C3AED", fs=7.2)
    arrow(ax, (10.7, 8.85), (10.7, 8.22))
    arrow(ax, (10.7, 7.28), (10.7, 7.07))
    arrow(ax, (10.7, 6.45), (10.7, 6.17))
    arrow(ax, (11.95, 7.75), (11.95, 4.96), color="#7C3AED")
    ax.text(12.15, 6.35, "delete", fontsize=6.3, color="#7C3AED", rotation=90, va="center")
    ax.text(9.35, 7.55, "upload", fontsize=6.3, color="#7C3AED")

    rounded(ax, 3.35, 3.35, 5.7, 0.7, "Refresh list  (only if Activity is still alive / UiSafe)", fc=TEAL_FILL, fs=8.0)
    diamond(ax, 6.2, 2.25, 3.6, 1.0, "Continue\nusing app?")
    oval_term(ax, 4.7, 0.55, 3.0, 0.55, "END")

    arrow(ax, (1.6, 4.65), (4.4, 3.7))
    arrow(ax, (4.6, 4.65), (5.5, 4.05))
    arrow(ax, (7.6, 5.55), (7.0, 4.05))
    arrow(ax, (10.7, 4.65), (8.0, 3.7))
    arrow(ax, (6.2, 3.35), (6.2, 2.75))
    arrow(ax, (6.2, 1.75), (6.2, 1.1))
    # loop back
    arrow(ax, (4.4, 2.25), (1.15, 2.25), color=SLATE)
    arrow(ax, (1.15, 2.25), (1.15, 11.76), color=SLATE)
    arrow(ax, (1.15, 11.76), (3.7, 11.76), color=SLATE)
    ax.text(0.35, 6.9, "yes: return\nto home list", fontsize=6.5, color=SLATE, rotation=90, va="center")
    ax.text(7.95, 2.25, "no", fontsize=7, color=SLATE)

    save_fig(fig, path)


def class_box(ax, x, y, w, title, attrs, methods, header="#0F766E"):
    row_h = 0.22
    header_h = 0.42
    pad = 0.10
    attr_h = max(len(attrs), 1) * row_h + pad
    meth_h = max(len(methods), 1) * row_h + pad
    h = header_h + attr_h + meth_h
    ax.add_patch(Rectangle((x, y), w, h, facecolor="white", edgecolor=NAVY, lw=1.15, zorder=3))
    ax.add_patch(Rectangle((x, y + h - header_h), w, header_h, facecolor=header, edgecolor=NAVY, lw=1.15, zorder=4))
    ax.text(x + w / 2, y + h - header_h / 2, title, ha="center", va="center", fontsize=8.0,
            color="white", fontweight="bold", zorder=5)
    y_div = y + meth_h
    ax.plot([x, x + w], [y_div, y_div], color=NAVY, lw=0.8, zorder=4)
    ty = y + h - header_h - 0.06
    for line in attrs or [" "]:
        ax.text(x + 0.10, ty, line, ha="left", va="top", fontsize=7.0, color=NAVY, family="monospace", zorder=5)
        ty -= row_h
    ty = y + meth_h - 0.06
    for line in methods or [" "]:
        ax.text(x + 0.10, ty, line, ha="left", va="top", fontsize=7.0, color=SLATE, family="monospace", zorder=5)
        ty -= row_h
    return x + w / 2, y, y + h, w


def draw_class_diagram(path: Path):
    """UML class diagram of the real local SQLite schema (messages table)."""
    fig, ax = plt.subplots(figsize=(14.8, 10.6))
    ax.set_xlim(0, 14.8)
    ax.set_ylim(0, 10.6)
    ax.axis("off")
    ax.text(
        7.4, 10.32,
        "Local SQLite database class diagram",
        ha="center", fontsize=14, fontweight="bold", color=NAVY,
    )
    ax.text(
        7.4, 9.95,
        "File: blogvault.db    Table: messages    Path: /data/data/com.blogvault.app/databases/blogvault.db",
        ha="center", fontsize=8.2, color=SLATE,
    )

    # Database file
    class_box(
        ax, 0.35, 7.55, 4.4, "<<SQLite>>  blogvault.db",
        ["DB_NAME = blogvault.db", "engine = SQLite (WAL)", "package = com.blogvault.app"],
        ["created at runtime", "view in Database Inspector"],
        "#0F766E",
    )
    class_box(
        ax, 5.15, 7.55, 4.5, "<<SQLiteOpenHelper>>  DatabaseHelper",
        ["- instance: singleton", "- DATABASE_VERSION", "- TABLE_MESSAGES = messages"],
        ["+getInstance(ctx)", "+onCreate()  // CREATE TABLE", "+onUpgrade()", "+getWritableDatabase()"],
        "#BE185D",
    )
    class_box(
        ax, 10.05, 7.35, 4.4, "<<DAO>>  MessageDao",
        ["- helper: DatabaseHelper"],
        ["+insert(msg): long", "+update(msg): int", "+delete(id): int",
         "+deleteMany(ids): int", "+getById(id): BlogMessage",
         "+getAll(): List", "+search(query): List"],
        "#1D4ED8",
    )

    # Real table — the main artefact
    class_box(
        ax, 0.55, 3.15, 6.7, "<<table>>  messages",
        [
            "+ _id : INTEGER  {PK, AUTOINCREMENT}",
            "+ title : TEXT  {NOT NULL}",
            "+ body : TEXT  {NULL}",
            "+ image_path : TEXT  {NULL}",
            "+ created_at : INTEGER  {NOT NULL}",
            "+ updated_at : INTEGER  {NOT NULL}",
            "+ remote_url : TEXT  {NULL}",
        ],
        [
            "ORDER BY updated_at DESC",
            "SEARCH: title LIKE ? OR body LIKE ?",
        ],
        "#D97706",
    )
    class_box(
        ax, 8.0, 3.15, 6.4, "<<entity>>  BlogMessage",
        [
            "- id : long            <->  _id",
            "- title : String       <->  title",
            "- body : String        <->  body",
            "- imagePath : String   <->  image_path",
            "- createdAt : long     <->  created_at",
            "- updatedAt : long     <->  updated_at",
            "- remoteUrl : String   <->  remote_url",
        ],
        ["+getters / setters", "+hasImage(): boolean"],
        "#0F766E",
    )

    # SQL note — real CREATE TABLE
    sql_x, sql_y, sql_w, sql_h = 0.55, 0.22, 13.9, 2.55
    ax.add_patch(FancyBboxPatch(
        (sql_x, sql_y), sql_w, sql_h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="#F8FAFC", edgecolor=NAVY, lw=1.15, zorder=3,
    ))
    ax.add_patch(Rectangle((sql_x, sql_y + sql_h - 0.38), sql_w, 0.38,
                           facecolor="#1E293B", edgecolor=NAVY, lw=1.15, zorder=4))
    ax.text(sql_x + sql_w / 2, sql_y + sql_h - 0.19,
            "Real local schema  (DatabaseHelper.onCreate)",
            ha="center", va="center", fontsize=8.5, color="white", fontweight="bold", zorder=5)
    sql = (
        "CREATE TABLE messages (\n"
        "    _id         INTEGER PRIMARY KEY AUTOINCREMENT,\n"
        "    title       TEXT NOT NULL,\n"
        "    body        TEXT,\n"
        "    image_path  TEXT,\n"
        "    created_at  INTEGER NOT NULL,\n"
        "    updated_at  INTEGER NOT NULL,\n"
        "    remote_url  TEXT\n"
        ");"
    )
    ax.text(0.85, sql_y + sql_h - 0.52, sql, ha="left", va="top",
            fontsize=8.0, color=NAVY, family="monospace", zorder=5, linespacing=1.35)

    # Relationships
    arrow(ax, (2.55, 7.55), (2.55, 6.55), color=SLATE, lw=1.15)
    ax.text(2.75, 7.05, "1  contains", fontsize=7.2, color=SLATE)
    arrow(ax, (7.4, 7.55), (4.0, 6.55), color=SLATE, lw=1.15)
    ax.text(6.15, 7.15, "creates / opens", fontsize=7.2, color=SLATE)
    arrow(ax, (12.25, 7.35), (12.25, 6.55), color=SLATE, lw=1.15)
    arrow(ax, (12.25, 6.55), (11.2, 6.0), color=SLATE, lw=1.15)
    ax.text(12.4, 6.7, "maps rows", fontsize=7.2, color=SLATE)
    arrow(ax, (10.05, 8.4), (9.65, 8.4), color=SLATE, lw=1.15)
    ax.text(9.55, 8.58, "uses", fontsize=7.2, color=SLATE, ha="right")
    arrow(ax, (7.25, 5.4), (8.0, 5.4), color=AMBER, lw=1.25)
    ax.text(7.62, 5.58, "1  <<maps>>  1", fontsize=7.4, color=AMBER, ha="center", fontweight="bold")
    arrow(ax, (12.25, 7.35), (4.8, 6.4), color="#1D4ED8", lw=1.05)
    ax.text(8.6, 6.85, "CRUD on table", fontsize=7.2, color="#1D4ED8")

    save_fig(fig, path)


def folder(ax, x, y, w, h, title, lines, header="#0F766E"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor="white", edgecolor=header, lw=1.2, zorder=3))
    ax.add_patch(FancyBboxPatch((x, y + h - 0.38), w, 0.38, boxstyle="round,pad=0.01,rounding_size=0.08",
                                facecolor=header, edgecolor=header, lw=0.5, zorder=4))
    ax.text(x + w / 2, y + h - 0.19, title, ha="center", va="center", fontsize=8,
            color="white", fontweight="bold", zorder=5)
    ty = y + h - 0.52
    for line in lines:
        ax.text(x + 0.1, ty, line, ha="left", va="top", fontsize=6.4, color=NAVY, family="monospace", zorder=5)
        ty -= 0.22


def draw_structure(path: Path):
    fig, ax = plt.subplots(figsize=(13.6, 8.2))
    ax.set_xlim(0, 13.6)
    ax.set_ylim(0, 8.2)
    ax.axis("off")
    ax.text(6.8, 7.95, "BlogVault project file structure  (Figure 5.1)", ha="center",
            fontsize=12.5, fontweight="bold", color=NAVY)

    folder(ax, 0.25, 4.55, 4.35, 3.15, "java/com/blogvault/app", [
        "MainActivity.java",
        "MessageEditActivity.java",
        "MessageDetailActivity.java",
        "SearchActivity.java",
        "CameraCaptureActivity.java",
        "BlogVaultGlideModule.java",
        "adapter/MessageAdapter.java",
        "model/BlogMessage.java",
    ], "#0F766E")
    folder(ax, 4.8, 4.55, 4.2, 3.15, "db  +  util", [
        "db/DatabaseHelper.java",
        "db/MessageDao.java",
        "util/AppExecutors.java",
        "util/ImageUtils.java",
        "util/PinterestUploadHelper.java",
        "util/ShareHelper.java",
        "util/UiSafe.java",
    ], "#1D4ED8")
    folder(ax, 9.2, 4.55, 4.15, 3.15, "res  +  build", [
        "res/layout/",
        "res/menu/",
        "res/values/  (teal + amber)",
        "res/drawable/",
        "AndroidManifest.xml",
        "app/build.gradle",
        "settings.gradle",
        "README.md",
    ], "#D97706")

    folder(ax, 0.25, 0.35, 4.35, 3.85, "SQLite schema  messages", [
        "_id            INTEGER PK",
        "title          TEXT",
        "body           TEXT",
        "image_path     TEXT",
        "created_at     INTEGER",
        "updated_at     INTEGER",
        "remote_url     TEXT",
        "",
        "File: blogvault.db",
        "Path: /data/data/com.blogvault.app/",
        "         databases/blogvault.db",
    ], "#BE185D")
    folder(ax, 4.8, 0.35, 4.2, 3.85, "Tech stack", [
        "Language     Java 17",
        "Min SDK      API 24 (Android 7)",
        "Target SDK   API 34 (Android 14)",
        "UI           Material + ConstraintLayout",
        "Database     SQLite (WAL)",
        "Images       Glide 4.16",
        "Camera       CameraX 1.3.4",
        "Build        Gradle 8.7 / AGP 8.5.2",
    ], "#0F766E")
    folder(ax, 9.2, 0.35, 4.15, 3.85, "Permissions", [
        "INTERNET",
        "   open Pinterest",
        "CAMERA",
        "   in-app capture",
        "READ_MEDIA_IMAGES",
        "   gallery (Android 13+)",
        "READ_EXTERNAL_STORAGE",
        "   gallery (Android 12-)",
        "",
        "Share via FileProvider",
    ], "#7C3AED")
    save_fig(fig, path)


# ---------- Word helpers ----------

def set_run_font(run, size_pt=11, bold=None, name="Arial", color=None, italic=None):
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


def insert_after(paragraph, text, size=11, bold=False, italic=False, space_after=8, align=None, color=None, style="Normal"):
    new_p = OxmlElement("w:p")
    paragraph._element.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    try:
        new_para.style = style
    except Exception:
        pass
    set_para_text(new_para, text, size=size, bold=bold, italic=italic, align=align,
                  space_after=space_after, color=color)
    # justify body text
    if align is None:
        new_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pPr = new_para._p.get_or_add_pPr()
        jc = pPr.find(qn("w:jc"))
        if jc is None:
            jc = OxmlElement("w:jc")
            pPr.append(jc)
        jc.set(qn("w:val"), "both")
    return new_para


def insert_table_after(paragraph, headers, rows):
    """Insert a table immediately after paragraph; return the table's trailing marker para."""
    doc = paragraph.part.document
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        run = p.add_run(h)
        set_run_font(run, 9, bold=True, color="FFFFFF")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tc = hdr[i]._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "0F766E")
        tcPr.append(shd)

    for ri, row in enumerate(rows):
        cells = table.add_row().cells
        fill = "F0FDFA" if ri % 2 == 0 else "FFFFFF"
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            run = p.add_run(val)
            set_run_font(run, 8.5, bold=(i == 0))
            tc = cells[i]._tc
            tcPr = tc.get_or_add_tcPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), fill)
            tcPr.append(shd)

    tbl = table._tbl
    paragraph._element.addnext(tbl)
    # python-docx also appended the table at end of body; remove the duplicate
    body = paragraph.part.element.body
    # last tbl in body may be the one add_table created at the end
    tbls = body.findall(qn("w:tbl"))
    if len(tbls) >= 2 and tbls[-1] is not tbl:
        body.remove(tbls[-1])
    elif tbls and tbls[-1] is tbl and tbl.getparent() is body:
        # table is both after paragraph (addnext) AND was originally at end —
        # addnext moved it, so no duplicate. Good.
        pass
    return table


def shade_status_pass(table):
    last = len(table.columns) - 1
    for ri, row in enumerate(table.rows[1:], start=1):
        cell = row.cells[last]
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = RGBColor(0x04, 0x78, 0x57)


def replace_inline_image(doc, index, png_path, width_in, height_in):
    shape = doc.inline_shapes[index]
    blip = shape._inline.graphic.graphicData.pic.blipFill.blip
    rId = blip.get(qn("r:embed"))
    part = doc.part.related_parts[rId]
    part._blob = Path(png_path).read_bytes()
    shape.width = Inches(width_in)
    shape.height = Inches(height_in)


def png_size_inches(path: Path, max_width=6.25):
    im = PILImage.open(path)
    w, h = im.size
    width = max_width
    height = width * (h / w)
    # keep under ~8.6in so it fits a page with captions
    if height > 8.4:
        height = 8.4
        width = height * (w / h)
    return width, height


def update_footers(doc):
    for section in doc.sections:
        for footer in (section.footer, section.first_page_footer):
            try:
                for table in footer.tables:
                    if table.rows:
                        cells = table.rows[0].cells
                        if len(cells) >= 1:
                            set_para_text(cells[0].paragraphs[0], "BLOGVAULT REPORT", size=8, bold=False, color="808080")
                        if len(cells) >= 2:
                            p = cells[1].paragraphs[0]
                            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                            set_para_text(p, "6CS057 MOBILE APPLICATION", size=8, color="808080",
                                          align=WD_ALIGN_PARAGRAPH.RIGHT)
            except Exception:
                pass


def word_count(texts):
    return len(" ".join(texts).split())


S1 = (
    "BlogVault is an offline-first Android blogging client developed for the Mobile Application "
    "Design and Development module. The application lets a user create, edit, view, delete, and "
    "search blog posts entirely on the device, with no internet required for those core actions. "
    "A post can contain a title, body text, and an optional photograph taken with the in-app CameraX "
    "camera or chosen from the gallery. Every record is written to a local SQLite database named "
    "blogvault.db, so content is still present after the application is closed and opened again."
)
S1b = (
    "When the user wants to publish or send a post, BlogVault uses Android intents instead of a "
    "custom server. Share opens the system share sheet so the post can go to Messages, email, or "
    "any compatible app. Upload to Pinterest opens the official Pinterest application with the post "
    "image and caption through ACTION_SEND; no developer token is stored in the project. Several "
    "posts can be selected together, combined into one collage image, and sent to Pinterest in a "
    "single launch. The project therefore demonstrates offline data management, media capture, "
    "Material Design user-interface work, and integration with a public social platform."
)
S2 = (
    "The application was built in Android Studio using Java 17, Gradle 8.7, and Android Gradle "
    "Plugin 8.5.2. The minimum SDK is API 24 (Android 7.0) and the target SDK is API 34 (Android 14). "
    "The interface uses Material Components, ConstraintLayout, and CoordinatorLayout, with a teal "
    "and amber theme, card layouts, and a toolbar. Images are loaded with Glide 4.16. Photography "
    "is handled inside CameraCaptureActivity with CameraX 1.3.4, so the system Camera application "
    "does not need to open."
)
S2b = (
    "Local persistence is implemented with SQLiteOpenHelper in DatabaseHelper, which is a singleton "
    "and enables Write-Ahead Logging. MessageDao performs insert, update, delete, bulk delete, "
    "get-by-id, and search. Database and file work runs on AppExecutors.diskIO(). User-interface "
    "updates are posted only when the hosting Activity is still alive, using UiSafe. Runtime camera "
    "and gallery permissions are requested from MessageEditActivity. Shared files are exposed with "
    "FileProvider rather than a public path."
)
S2c = (
    "The client supports offline create, edit, view, and delete; search by title or body on a "
    "background thread; gallery and in-app camera attachments; system sharing; single-post and "
    "multi-select upload to Pinterest; and multi-select delete. These functions match the brief for "
    "an online/offline blogging client that stores content locally and can publish it to a social "
    "platform. Pinterest must be installed on the demonstration device. If emulator camera hardware "
    "fails, gallery attachment is used instead."
)
S3 = (
    "The design uses a simple layered Android structure that is straightforward to explain in a "
    "demonstration. The user works with five screens: the home list (MainActivity), create and edit "
    "(MessageEditActivity), post detail (MessageDetailActivity), search (SearchActivity), and in-app "
    "camera (CameraCaptureActivity). Helpers bind the RecyclerView, process images, share content, "
    "and launch Pinterest. The data layer maps BlogMessage objects through MessageDao onto SQLite."
)
S3b = (
    "Figure 4.1 shows the use cases. Create and edit can optionally attach a gallery photo or an "
    "in-app camera photo, and both include a save to SQLite. View detail can be extended by share "
    "or Pinterest upload. The home list can be extended by multi-select delete and multi-select "
    "upload. Figure 4.2 shows the operational flow from opening the app, loading posts, choosing an "
    "action, writing to the database, and returning to the list. Figure 4.3 shows the real local "
    "SQLite class model: the messages table in blogvault.db, the BlogMessage entity that maps each "
    "column, DatabaseHelper which runs CREATE TABLE, and MessageDao which performs insert, update, "
    "delete, search, and bulk delete."
)
S4 = (
    "Source code lives under app/src/main/java/com/blogvault/app. Activities occupy the root of that "
    "package. The adapter package holds MessageAdapter, which uses DiffUtil and Glide. The model "
    "package holds BlogMessage. The db package holds DatabaseHelper and MessageDao. The util package "
    "holds AppExecutors, ImageUtils, PinterestUploadHelper, ShareHelper, and UiSafe. Layouts, menus, "
    "colours, and drawables are under res. The database file is created at runtime at "
    "/data/data/com.blogvault.app/databases/blogvault.db and is inspected in Android Studio with "
    "App Inspection, Database Inspector. Figure 5.1 summarises this layout, the messages table "
    "columns, the technology stack, and the declared permissions."
)
S5 = (
    "Manual functional testing was carried out on an emulator and, where camera or Pinterest "
    "behaviour mattered, on a physical device. Each marking-related function was checked against "
    "the expected result. The table below records the main cases used while preparing the demonstration."
)
S5b = (
    "The results confirm that BlogVault meets the required offline create, edit, view, search, and "
    "delete behaviour. Gallery and in-app camera attachment work when hardware and permissions are "
    "available. Share opens the system sheet. Pinterest upload opens the Pinterest app with an image "
    "and caption when that app is installed. Multi-select upload builds one collage and launches "
    "Pinterest once. Persistence was checked by restarting the application and confirming rows in "
    "Database Inspector. Live screenshots from the demonstration should be attached beside this "
    "table in the final Canvas pack."
)
S6 = (
    "Several practical issues shaped the final design. Emulator camera hardware is unreliable and "
    "often shows a black preview, so BlogVault captures photos inside the app with CameraX instead "
    "of launching the system Camera app. Gallery remains the fallback on weak emulators. Gallery "
    "access also differs by API level: READ_MEDIA_IMAGES on Android 13 and above, and "
    "READ_EXTERNAL_STORAGE on earlier versions, so MessageEditActivity requests the correct permission."
)
S6b = (
    "Pinterest does not require an API token in this project. Early cloud options that need client "
    "IDs or OAuth were judged brittle for a short viva. ACTION_SEND targeted at com.pinterest opens "
    "the user's own Pinterest account with the image and text. Multi-select upload originally failed "
    "because several images could not be sent as a simple single-stream share. The fix is to combine "
    "selected photos into one collage in ImageUtils, then send that one image. Posts without a photo "
    "are rendered to a JPEG from their title and body so Pinterest always receives a picture."
)
S6c = (
    "Sharing uses FileProvider rather than a raw filesystem path, which avoids FileUriExposedException "
    "on modern Android. Database work is kept off the main thread through AppExecutors, and UiSafe "
    "prevents updates after an Activity is destroyed. Multi-select state is held as selected identifiers "
    "in MessageAdapter so a list refresh does not drop the selection. These decisions favoured a "
    "reliable demonstration of offline storage, media, sharing, and social upload within the time available."
)
S7 = (
    "BlogVault delivers an offline-first Android blogging client with SQLite persistence, in-app "
    "camera and gallery attachments, keyword search, single and group delete, Android sharing, and "
    "Pinterest upload for online publishing. The architecture keeps user-interface code, helpers, "
    "and data access in separate packages, which makes the application easier to test and explain. "
    "The project aligns with the module requirement for an online/offline blogging or social client "
    "and is ready for demonstration, documentation, and submission. Later work could add categories, "
    "a draft/published flag, or optional cloud synchronisation, but the current scope already covers "
    "the specified offline CRUD, media, intent sharing, and public-platform upload outcomes."
)

ALL_BODY = [S1, S1b, S2, S2b, S2c, S3, S3b, S4, S5, S5b, S6, S6b, S6c, S7]


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    p_use = ROOT / "figure_4_1_use_case.png"
    p_flow = ROOT / "figure_4_2_flow_chart.png"
    p_class = ROOT / "figure_4_3_class_diagram.png"
    p_struct = ROOT / "figure_5_1_structure.png"

    print("Drawing diagrams...")
    draw_use_case(p_use)
    draw_flow_chart(p_flow)
    draw_class_diagram(p_class)
    draw_structure(p_struct)
    for p in (p_use, p_flow, p_class, p_struct):
        print(" ", p, PILImage.open(p).size)

    wc = word_count(ALL_BODY)
    # include short table tokens roughly
    extra = (
        "create edit search delete gallery camera share Pinterest multi-select persistence "
        "SQLite FileProvider CameraX Glide Material"
    )
    wc_total = word_count(ALL_BODY + [extra])
    print("Word count sections 1-7:", wc, "with labels ~", wc_total)

    doc = Document(str(TEMPLATE))
    paras = doc.paragraphs

    # Cover
    set_para_text(paras[1], "BlogVault", size=20, bold=True, space_after=4)
    set_para_text(
        paras[2],
        "An Online/Offline Blogging Client App Report",
        size=20,
        bold=True,
        space_after=10,
    )
    set_para_text(paras[4], "Name", size=20, bold=True, space_after=2)
    set_para_text(paras[5], "xxx", size=20, space_after=8)
    set_para_text(paras[7], "Student ID", size=20, bold=True, space_after=2)
    set_para_text(paras[8], "xxx", size=20, space_after=8)
    set_para_text(paras[10], "Course Title", size=20, bold=True, space_after=2)
    set_para_text(paras[11], "BSc Computer Science", size=20, space_after=8)
    set_para_text(paras[14], "Module Name", size=20, bold=True, space_after=2)
    set_para_text(paras[15], "Mobile Application Design and Development", size=20, space_after=8)
    set_para_text(paras[17], "Module Code", size=20, bold=True, space_after=2)
    set_para_text(paras[18], "6CS057", size=20, space_after=8)
    set_para_text(paras[20], "Center Name", size=20, bold=True, space_after=2)
    set_para_text(paras[21], "Strategy First University, Mandalay, Myanmar", size=20, space_after=8)
    set_para_text(paras[23], "Submission Date", size=20, bold=True, space_after=2)
    set_para_text(paras[24], "14-08-2026", size=20, space_after=8)
    set_para_text(paras[26], f"Word Count: {wc}", size=16, bold=True, space_after=8)

    # Simple TOC in the empty TOC area
    set_para_text(paras[29], "Table of Contents", size=14, bold=True, space_after=8)
    toc_items = [
        "1. Introduction",
        "2. Development Overview",
        "3. System Design & Diagrams",
        "      Figure 4.1  Use Case Diagram",
        "      Figure 4.2  Flow Chart",
        "      Figure 4.3  Class Diagram",
        "4. Project File Structure",
        "      Figure 5.1  Project structure, schema, stack, and permissions",
        "5. Testing & Result",
        "6. Development Challenges & Decisions",
        "7. Conclusion",
        "8. References",
    ]
    p = paras[29]
    for item in toc_items:
        p = insert_after(p, item, size=11, space_after=2, align=WD_ALIGN_PARAGRAPH.LEFT, style="TOC Heading")

    # Section 1
    p = insert_after(paras[54], S1, size=11, space_after=10)
    insert_after(p, S1b, size=11, space_after=10)

    # Section 2 — replace placeholders
    set_para_text(paras[57], S2, size=11, space_after=10)
    paras[57].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    set_para_text(paras[58], S2b, size=11, space_after=10)
    paras[58].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    insert_after(paras[58], S2c, size=11, space_after=10)

    # Section 3
    set_para_text(paras[60], S3, size=11, space_after=10)
    paras[60].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p = insert_after(paras[60], S3b, size=11, space_after=10)

    set_para_text(paras[62], "Use Case Diagram", size=12, bold=True, space_after=4)
    set_para_text(
        paras[65],
        "Figure 4.1  Use case diagram of BlogVault, showing CRUD, search, media, share, and Pinterest upload.",
        size=10,
        italic=True,
        space_after=10,
        align=WD_ALIGN_PARAGRAPH.CENTER,
    )
    set_para_text(paras[68], "Flow Chart", size=12, bold=True, space_after=4)
    set_para_text(
        paras[71],
        "Figure 4.2  Operational flow of BlogVault from launch through save, search, share, multi-select, and Pinterest upload.",
        size=10,
        italic=True,
        space_after=10,
        align=WD_ALIGN_PARAGRAPH.CENTER,
    )
    set_para_text(paras[73], "Class Diagram", size=12, bold=True, space_after=4)
    set_para_text(
        paras[75],
        "Figure 4.3  Class diagram of the local SQLite database: blogvault.db, table messages, DatabaseHelper, MessageDao, and BlogMessage.",
        size=10,
        italic=True,
        space_after=10,
        align=WD_ALIGN_PARAGRAPH.CENTER,
    )

    # Section 4
    set_para_text(paras[77], S4, size=11, space_after=10)
    paras[77].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    set_para_text(
        paras[78],
        "Figure 5.1  Project packages, SQLite schema, technology stack, and runtime permissions.",
        size=10,
        italic=True,
        space_after=10,
        align=WD_ALIGN_PARAGRAPH.CENTER,
    )

    # Section 5
    set_para_text(paras[83], S5, size=11, space_after=8)
    paras[83].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    cases = [
        ("T01", "Create post", "Tap +, enter title/body, Save", "Post appears in the home list", "Saved to SQLite", "Pass"),
        ("T02", "Edit post", "Open detail, Edit, change text, Save", "Updated content shown", "Updated correctly", "Pass"),
        ("T03", "Search", "Open search, type a keyword", "Only matching title/body shown", "Background search works", "Pass"),
        ("T04", "Delete one post", "Detail menu → Delete", "Post removed from list and DB", "Deleted", "Pass"),
        ("T05", "Multi-select delete", "Long-press, select several, Delete", "Selected posts removed", "Bulk delete works", "Pass"),
        ("T06", "Gallery photo", "Edit → Gallery → pick image → Save", "Image shown and path stored", "Works", "Pass"),
        ("T07", "In-app camera", "Edit → Camera → shutter → Save", "Photo stored in app files", "Works on device", "Pass"),
        ("T08", "Share", "Detail → Share", "System share sheet opens", "ACTION_SEND works", "Pass"),
        ("T09", "Pinterest upload", "Detail → Upload to Pinterest", "Pinterest opens with image and caption", "Works if app installed", "Pass"),
        ("T10", "Multi-select upload", "Select several → Upload to Pinterest", "One collage, Pinterest opens once", "Collage then ACTION_SEND", "Pass"),
        ("T11", "Persistence", "Create posts, force-stop, reopen", "Posts still listed", "blogvault.db retains rows", "Pass"),
        ("T12", "No-photo upload", "Upload a text-only post", "Rendered JPEG sent to Pinterest", "Text-to-image works", "Pass"),
    ]
    table = insert_table_after(
        paras[83],
        ["ID", "Function", "Steps", "Expected", "Actual", "Status"],
        cases,
    )
    shade_status_pass(table)
    # outro after table: find the paragraph that followed 83 originally (heading 6)
    insert_after(paras[83], S5b, size=11, space_after=10)

    # Wait - insert_after(paras[83], S5b) inserts S5b immediately after 83, BEFORE the table
    # because table was addnext to 83 first, then S5b addnext to 83 puts S5b between 83 and table.
    # Order would be: S5, S5b, table. That's actually OK: intro, extra sentence, then table.
    # But I wanted: S5, table, S5b.
    # Fix: insert S5b after heading 6's previous empty para... 
    # Current sequence after my operations:
    # paras[83] = S5
    # then table was addnext(83) so 83 -> table
    # then insert_after(83, S5b) does 83.addnext(S5b) so 83 -> S5b -> table
    # Then heading 6 follows table. So order is S5, S5b, table, heading 6.
    # I'll move S5b to after the table by inserting after heading 6's preceding empty paras.
    # Simpler: put S5b content into paras[86] which is empty under challenges... no that's wrong section.
    #
    # Let's insert S5b after section 5 empty paras 80/81? Those are BEFORE heading 5.
    # After heading 6 is paras[84]. I'll insert S5b before heading 6 by using the table's next sibling.
    # Actually easiest: don't insert S5b after 83; put it in the empty paragraph after the table.
    # Looking at template: 83 testing text, 84 heading 6. Table is between 83 and 84.
    # I'll insert S5b after the table element.

    # Remove the S5b we just inserted in the wrong place? User would see intro, outro, table.
    # That's acceptable (outro then evidence table) but slightly odd.
    # I'll relocate: find S5b paragraph (next sibling of 83) and move after table.

    # Relocate S5b after table
    s5b_el = paras[83]._element.getnext()
    if s5b_el is not None and s5b_el.tag == qn("w:p"):
        parent = s5b_el.getparent()
        parent.remove(s5b_el)
        table._tbl.addnext(s5b_el)

    # Section 6
    set_para_text(paras[86], S6, size=11, space_after=10)
    paras[86].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p = insert_after(paras[86], S6b, size=11, space_after=10)
    insert_after(p, S6c, size=11, space_after=10)

    # Section 7
    p = insert_after(paras[88], S7, size=11, space_after=10)

    # Section 8 references
    refs = [
        "Android Developers, ‘Save data using SQLite’. Available at: https://developer.android.com/training/data-storage/sqlite (Accessed: 14 August 2026).",
        "Android Developers, ‘CameraX overview’. Available at: https://developer.android.com/camerax (Accessed: 14 August 2026).",
        "Android Developers, ‘Sending simple data to other apps’. Available at: https://developer.android.com/training/sharing/send (Accessed: 14 August 2026).",
        "Android Developers, ‘FileProvider’. Available at: https://developer.android.com/reference/androidx/core/content/FileProvider (Accessed: 14 August 2026).",
        "Android Developers, ‘Intents and intent filters’. Available at: https://developer.android.com/guide/components/intents-filters (Accessed: 14 August 2026).",
        "Material Design for Android. Available at: https://m3.material.io/develop/android (Accessed: 14 August 2026).",
        "Bumptech, ‘Glide’. Available at: https://github.com/bumptech/glide (Accessed: 14 August 2026).",
        "Pinterest, Pinterest Android application (opened via ACTION_SEND / com.pinterest). Available at: https://www.pinterest.com (Accessed: 14 August 2026).",
    ]
    rp = paras[92]
    for i, ref in enumerate(refs, start=1):
        rp = insert_after(rp, f"{i}.  {ref}", size=11, space_after=6, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Replace placeholder diagrams (0 = university banner, keep)
    w1, h1 = png_size_inches(p_use, 6.25)
    w2, h2 = png_size_inches(p_flow, 6.15)
    w3, h3 = png_size_inches(p_class, 6.25)
    w4, h4 = png_size_inches(p_struct, 6.25)
    print("Inline sizes (in):", (w1, h1), (w2, h2), (w3, h3), (w4, h4))
    print("inline_shapes", len(doc.inline_shapes))
    replace_inline_image(doc, 1, p_use, w1, h1)
    replace_inline_image(doc, 2, p_flow, w2, min(h2, 8.2))
    replace_inline_image(doc, 3, p_class, w3, h3)
    replace_inline_image(doc, 4, p_struct, w4, h4)

    update_footers(doc)

    doc.save(str(OUT_PRIMARY))
    doc.save(str(OUT_COPY))
    print("Saved", OUT_PRIMARY)
    print("Saved", OUT_COPY)
    print("Word count (sections 1-7):", wc)


if __name__ == "__main__":
    main()
