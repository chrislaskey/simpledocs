from flask import g, request
from application.pagetemplateparser import PageTemplateVariableParser

def common_page_processing():
    g.templatevars = PageTemplateVariableParser().parse(request)
