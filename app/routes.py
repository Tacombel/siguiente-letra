from flask import flash, redirect, render_template, session, url_for

from app import app
from app.forms import palabra_en_formacion
import siguiente_letra


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = palabra_en_formacion()
    candidatas = []
    if not session['letras']:
        session['letras'] = ""
    if form.validate_on_submit():
        letras = form.letras.data
        letras = letras.lower()
        session['letras'] = letras
        candidatas = siguiente_letra.main(letras)
        session['candidatas'] = candidatas
        flash('Candidatas para la siguiente letra {}'.format(candidatas))
        return redirect(url_for('index'))
    return render_template('index.html', form=form, letras=session['letras'])
