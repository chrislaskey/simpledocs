import re
from unicodedata import normalize

from . requestparser import RequestParser


class TemplateVariableParser:

    def __init__(self):
        self.templatevars = {}

    def set(self, name, value):
        self.templatevars[name] = value

    def parse(self, request):
        self._parse_request(request)
        self._parse_templatevars()
        return self.templatevars

    def _parse_request(self, request):
        parsed_request = RequestParser().parse(request)
        parsed_request['form'] = request.form
        self.templatevars.update(parsed_request)

    def _parse_templatevars(self):
        segments = self.templatevars.get('uri_segments')[:]
        self._set_page_title(segments)
        self._set_body_class(segments)

    def _set_page_title(self, segments):
        page_title = _PageTitleCreator().get(segments)
        self.set('page_title', page_title)

    def _set_body_class(self, segments):
        body_class = _BodyClassCreator().get(segments)
        self.set('body_class', body_class)


class _PageTitleCreator:

    def get(self, uri_segments):
        sections = self._process_page_title_segments(uri_segments)
        if not sections:
            return 'Home'
        elif len(sections) > 1:
            return ' | '.join(sections)
        else:
            return sections[0]

    def _process_page_title_segments(self, uri_segments):
        sections = []
        for piece in uri_segments:
            if piece in ('be', 'en'):
                continue
            title = self._create_title_from_slug(piece)
            sections.append(title)
        sections.reverse()
        return sections

    def _create_title_from_slug(self, text):
        replaced_text = re.sub(r'[-_]+', ' ', text)
        stripped_text = replaced_text.strip()
        return stripped_text.title()


class _BodyClassCreator:

    def get(self, uri_segments):
        classes = ['body']
        for section in uri_segments:
            previous_class = classes[-1][:]
            section_slug = self._create_slug(section)
            new_class = previous_class + '-{0}'.format(section_slug)
            classes.append(new_class)
        classes_string = ' '.join(classes)
        return classes_string

    def _create_slug(self, text, delimiter=u'-'):
        '''
        Return ascii-only slugs from unicode.
        See: http://flask.pocoo.org/snippets/5/
        '''
        try:
            _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
            result = []
            text = text.strip()
            text = text.lower()
            for word in _punct_re.split(text):
                word = normalize('NFKD', word).encode('ascii', 'ignore')
                if word:
                    result.append(word)

            return unicode(delimiter.join(result))
        except TypeError:
            text = unicode(text)
            return self._create_slug(text, delimiter)
