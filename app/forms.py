from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class palabra_en_formacion(FlaskForm):
    letras = StringField('letras', validators=[DataRequired()])
    submit = SubmitField('Busca')
