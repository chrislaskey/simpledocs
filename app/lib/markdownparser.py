from markdown import markdown


class MarkdownParser:

    def __init__(self, custom_options=None):
        self.options = self._get_default_options()
        if custom_options:
            self.options = self.options.update(custom_options)

    def _get_default_options(self):
        options = {
            "output_format": "html5",
            "safe_mode": "escape"
        }
        return options

    def parse(self, unicode_text):
        parsed_html = markdown(unicode_text, **self.options)
        return parsed_html
