from flask import flash, redirect, render_template, session, url_for

from app import app
from app.forms import palabra_en_formacion
import siguiente_letra


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = palabra_en_formacion()
    candidatas = []
    if 'letras' in session:
        letras_old = session['letras']
    else:
        letras_old = ''
        session['letras'] = letras_old
    if form.validate_on_submit():
        letra = form.letras.data
        letra = letra.lower()
        letras = letras_old + letra
        candidatas = siguiente_letra.main(letras)
        session['letras'] = letras
        session['candidatas'] = candidatas
        flash('Candidatas para la siguiente letra {}'.format(candidatas))
        return redirect(url_for('index'))
    return render_template('index.html', form=form, letras=session['letras'])

@app.route('/reset')
def reset():
    session['letras'] = ''
    return redirect(url_for('index'))
