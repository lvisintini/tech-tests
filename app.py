from flask import Flask

from views import PassphraseSing

app = Flask(__name__)
app.add_url_rule('/', view_func=PassphraseSign.as_view('sign'))

if __name__ == "__main__":
    app.debug = True
    app.run(port=8000)
