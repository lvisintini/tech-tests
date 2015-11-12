import json
from flask import request, render_template, Response
from flask.views import MethodView

from forms import ArtistSearchForm


class ArtistSearchView(MethodView):

    def get(self):
        form = ArtistSearchForm()
        return render_template('artist-search.html', form=form)

    def post(self):
        form = ArtistSearchForm(request.form)
        if not form.validate():
            return render_template('artist-search.html', form=form)

        search_results = form.get_results()

        return Response(json.dumps(search_results, indent=4),  mimetype='application/json')