from .. import app


def filter(words):
    filter = app.config["SEARCH_TERM_CHARACTER_FILTER"]
    filtered = [ re.sub(filter, '', x) for x in words if x]
    return filtered
