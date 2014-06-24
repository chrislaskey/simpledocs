from flask import g, request
# from . pagetemplateparser import PageTemplateVariableParser
from .. lib.templateparser import TemplateVariableParser


def common_page_processing():
    # g.templatevars = PageTemplateVariableParser().parse(request)
    g.templatevars = TemplateVariableParser().parse(request)
