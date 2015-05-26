from flask import Flask
from jinja2 import Environment, PackageLoader

from search.views import ArtistSearchView

app = Flask(__name__)

app.add_url_rule('/artist-search/', view_func=ArtistSearchView.as_view('search'))

#env = Environment(loader=PackageLoader('artist-search', 'templates'))

if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
