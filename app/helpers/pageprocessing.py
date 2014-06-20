from flask import g, request
from application.pagetemplateparser import PageTemplateVariableParser

def common_page_processing():
    additional_data = {'documents_directory': 'docs'}
    g.templatevars = PageTemplateVariableParser().parse(request,
                                                        additional_data)
