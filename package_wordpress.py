"""Export the inline-styled page for a WordPress Custom HTML block.

Uses only Python's standard library. Run from any working directory.
"""
from html.parser import HTMLParser
from pathlib import Path
import re


class BlockValidator(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in {"html", "head", "body", "style", "script", "link", "iframe"}:
            raise ValueError(f"Unexpected <{tag}> in WordPress content")
        if any(name.startswith("on") for name in attributes):
            raise ValueError("Event handlers are not supported")
        style = attributes.get("style", "")
        if not style or "var(" in style or "@media" in style:
            raise ValueError(f"<{tag}> must use self-contained inline styles")
        if tag == "a":
            self.links.append(attributes.get("href", ""))
        if "id" in attributes:
            if attributes["id"] in self.ids:
                raise ValueError(f"Duplicate ID: {attributes['id']}")
            self.ids.add(attributes["id"])
        self.labels.extend(attributes.get("aria-labelledby", "").split())

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.labels = []


def main():
    root = Path(__file__).resolve().parent
    page = (root / "index.html").read_text(encoding="utf-8")
    body = re.search(r"<body\b[^>]*>(.*?)</body\s*>", page, re.S | re.I)
    if body is None:
        raise ValueError("index.html must contain a body element")
    content = body.group(1).strip() + "\n"
    validator = BlockValidator()
    validator.feed(content)
    validator.close()
    references = [link[1:] for link in validator.links if link.startswith("#")]
    for reference in references + validator.labels:
        if reference not in validator.ids:
            raise ValueError(f"Missing anchor or accessible label: {reference}")
    output = root / "wordpress" / "custom-html.html"
    output.parent.mkdir(exist_ok=True)
    output.write_text(content, encoding="utf-8")
    print(f"Created {output} ({len(content.encode('utf-8')):,} bytes)")


if __name__ == "__main__":
    main()
