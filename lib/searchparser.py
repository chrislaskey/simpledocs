
    # TODO temporary

    # Break search into individual words.
    #   For each word:
    #       Validate query.
    #       Search for file names.
    #       Search within files.
    #       Add to list of returned pages

#     def is_valid_query(query):
#         if not query or '..' in query or query.startswith('/'):
#             return False
#         return True

#     search = '../'
#     if not is_valid_query(search):
#         return []

#     cli = CommandLine()
#     command = cli.execute_queue([
#         ['ls', '-a'],
#         ['grep', '.py']
#     ])
#     templatevars = {
#         "content": command
#     }

class SearchParser:

    def __init__():
        pass
