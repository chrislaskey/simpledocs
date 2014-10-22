import re
from .. import app


class PageTitle:

    def get(self, uri_segments):
        sections = self._process_page_title_segments(uri_segments)
        sections.insert(0, app.config["HEADER_TITLE"])
        if not sections:
            return 'Home'
        elif len(sections) > 1:
            return ' | '.join(sections)
        else:
            return sections[0]

    def _process_page_title_segments(self, uri_segments):
        sections = []
        for piece in uri_segments:
            stripped = self._strip_numeric_prefix(piece)
            title = self._create_title_from_slug(stripped)
            sections.append(title)
        sections.reverse()
        return sections

    def _strip_numeric_prefix(self, text):
        stripped = re.sub(r'^[0-9_-]*(.*)', r'\1', text)
        return stripped

    def _create_title_from_slug(self, text):
        replaced_text = re.sub(r'[-_]+', ' ', text)
        stripped_text = replaced_text.strip()
        return stripped_text.title()
