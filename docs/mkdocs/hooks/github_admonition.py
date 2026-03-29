import re

ADMONITION_TYPES = {
    "NOTE": "note",
    "TIP": "tip",
    "WARNING": "warning",
    "CAUTION": "danger",
    "IMPORTANT": "important",
}

PATTERN = re.compile(
    r"^([ \t]*)> \[!("
    + "|".join(ADMONITION_TYPES.keys())
    + r")\](.*?)$\n((?:\1>(?: .*)?$\n)*)",
    re.MULTILINE,
)


def on_page_markdown(markdown, **kwargs):
    def replace_block(match):
        indent = match.group(1)
        gh_type = match.group(2)
        title = match.group(3).strip()
        body_lines = match.group(4)

        mkdocs_type = ADMONITION_TYPES[gh_type]
        if title:
            header = f'{indent}!!! {mkdocs_type} "{title}"'
        else:
            header = f"{indent}!!! {mkdocs_type}"

        converted_lines = []
        for line in body_lines.split("\n"):
            if line.strip() == "":
                converted_lines.append("")
            else:
                content = re.sub(
                    r"^" + re.escape(indent) + r">\s?", "", line
                )
                converted_lines.append(f"{indent}    {content}")

        body = "\n".join(converted_lines).rstrip()
        return f"{header}\n{body}"

    return PATTERN.sub(replace_block, markdown)
