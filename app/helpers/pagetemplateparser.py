from .. lib.templateparser import TemplateVariableParser
from . navigationcreator import NavigationCreator


class PageTemplateVariableParser:

    def __init__(self):
        self.templatevars = {}

    def set(self, name, value):
        self.templatevars[name] = value

    def parse(self, request, additional_data = {}):
        self.data = additional_data
        self._add_core_templatevars(request)
        self._parse_templatevars()
        return self.templatevars

    def _add_core_templatevars(self, request):
        vars = TemplateVariableParser().parse(request)
        self.templatevars.update(vars)

    def _parse_templatevars(self):
        dir = self.data.get('documents_directory', '')
        self.templatevars['nav_items'] = NavigationCreator().create(dir)
