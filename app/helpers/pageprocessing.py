from flask import g, request
from .. lib.templateparser import TemplateVariableParser


def common_page_processing():
    g.templatevars = TemplateVariableParser().parse(request)
