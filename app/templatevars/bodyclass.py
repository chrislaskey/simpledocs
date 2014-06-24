import re
from unicodedata import normalize


class BodyClass:

    def get(self, uri_segments):
        classes = ['body']
        for section in uri_segments:
            previous_class = classes[-1][:]
            section_slug = self._create_slug(section)
            new_class = previous_class + '-{0}'.format(section_slug)
            classes.append(new_class)
        classes_string = ' '.join(classes)
        return classes_string

    def _create_slug(self, text, delimiter=u'-'):
        '''
        Return ascii-only slugs from unicode.
        See: http://flask.pocoo.org/snippets/5/
        '''
        try:
            _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
            result = []
            text = text.strip()
            text = text.lower()
            for word in _punct_re.split(text):
                word = normalize('NFKD', word).encode('ascii', 'ignore')
                if word:
                    result.append(word)

            return unicode(delimiter.join(result))
        except TypeError:
            text = unicode(text)
            return self._create_slug(text, delimiter)

