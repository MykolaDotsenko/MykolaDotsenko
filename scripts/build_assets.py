#!/usr/bin/env python3
"""Generate the profile README artwork in light and dark variants.

Visual language: fields, furrows, wheat and sprouts (agriculture) with a
light touch of Irish Celtic ornament (triquetra, interlaced plait bands).

Run from the repository root:  python3 scripts/build_assets.py
"""

from __future__ import annotations

import math
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": {
        "bg0": "#0E1512", "bg1": "#131D16", "card": "#152019", "card_hi": "#18261C",
        "stroke": "#2A3A2E", "grid": "#1C2820", "text": "#EEF2E6", "muted": "#9AA894",
        "label": "#A9C78F", "accent": "#8FBF73", "gold": "#D8B868", "soil": "#6E5438",
        "line": "#3E5341", "hill1": "#17261B", "hill2": "#1C2F20", "field": "#1A2A1D",
        "furrow": "#2C4230", "shadow": ".42", "glow": ".30",
    },
    "light": {
        "bg0": "#F8F6EC", "bg1": "#EEF2E3", "card": "#FFFEF8", "card_hi": "#F4F7EC",
        "stroke": "#D8DDC8", "grid": "#E7EADB", "text": "#1D2A1F", "muted": "#5F6B5C",
        "label": "#4F7A3D", "accent": "#5E8F48", "gold": "#A8822C", "soil": "#B89A72",
        "line": "#B9C6AE", "hill1": "#E3EAD3", "hill2": "#D6E2C4", "field": "#DCE6CB",
        "furrow": "#C2D1AE", "shadow": ".10", "glow": ".22",
    },
}

SANS = "ui-sans-serif,system-ui,-apple-system,Segoe UI,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Consolas,Menlo,monospace"
SERIF = "Georgia,Iowan Old Style,Palatino Linotype,Book Antiqua,serif"

REDUCED_MOTION = "<style>@media (prefers-reduced-motion: reduce) { .motion { display: none; } }</style>"


def f(v: float) -> str:
    return f"{v:.1f}".rstrip("0").rstrip(".")


def text(x, y, s, fill, size, family=SANS, weight=None, spacing=None, anchor=None, italic=False):
    attrs = [f'x="{f(x)}"', f'y="{f(y)}"', f'fill="{fill}"', f'font-family="{family}"', f'font-size="{size}"']
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if italic:
        attrs.append('font-style="italic"')
    return f"<text {' '.join(attrs)}>{s}</text>"


def svg(width, height, title, desc, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">\n'
        f'  <title id="title">{title}</title>\n  <desc id="desc">{desc}</desc>\n'
        f"  {REDUCED_MOTION}\n  <defs>{defs}</defs>\n{body}\n</svg>\n"
    )


# --- Ornaments -------------------------------------------------------------

def triquetra(cx, cy, r, stroke, width=2.0, ring=True, ring_stroke=None):
    """Three interlaced vesica lobes, optionally with a ring (Celtic trinity knot)."""
    parts = []
    if ring:
        parts.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.56)}" fill="none" '
                     f'stroke="{ring_stroke or stroke}" stroke-width="{f(width * 0.8)}"/>')
    for k in range(3):
        a = math.radians(-90 + 120 * k)
        tx, ty = cx + r * math.cos(a), cy + r * math.sin(a)
        parts.append(
            f'<path d="M{f(cx)} {f(cy)}A{f(r)} {f(r)} 0 0 1 {f(tx)} {f(ty)}'
            f'A{f(r)} {f(r)} 0 0 1 {f(cx)} {f(cy)}Z" fill="none" stroke="{stroke}" '
            f'stroke-width="{f(width)}" stroke-linejoin="round"/>'
        )
    return "".join(parts)


def plait(uid, x1, x2, y, amp, period, stroke, width, gap=3.0, fade=True):
    """Two-strand Celtic plait with real over/under crossings (via masks, so it
    works on any background)."""
    n = max(8, int((x2 - x1) / 3))

    def pts(sign, a, b):
        out = []
        steps = max(4, int((b - a) / 3))
        for i in range(steps + 1):
            x = a + (b - a) * i / steps
            out.append((x, y + sign * amp * math.sin(2 * math.pi * (x - x1) / period)))
        return "M" + "L".join(f"{f(px)} {f(py)}" for px, py in out)

    strands = {1: pts(1, x1, x2), -1: pts(-1, x1, x2)}
    over = {1: [], -1: []}
    half = period / 2
    i, cross = 0, x1 + half
    while cross < x2 - 1:
        s = 1 if i % 2 == 0 else -1
        a, b = max(x1, cross - period * 0.16), min(x2, cross + period * 0.16)
        over[s].append(pts(s, a, b))
        cross += half
        i += 1
    defs = []
    if fade:
        defs.append(
            f'<linearGradient id="{uid}g" gradientUnits="userSpaceOnUse" x1="{f(x1)}" y1="0" x2="{f(x2)}" y2="0">'
            f'<stop offset="0" stop-color="{stroke}" stop-opacity="0"/>'
            f'<stop offset=".2" stop-color="{stroke}"/><stop offset=".8" stop-color="{stroke}"/>'
            f'<stop offset="1" stop-color="{stroke}" stop-opacity="0"/></linearGradient>'
        )
    paint = f"url(#{uid}g)" if fade else stroke
    body = []
    for s in (1, -1):
        other = -s
        mid = f"{uid}m{'a' if s == 1 else 'b'}"
        cut = "".join(
            f'<path d="{d}" fill="none" stroke="#000" stroke-width="{f(width + 2 * gap)}" stroke-linecap="butt"/>'
            for d in over[other]
        )
        defs.append(
            f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="{f(x1 - 10)}" y="{f(y - amp - 20)}" '
            f'width="{f(x2 - x1 + 20)}" height="{f(2 * amp + 40)}">'
            f'<rect x="{f(x1 - 10)}" y="{f(y - amp - 20)}" width="{f(x2 - x1 + 20)}" height="{f(2 * amp + 40)}" fill="#fff"/>'
            f"{cut}</mask>"
        )
        body.append(
            f'<path d="{strands[s]}" fill="none" stroke="{paint}" stroke-width="{f(width)}" '
            f'stroke-linecap="round" mask="url(#{mid})"/>'
        )
    del n
    return "".join(defs), "".join(body)


def wheat(x, y, h, angle, stem, grain, awn=True, grains=6):
    """A wheat ear standing at (x, y), height h, rotated by angle degrees."""
    g = [f'<g transform="translate({f(x)} {f(y)}) rotate({f(angle)})">']
    g.append(f'<path d="M0 0C1 {f(-h * .35)} 0 {f(-h * .7)} 0 {f(-h)}" fill="none" stroke="{stem}" stroke-width="1.6" stroke-linecap="round"/>')
    head0 = h * 0.45
    step = (h - head0) / grains
    for i in range(grains):
        yy = -(head0 + i * step)
        for side in (-1, 1):
            g.append(
                f'<ellipse cx="{f(side * 3.4)}" cy="{f(yy)}" rx="2.6" ry="5.4" fill="{grain}" '
                f'transform="rotate({f(side * 24)} {f(side * 3.4)} {f(yy)})"/>'
            )
            if awn:
                g.append(f'<path d="M{f(side * 4.6)} {f(yy - 4)}L{f(side * 9.5)} {f(yy - 15)}" stroke="{grain}" stroke-width=".8" opacity=".75"/>')
    g.append(f'<ellipse cx="0" cy="{f(-h - 2)}" rx="2.4" ry="5" fill="{grain}"/>')
    g.append("</g>")
    return "".join(g)


def sprout(x, y, s, stem, leaf):
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})">'
        f'<path d="M0 10V-4" stroke="{stem}" stroke-width="1.8" stroke-linecap="round"/>'
        f'<path d="M0 -2C-2 -10 -9 -12 -13 -10C-12 -4 -6 -1 0 -2Z" fill="{leaf}"/>'
        f'<path d="M0 -4C2 -13 9 -16 14 -13C13 -6 6 -3 0 -4Z" fill="{leaf}"/>'
        f'<path d="M-8 10H8" stroke="{stem}" stroke-width="1.6" stroke-linecap="round" opacity=".7"/>'
        f"</g>"
    )


def seed(x, y, s, fill, soil):
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})">'
        f'<path d="M-14 8C-7 4 7 4 14 8" fill="none" stroke="{soil}" stroke-width="1.8" stroke-linecap="round"/>'
        f'<ellipse cx="-5" cy="-2" rx="3.2" ry="4.6" fill="{fill}" transform="rotate(-25 -5 -2)"/>'
        f'<ellipse cx="4" cy="-4" rx="3.2" ry="4.6" fill="{fill}" transform="rotate(20 4 -4)"/>'
        f'<ellipse cx="0" cy="4" rx="3" ry="4.2" fill="{fill}" opacity=".8"/>'
        f"</g>"
    )


def roots(x, y, s, c):
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})" fill="none" stroke="{c}" stroke-width="1.7" stroke-linecap="round">'
        f'<path d="M-12 -8H12"/><path d="M0 -8V2C0 6 -4 8 -8 11"/><path d="M0 2C0 6 4 8 9 10"/>'
        f'<path d="M0 0C-3 3 -8 3 -12 5"/><path d="M0 -2C3 1 8 1 12 2"/><path d="M0 4V13"/></g>'
    )


def leaf(x, y, s, c, vein):
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})">'
        f'<path d="M-12 10C-12 -6 0 -12 12 -12C12 2 4 12 -12 10Z" fill="{c}"/>'
        f'<path d="M-10 8C-4 2 2 -4 9 -9" stroke="{vein}" stroke-width="1.3" fill="none" stroke-linecap="round"/></g>'
    )


def soil_layers(x, y, s, a, b):
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})" fill="none" stroke-linecap="round" stroke-width="2">'
        f'<path d="M-13 -7C-6 -10 6 -4 13 -7" stroke="{a}"/>'
        f'<path d="M-13 0C-6 -3 6 3 13 0" stroke="{b}"/>'
        f'<path d="M-13 7C-6 4 6 10 13 7" stroke="{a}"/></g>'
    )


def sun(x, y, s, c):
    rays = "".join(
        f'<path d="M{f(11 * math.cos(math.radians(a)))} {f(11 * math.sin(math.radians(a)))}'
        f'L{f(15 * math.cos(math.radians(a)))} {f(15 * math.sin(math.radians(a)))}"/>'
        for a in range(0, 360, 45)
    )
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})" fill="none" stroke="{c}" stroke-width="1.7" stroke-linecap="round">'
        f'<circle r="6.5"/>{rays}</g>'
    )


def pine(x, y, s, c, trunk):
    return (
        f'<g transform="translate({f(x)} {f(y)}) scale({s})">'
        f'<path d="M0 -14L7 -4H3L9 5H-9L-3 -4H-7Z" fill="{c}"/>'
        f'<path d="M0 5V11" stroke="{trunk}" stroke-width="2" stroke-linecap="round"/></g>'
    )


def card_bg(t, x, y, w, h, rx, uid):
    return (
        f'<linearGradient id="{uid}" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{t["bg0"]}"/><stop offset="1" stop-color="{t["bg1"]}"/></linearGradient>'
        f'<filter id="{uid}s" x="-10%" y="-20%" width="120%" height="150%">'
        f'<feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#000" flood-opacity="{t["shadow"]}"/></filter>'
        f'<clipPath id="{uid}c"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>'
    )


def outer(x, y, w, h, rx, uid, t):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#{uid})" filter="url(#{uid}s)"/>'
        f'<rect x="{x + .5}" y="{y + .5}" width="{w - 1}" height="{h - 1}" rx="{rx - .5}" fill="none" stroke="{t["stroke"]}"/>'
    )


def corner_knots(t, x, y, w, h, inset=26, r=7):
    return "".join(
        f'<g opacity=".7">{triquetra(cx, cy, r, t["line"], 1.2, ring=False)}</g>'
        for cx, cy in ((x + inset, y + inset), (x + w - inset, y + inset))
    )


# --- Landscape helpers -----------------------------------------------------

def crest_y(x):
    return 232 - 22 * math.sin((x - 700) / 95) - 12 * math.sin((x - 700) / 41 + 1.3)


def poly(fn, a, b, step=4):
    xs = [a + i * step for i in range(int((b - a) / step) + 1)] + [b]
    return "L".join(f"{f(x)} {f(fn(x))}" for x in xs)


# --- Assets ----------------------------------------------------------------

def hero(t):
    W, H = 1200, 360
    defs = card_bg(t, 18, 18, 1164, 324, 28, "bg")
    defs += (
        f'<radialGradient id="sunGlow" cx="1088" cy="96" r="150" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="{t["gold"]}" stop-opacity="{t["glow"]}"/>'
        f'<stop offset="1" stop-color="{t["gold"]}" stop-opacity="0"/></radialGradient>'
        f'<linearGradient id="fieldFade" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".34" stop-color="#fff"/>'
        f'<stop offset="1" stop-color="#fff"/></linearGradient>'
        f'<mask id="fade" maskUnits="userSpaceOnUse" x="600" y="18" width="582" height="324">'
        f'<rect x="600" y="18" width="582" height="324" fill="url(#fieldFade)"/></mask>'
        f'<filter id="glow" x="-300%" y="-300%" width="700%" height="700%"><feGaussianBlur stdDeviation="3.5" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    )
    front = f"M600 {f(crest_y(600))}L{poly(crest_y, 600, 1182)}L1182 342L600 342Z"
    defs += f'<clipPath id="frontField"><path d="{front}"/></clipPath>'

    vx, vy = 960, crest_y(960) - 6
    furrows = "".join(
        f'<path d="M{f(vx)} {f(vy)}L{f(bx)} 360" stroke="{t["furrow"]}" stroke-width="{f(1.2 + abs(bx - vx) / 260)}"/>'
        for bx in range(420, 1560, 46)
    )
    rows = "".join(
        f'<path d="M640 {f(yy)}L1182 {f(yy)}" stroke="{t["furrow"]}" stroke-width=".8" opacity=".55"/>'
        for yy in (262, 280, 302, 330)
    )
    back_hill = (
        f'<path d="M600 214C690 170 780 150 870 170C950 188 1010 150 1090 138C1130 132 1160 136 1182 142V342H600Z" fill="{t["hill1"]}"/>'
        f'<path d="M640 238C720 200 800 196 880 212C960 228 1040 196 1120 178C1150 172 1170 172 1182 174V342H640Z" fill="{t["hill2"]}" opacity=".9"/>'
    )
    nodes = [(760, "BACKEND"), (846, "FRONTEND"), (932, "DATA"), (1012, "AI"), (1100, "AGRITECH")]
    signal = f"M700 {f(crest_y(700))}L{poly(crest_y, 700, 1160)}"
    node_svg = []
    for i, (nx, lab) in enumerate(nodes):
        ny = crest_y(nx)
        fill = t["gold"] if lab == "AGRITECH" else t["accent"]
        node_svg.append(f'<path d="M{nx} {f(ny - 7)}V{f(ny - 18)}" stroke="{t["line"]}" stroke-width="1"/>')
        node_svg.append(f'<circle cx="{nx}" cy="{f(ny)}" r="4.6" fill="{fill}"/>')
        node_svg.append(text(nx, ny - 24, lab, t["muted"], 9.5, MONO, spacing=1.1, anchor="middle"))
        del i

    wheats = "".join(
        wheat(x, 346, h, a, t["soil"], t["gold"]) for x, h, a in
        ((1118, 88, -8), (1134, 104, 3), (1150, 92, 12), (1166, 78, 20), (1102, 72, -18))
    )
    band_defs, band = plait("hb", 72, 520, 322, 4.2, 26, t["line"], 1.6, gap=2.4)
    defs += band_defs

    body = f"""  {outer(18, 18, 1164, 324, 28, "bg", t)}
  <g clip-path="url(#bgc)">
    <rect x="740" y="-40" width="480" height="300" fill="url(#sunGlow)"/>
    <g mask="url(#fade)">{back_hill}
      <g clip-path="url(#frontField)"><rect x="600" y="150" width="600" height="200" fill="{t["field"]}"/>{furrows}{rows}</g>
      <path id="signalPath" d="{signal}" fill="none" stroke="{t["accent"]}" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>
    </g>
    <g>{triquetra(1088, 96, 34, t["gold"], 2.2)}</g>
    <circle cx="1088" cy="96" r="44" fill="none" stroke="{t["gold"]}" stroke-width="1" opacity=".45"/>
    {"".join(node_svg)}
    <circle class="motion" r="3.6" fill="{t["gold"]}" filter="url(#glow)">
      <animateMotion dur="7s" repeatCount="indefinite"><mpath href="#signalPath"/></animateMotion>
    </circle>
    {wheats}
    <rect x="716" y="274" width="316" height="52" rx="12" fill="{t["card"]}" fill-opacity=".94" stroke="{t["stroke"]}"/>
    {text(734, 295, "ENGINEERING SIGNAL", t["label"], 10, MONO, spacing=1.5)}
    {text(734, 315, "reliable systems → useful decisions", t["text"], 14, SANS, 650)}

    {text(72, 82, "SOFTWARE ENGINEER · FINLAND", t["label"], 14.5, SANS, 750, 3.2)}
    <text x="72" y="140" fill="{t["text"]}" font-family="{SERIF}" font-size="38" font-weight="700">
      <tspan x="72" dy="0">I build trustworthy software</tspan>
      <tspan x="72" dy="46">for messy reality.</tspan>
    </text>
    {text(72, 240, "Python / Django · React / Next.js · Data · AI Integrations", t["text"], 17.5, SANS, 500)}
    {text(72, 272, "backend depth · frontend delivery · data discipline · AgriTech perspective", t["muted"], 14.5)}
    {band}
  </g>"""
    return svg(W, H, "Mykola Dotsenko — Software Engineer",
               "Banner with a field landscape, furrows, wheat and a Celtic triquetra sun; backend, frontend, data, AI "
               "and AgriTech are marked along the horizon.", body, defs)


def divider(t):
    W, H = 1200, 80
    d1, b1 = plait("dl", 40, 520, 40, 7, 34, t["accent"], 2.0, gap=2.6)
    d2, b2 = plait("dr", 680, 1160, 40, 7, 34, t["accent"], 2.0, gap=2.6)
    body = f"""  {b1}{b2}
  <circle cx="600" cy="40" r="30" fill="none" stroke="{t["gold"]}" stroke-width="1.4" opacity=".55"/>
  {triquetra(600, 40, 24, t["gold"], 2.2, ring_stroke=t["accent"])}
  {wheat(548, 58, 34, -62, t["soil"], t["gold"], grains=4)}
  {wheat(652, 58, 34, 62, t["soil"], t["gold"], grains=4)}"""
    return svg(W, H, "Celtic knot and wheat divider",
               "An interlaced Celtic plait with a triquetra and two wheat ears at the centre.", body, d1 + d2)


def production_flow(t):
    W, H = 1200, 290
    defs = card_bg(t, 18, 18, 1164, 254, 26, "bg")
    defs += (
        f'<filter id="glow" x="-300%" y="-300%" width="700%" height="700%"><feGaussianBlur stdDeviation="3.5" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    )
    cards = [
        (40, "MESSY INPUTS · SOIL", ["APIs · legacy systems", "real users"],
         ["stale data · duplicates · missing state", "conflicting ownership · imperfect workflows"],
         seed(352, 110, 1.1, t["gold"], t["soil"]), False),
        (425, "ENGINEERING · GROWTH", ["rules · state", "evidence · UX"],
         ["source of truth · retries · validation", "loading/error states · fallbacks · observability"],
         sprout(737, 112, 1.2, t["soil"], t["accent"]), True),
        (810, "USEFUL OUTPUT · HARVEST", ["clear interfaces", "reliable workflows"],
         ["understandable state · safer decisions", "software people can actually trust"],
         wheat(1118, 138, 30, 14, t["soil"], t["gold"], grains=4), False),
    ]
    out = []
    for x, lab, titles, subs, icon, hi in cards:
        stroke = t["accent"] if hi else t["stroke"]
        out.append(f'<rect x="{x}" y="86" width="350" height="156" rx="18" fill="{t["card_hi"] if hi else t["card"]}" '
                   f'stroke="{stroke}" stroke-opacity="{".7" if hi else "1"}"/>')
        out.append(text(x + 24, 116, lab, t["label"], 10.5, MONO, spacing=1.6))
        out.append(text(x + 24, 148, titles[0], t["text"], 19, SANS, 720))
        out.append(text(x + 24, 172, titles[1], t["text"], 19, SANS, 720))
        out.append(text(x + 24, 202, subs[0], t["muted"], 11.5))
        out.append(text(x + 24, 222, subs[1], t["muted"], 11.5))
        out.append(icon)
    links = (
        f'<path id="flow1" d="M390 164H425" stroke="{t["line"]}" stroke-width="2" stroke-dasharray="3 4"/>'
        f'<path id="flow2" d="M775 164H810" stroke="{t["line"]}" stroke-width="2" stroke-dasharray="3 4"/>'
        f'<circle class="motion" r="3.6" fill="{t["gold"]}" filter="url(#glow)"><animateMotion dur="2.6s" repeatCount="indefinite"><mpath href="#flow1"/></animateMotion></circle>'
        f'<circle class="motion" r="3.6" fill="{t["gold"]}" filter="url(#glow)"><animateMotion dur="2.6s" begin="-1.3s" repeatCount="indefinite"><mpath href="#flow2"/></animateMotion></circle>'
    )
    bd, band = plait("pb", 520, 1150, 55, 3.6, 24, t["line"], 1.4, gap=2.2)
    body = f"""  {outer(18, 18, 1164, 254, 26, "bg", t)}
  <g clip-path="url(#bgc)">
    {text(42, 60, "PRODUCTION LENS / TURNING MESSY REALITY INTO USEFUL SOFTWARE", t["muted"], 10.8, MONO, spacing=2)}
    {band}
    {"".join(out)}
    {links}
  </g>"""
    return svg(W, H, "Production engineering flow",
               "Messy inputs (soil) move through engineering rules and state handling (growth) into clear interfaces "
               "and reliable workflows (harvest).", body, defs + bd)


def capability_map(t):
    W, H = 1200, 340
    defs = card_bg(t, 18, 18, 1164, 304, 26, "bg")
    defs += (
        f'<filter id="glow" x="-300%" y="-300%" width="700%" height="700%"><feGaussianBlur stdDeviation="3.5" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        f'<clipPath id="agri"><rect x="650" y="88" width="508" height="212" rx="20"/></clipPath>'
    )
    small = [
        (46, 88, "BACKEND · ROOTS", "Python · Django · DRF", "rules · APIs · reliability", roots(282, 108, 1, t["soil"])),
        (330, 88, "FRONTEND · LEAVES", "React · Next.js · TS", "UI states · flows · localization", leaf(566, 110, .9, t["accent"], t["card"])),
        (46, 210, "DATA SYSTEMS · SOIL", "PostgreSQL · SQL · ETL", "identity · sync · validation", soil_layers(282, 230, 1, t["soil"], t["accent"])),
        (330, 210, "AI &amp; INTEGRATIONS · SUN", "APIs · AI-enabled flows", "automation · evidence · fallbacks", sun(566, 230, 1, t["gold"])),
    ]
    out = []
    for x, y, lab, title, sub, icon in small:
        out.append(f'<rect x="{x}" y="{y}" width="262" height="90" rx="16" fill="{t["card"]}" stroke="{t["stroke"]}"/>')
        out.append(text(x + 20, y + 28, lab, t["label"], 10.5, MONO, spacing=1.4))
        out.append(text(x + 20, y + 56, title, t["text"], 16, SANS, 700))
        out.append(text(x + 20, y + 76, sub, t["muted"], 12))
        out.append(icon)

    strip_y = lambda x: 272 - 9 * math.sin((x - 650) / 70) - 5 * math.sin((x - 650) / 29)  # noqa: E731
    strip = f"M650 {f(strip_y(650))}L{poly(strip_y, 650, 1158)}L1158 300L650 300Z"
    furrows = "".join(
        f'<path d="M905 262L{bx} 310" stroke="{t["furrow"]}" stroke-width="1.2"/>' for bx in range(560, 1260, 40)
    )
    agri = f"""<rect x="650" y="88" width="508" height="212" rx="20" fill="{t["card_hi"]}" stroke="{t["accent"]}" stroke-opacity=".7"/>
    <g clip-path="url(#agri)">
      <path d="{strip}" fill="{t["field"]}"/>
      <clipPath id="strip"><path d="{strip}"/></clipPath>
      <g clip-path="url(#strip)">{furrows}</g>
      {wheat(1110, 300, 58, -6, t["soil"], t["gold"], grains=5)}{wheat(1126, 300, 68, 6, t["soil"], t["gold"], grains=5)}{wheat(1140, 300, 52, 16, t["soil"], t["gold"], grains=4)}
    </g>
    {triquetra(1124, 120, 14, t["gold"], 1.6)}
    {text(676, 120, "AGRITECH / DECISION SOFTWARE", t["label"], 10.5, MONO, spacing=1.8)}
    {text(676, 156, "Real data → useful action", t["text"], 24, SERIF, 700)}
    {text(676, 186, "Production · Revenue · Operations · Finance", t["text"], 14)}
    {text(676, 208, "Intelligence · Trade · explainable decisions", t["text"], 14)}
    {text(676, 236, "reliable state · clear UI · explicit evidence · measurable value", t["muted"], 9.8, MONO)}"""

    routes = [
        ("r1", "M308 133H330"), ("r2", "M308 255H330"),
        ("r3", "M592 133C622 133 622 180 650 186"), ("r4", "M592 255C622 255 622 206 650 200"),
    ]
    rt = "".join(f'<path id="{i}" d="{d}" fill="none" stroke="{t["line"]}" stroke-width="2" stroke-dasharray="3 4"/>' for i, d in routes)
    dots = "".join(
        f'<circle class="motion" r="3.4" fill="{t["gold"]}" filter="url(#glow)"><animateMotion dur="{dur}s" begin="{b}s" '
        f'repeatCount="indefinite"><mpath href="#{i}"/></animateMotion></circle>'
        for (i, _), dur, b in zip(routes, (2.4, 2.8, 3.2, 3.6), (0, -.9, -1.6, -.4))
    )
    body = f"""  {outer(18, 18, 1164, 304, 26, "bg", t)}
  <g clip-path="url(#bgc)">
    {text(46, 60, "ENGINEERING MAP / ROOTS, LEAVES, SOIL AND SUN FEED THE CROP", t["muted"], 10.8, MONO, spacing=2)}
    {rt}{"".join(out)}{agri}{dots}
  </g>"""
    return svg(W, H, "Engineering capability map",
               "Backend (roots), frontend (leaves), data systems (soil) and AI integrations (sun) feed AgriTech "
               "decision software.", body, defs)


def current_focus(t):
    W, H = 1200, 210
    defs = card_bg(t, 18, 18, 1164, 174, 22, "bg")
    bd, band = plait("fb", 420, 1150, 78, 4, 26, t["line"], 1.4, gap=2.2)
    cols = [
        (48, "WORK", "Production software", "backend · frontend · data", sprout(290, 118, .8, t["soil"], t["accent"])),
        (336, "STUDY", "MSc Software Engineering", "decision support · forecasting", seed(578, 118, .8, t["gold"], t["soil"])),
        (624, "CLOUD", "AWS architecture", "Solutions Architect Associate", sun(866, 118, .85, t["gold"])),
        (912, "FINLAND", "Finnish", "work · study · daily life", pine(1152, 118, 1, t["accent"], t["soil"])),
    ]
    out = []
    for x, lab, title, sub, icon in cols:
        out.append(text(x, 124, lab, t["label"], 10.5, MONO, spacing=1.5))
        out.append(text(x, 152, title, t["text"], 16, SANS, 700))
        out.append(text(x, 174, sub, t["muted"], 12.5))
        out.append(icon)
    seps = "".join(f'<path d="M{x} 110V178" stroke="{t["stroke"]}"/>' for x in (318, 606, 894))
    body = f"""  {outer(18, 18, 1164, 174, 22, "bg", t)}
  <g clip-path="url(#bgc)">
    {text(48, 58, "NOW / 2026", t["label"], 11, MONO, spacing=2.4)}
    {text(48, 88, "building while learning", t["text"], 22, SERIF, 700)}
    {band}{seps}{"".join(out)}
  </g>"""
    return svg(W, H, "Current focus",
               "Current focus: production software, MSc Software Engineering, AWS architecture (Solutions Architect "
               "Associate) and Finnish.", body, defs + bd)


def main():
    builders = {
        "profile-hero": hero, "celtic-divider": divider, "production-flow": production_flow,
        "capability-map": capability_map, "current-focus": current_focus,
    }
    for name, fn in builders.items():
        for theme, tokens in THEMES.items():
            (ASSETS / f"{name}-{theme}.svg").write_text(fn(tokens), encoding="utf-8")
            print(f"wrote assets/{name}-{theme}.svg")


if __name__ == "__main__":
    main()
