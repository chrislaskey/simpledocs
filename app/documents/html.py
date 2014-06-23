from markdown import markdown


def from_markdown(unicode_text):
    options = {
        "output_format": "html5",
        "safe_mode": "escape"
    }
    as_html = markdown(unicode_text, **options)
    return as_html
