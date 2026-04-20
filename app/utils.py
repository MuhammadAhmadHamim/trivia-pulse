import textwrap


def wrap_text(text: str, max_chars: int = 68) -> list[str]:
    """
    Wrap fact text into lines that fit within the SVG width.
    Returns a list of string lines.
    """
    text = text.strip()
    if not text.endswith("."):
        text += "."
    wrapped = textwrap.wrap(text, width=max_chars)
    return wrapped


def calculate_svg_height(line_count: int) -> int:
    """
    Dynamically calculate SVG height based on number of text lines.
    Base height accounts for header, padding, and footer elements.
    """
    base_height = 110
    line_height = 22
    return base_height + (line_count * line_height)


def escape_xml(text: str) -> str:
    """
    Escape special XML/SVG characters in fact text.
    """
    return (
        text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )