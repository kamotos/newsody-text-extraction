import flask
from flask.ext import restful

from resources import TextExtractionResource


app = flask.Flask(__name__)
api = restful.Api(app)


api.add_resource(TextExtractionResource, '/v1/')

if __name__ == '__main__':
    app.run(host="0", port=5000)
