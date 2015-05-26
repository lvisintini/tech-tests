import os

from flask import Flask
from ojota import set_data_source

from search.views import ArtistSearchView

# Setup application
app = Flask(__name__)
app.add_url_rule('/artist-search/', view_func=ArtistSearchView.as_view('search'))

# Setup JSON sources
file_path = (os.path.dirname(os.path.abspath(__file__)))
set_data_source(os.path.join(file_path, "data"))

if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
