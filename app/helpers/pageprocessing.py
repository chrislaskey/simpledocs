from flask import g, request
from . pagetemplateparser import PageTemplateVariableParser


def common_page_processing():
    g.templatevars = _PageTemplateVariableParser().parse(request)
