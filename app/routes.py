from flask import flash, redirect, render_template

from app import app
from app.forms import palabra_en_formacion
import siguiente_letra


@app.route('/', methods=['GET', 'POST'])
def index():
    form = palabra_en_formacion()
    candidatas = []
    if form.validate_on_submit():
        letras = form.letras.data
        letras = letras.lower()
        candidatas = siguiente_letra.main(letras)
        flash('Has introducido las siguientes letras: {}'.format(letras))
        flash('Candidatas para la siguiente letra {}'.format(candidatas))
        return redirect('/')
    return render_template('index.html', form=form)
