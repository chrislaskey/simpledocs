from lib.templateparser import TemplateVariableParser

class PageTemplateVariableParser:

    def __init__(self):
        self.templatevars = {}

    def set(self, name, value):
        self.templatevars[name] = value

    def parse(self, request):
        self._add_core_templatevars(request)
        self._parse_templatevars()
        return self.templatevars

    def _add_core_templatevars(self, request):
        vars = TemplateVariableParser().parse(request)
        self.templatevars.update(vars)

    def _parse_templatevars(self):
        self.templatevars['language'] = self._parse_language()
        self.templatevars['mirror_language_link'] = \
                self._parse_mirror_language_link()

    def _parse_language(self):
        uri_segments = self.templatevars.get('uri_segments')[:]
        if not uri_segments:
            language = 'en'
        else:
            language = uri_segments[0]
        return language

    def _parse_mirror_language_link(self):
        inactive_language = self._return_inactive_language()
        uri_segments = self.templatevars.get('uri_segments')
        if len(uri_segments) > 0 and uri_segments[0] in ('be', 'en'):
            uri_segments[0] = inactive_language
        else:
            uri_segments.insert(0, inactive_language)
        return '/' + '/'.join(uri_segments)

    def _return_inactive_language(self):
        language = self.templatevars['language']
        if language == 'en':
            return 'be'
        else:
            return 'en'
