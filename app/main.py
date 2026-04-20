import sys
import os
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services import get_random_fact
from utils import wrap_text, calculate_svg_height, escape_xml


# ── Palette ────────────────────────────────────────────────────────────────
VOID_BLACK      = "#0a0a0a"
TERMINAL_WHITE  = "#e8e8e8"
DIM_SILVER      = "#a0a0a0"
GHOST_WHITE     = "#f0f0f0"
GRID_COLOR      = "#161616"
ACCENT_LINE     = "#c0c0c0"
BORDER_COLOR    = "#2a2a2a"


def build_svg(fact: str) -> str:
    lines   = wrap_text(fact)
    height  = calculate_svg_height(len(lines))
    width   = 740
    now_utc = datetime.now(timezone.utc).strftime("%d %b %Y · %H:%M UTC")

    text_lines_svg = ""
    y_start = 88
    for i, line in enumerate(lines):
        y = y_start + i * 22
        text_lines_svg += (
            f'    <text x="36", y="{y}" '
            f'font-family="'Courier New', Courier, monospace" '
            f'font-size="13.5" fill="{GHOST_WHITE}" '
            f'letter-spacing="0.3">{escape_xml(line)}</text>\n'
        )

    bottom_y = height - 18

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="{GRID_COLOR}" stroke-width="0.4"/>
    </pattern>

    <filter id="silver-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="text-glow" x="-5%" y="-5%" width="110%" height="110%">
      <feGaussianBlur stdDeviation="1" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <linearGradient id="fade-bottom" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{VOID_BLACK}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{VOID_BLACK}" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="top-bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{TERMINAL_WHITE}" stop-opacity="0.1"/>
      <stop offset="30%" stop-color="{TERMINAL_WHITE}" stop-opacity="1"/>
      <stop offset="70%" stop-color="{TERMINAL_WHITE}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{TERMINAL_WHITE}" stop-opacity="0.1"/>
    </linearGradient>
  </defs>

  <!-- Void black base -->
  <rect width="{width}" height="{height}" fill="{VOID_BLACK}" rx="10"/>

  <!-- Grid texture -->
  <rect width="{width}" height="{height}" fill="url(#grid)" rx="10" opacity="1"/>

  <!-- Silver top border bar with fade -->
  <rect x="0" y="0" width="{width}" height="2" fill="url(#top-bar)" rx="2"/>

  <!-- Left accent stripe -->
  <rect x="0" y="2" width="2" height="{height - 2}" fill="{TERMINAL_WHITE}" opacity="0.08"/>

  <!-- Right accent stripe -->
  <rect x="{width - 2}" y="2" width="2" height="{height - 2}" fill="{TERMINAL_WHITE}" opacity="0.04"/>

  <!-- Corner bracket top-left -->
  <path d="M 18 14 L 18 26 L 30 26" fill="none" stroke="{TERMINAL_WHITE}" stroke-width="1.6" stroke-linecap="square" filter="url(#silver-glow)"/>

  <!-- Corner bracket top-right -->
  <path d="M {width - 18} 14 L {width - 18} 26 L {width - 30} 26" fill="none" stroke="{TERMINAL_WHITE}" stroke-width="1.6" stroke-linecap="square" filter="url(#silver-glow)"/>

  <!-- Corner bracket bottom-left -->
  <path d="M 18 {height - 14} L 18 {height - 26} L 30 {height - 26}" fill="none" stroke="{TERMINAL_WHITE}" stroke-width="1.6" stroke-linecap="square" opacity="0.35"/>

  <!-- Corner bracket bottom-right -->
  <path d="M {width - 18} {height - 14} L {width - 18} {height - 26} L {width - 30} {height - 26}" fill="none" stroke="{TERMINAL_WHITE}" stroke-width="1.6" stroke-linecap="square" opacity="0.35"/>

  <!-- Header label -->
  <text x="36" y="34"
    font-family="'Courier New', Courier, monospace"
    font-size="10" font-weight="bold"
    fill="{TERMINAL_WHITE}" letter-spacing="4"
    filter="url(#silver-glow)">TRIVIA_PULSE</text>

  <!-- Blinking cursor dot -->
  <circle cx="148" cy="30" r="2.5" fill="{TERMINAL_WHITE}" filter="url(#silver-glow)">
    <animate attributeName="opacity" values="1;0;1" dur="1.4s" repeatCount="indefinite"/>
  </circle>

  <!-- System tag right side -->
  <text x="{width - 36}" y="34"
    font-family="'Courier New', Courier, monospace"
    font-size="9" fill="{DIM_SILVER}"
    text-anchor="end" letter-spacing="1" opacity="0.6">SYS::RANDOM_FACT</text>

  <!-- Separator line -->
  <line x1="36" y1="46" x2="{width - 36}" y2="46"
    stroke="{ACCENT_LINE}" stroke-width="0.5" opacity="0.3"/>

  <!-- Prompt character -->
  <text x="36" y="72"
    font-family="'Courier New', Courier, monospace"
    font-size="12" fill="{TERMINAL_WHITE}"
    filter="url(#text-glow)">~/fact $</text>

  <!-- Fact text lines -->
{text_lines_svg}
  <!-- Bottom fade overlay -->
  <rect x="0" y="{height - 40}" width="{width}" height="40" fill="url(#fade-bottom)" rx="10"/>

  <!-- Bottom separator -->
  <line x1="36" y1="{bottom_y - 10}" x2="{width - 36}" y2="{bottom_y - 10}"
    stroke="{ACCENT_LINE}" stroke-width="0.5" opacity="0.15"/>

  <!-- Timestamp -->
  <text x="36" y="{bottom_y}"
    font-family="'Courier New', Courier, monospace"
    font-size="9" fill="{DIM_SILVER}"
    letter-spacing="1" opacity="0.5">UPDATED :: {now_utc}</text>

  <!-- Source tag -->
  <text x="{width - 36}" y="{bottom_y}"
    font-family="'Courier New', Courier, monospace"
    font-size="9" fill="{DIM_SILVER}"
    text-anchor="end" letter-spacing="1" opacity="0.4">uselessfacts.jsph.pl</text>
</svg>"""

    return svg


def main():
    print("trivia-pulse: fetching fact...")
    fact = get_random_fact()
    print(f"   -> {fact[:72]}{'...' if len(fact) > 72 else ''}")

    svg_content = build_svg(fact)

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "fact.svg"
    )
    output_path = os.path.normpath(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"   -> SVG written to {output_path}")
    print("Done.")


if __name__ == "__main__":
    main()