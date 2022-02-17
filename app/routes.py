from crypt import methods

from flask import flash, redirect, render_template

from app import app
from app.forms import palabra_en_formacion


@app.route('/', methods=['GET', 'POST'])
def index():
    form = palabra_en_formacion()
    if form.validate_on_submit():
        letras = form.letras.data
        letras = letras.lower()
        flash('Has introducido las siguientes letras {}'.format(letras))
        return redirect('/')
    return render_template('index.html', form=form)
