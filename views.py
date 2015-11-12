import json

from flask import request, Response
from flask.views import MethodView

from forms import RequestSingnatureForm


class PassphraseSign(MethodView):

    def get(self):
        """
            This is where the single page application is served

        """
        return 'Coming Soon!'

    def post(self):
        """
            Uses form data and uses the provided passphrase to sing the person data

        """
        try:
            data = json.loads(request.data)
        except ValueError:
            return Response('Unexpected data format. Expected JSON', status=400)

        form = RequestSingnatureForm(**data)

        if not form.validate():
            return json.dumps({
                'errors': form.errors,
                'success': False
            })

        signed_data = form.sign_data()

        response = {'success': True}
        response.update(signed_data)

        return json.dumps(response)