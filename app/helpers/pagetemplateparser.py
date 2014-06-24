from .. lib.templateparser import TemplateVariableParser


class PageTemplateVariableParser:

    def __init__(self):
        self.templatevars = {}

    def set(self, name, value):
        self.templatevars[name] = value

    def parse(self, request):
        self._add_core_templatevars(request)
        return self.templatevars

    def _add_core_templatevars(self, request):
        vars = TemplateVariableParser().parse(request)
        self.templatevars.update(vars)
