def parse(request):
    return UriParser().parse(request)


class UriParser:

    '''
    Parses a Flask Request object into a dictionary of useful URI information
    like a list of uri segments, the domain, request protocol, etc.
    '''

    def parse(self, flask_request):
        self.request = flask_request
        return self._parse_request()

    def _parse_request(self):
        self.parsed = {}
        self.parsing = self.request.base_url.__str__()
        self._validate_url()
        self._parse_protocol()
        self._parse_domain()
        self._parse_uri_segments()
        self._parse_uri()
        return self.parsed

    def _validate_url(self):
        has_protocol_string = (self.parsing.find('://') != -1)
        if not has_protocol_string:
            raise Exception('Invalid URL')

    def _parse_protocol(self):
        protocol, self.parsing = self.parsing.split('://')
        self.parsed['protocol'] = protocol

    def _parse_domain(self):
        self._parse_into_segments()
        self.parsed['domain'] = self._segments[0]

    def _parse_into_segments(self):
        segments = self.parsing.split('/')
        filtered_segments = [x for x in segments if x]
        self._segments = filtered_segments

    def _parse_uri_segments(self):
        self.parsed['uri_segments'] = self._segments[1:]

    def _parse_uri(self):
        uri_segments = self.parsed.get('uri_segments')
        self.parsed['uri'] = '/' + '/'.join(uri_segments)
