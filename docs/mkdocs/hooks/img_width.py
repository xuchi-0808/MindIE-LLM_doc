import re

IMG_PATTERN = re.compile(
    r"<img\s+([^>]*?)>",
    re.MULTILINE,
)

ATTR_PATTERNS = {
    "src": re.compile(r'src=["\']([^"\']*)["\']'),
    "alt": re.compile(r'alt=["\']([^"\']*)["\']'),
    "width": re.compile(r'width=["\']([^"\']*)["\']'),
}


def on_page_markdown(markdown, **kwargs):
    def replace_img(match):
        attrs_str = match.group(1)

        src_match = ATTR_PATTERNS["src"].search(attrs_str)
        alt_match = ATTR_PATTERNS["alt"].search(attrs_str)
        width_match = ATTR_PATTERNS["width"].search(attrs_str)

        if not src_match:
            return match.group(0)

        src = src_match.group(1)
        alt = alt_match.group(1) if alt_match else ""
        width = width_match.group(1) if width_match else None

        if width:
            return f'![{alt}]({src}){{ width="{width}" }}'
        return f"![{alt}]({src})"

    return IMG_PATTERN.sub(replace_img, markdown)
