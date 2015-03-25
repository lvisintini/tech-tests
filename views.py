from flask import request
from flask.views import MethodView


class PassphraseSing(MethodView):

    def get(self):
        '''
            This is where the single page application is served
        '''
        return 'Itsa me! Luigi!!!'

    def post(self):
        '''
            Uses form data and uses the provided passphrase to sing the person data
        '''
        pass
