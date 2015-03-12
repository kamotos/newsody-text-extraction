import bs4
from flask.ext import restful
from flask.ext.restful import fields, abort, reqparse
import requests
from readability import readability


parser = reqparse.RequestParser()
parser.add_argument('html', type=str)
parser.add_argument('url', type=fields.Url)


class TextExtractionResource(restful.Resource):
    error_messages = {
        'missing_params': "You should provide either an `url` or `html` "
                          "parameter"
    }

    def get(self):
        args = parser.parse_args()
        if not args.html and not args.url:
            abort(400, message=self.error_messages['missing_params'])
        return summarize(url=args.url, html=args.html)


def summarize(url=None, html=None):
    if url:
        html = requests.get(url.endpoint).content
    document = readability.Document(html)
    body = bs4.BeautifulSoup(document.summary())
    text = body.get_text()

    return {'text': text, 'title': document.short_title()}
