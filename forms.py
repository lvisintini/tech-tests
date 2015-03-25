from wtforms import Form, StringField, PasswordField, validators


class RequestSingnatureForm(Form):
    passphrase = PasswordField('Passphrase', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    surname = StringField('Surname', [validators.DataRequired()])
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Email()
    ])