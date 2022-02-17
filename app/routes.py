from crypt import methods

from flask import flash, redirect, render_template

from app import app
from app.forms import palabra_en_formacion


@app.route('/', methods=['GET', 'POST'])
def index():
    form = palabra_en_formacion()
    if form.validate_on_submit():
        flash('Has introducido las siguientes letras {}'.format(form.letras.data))
        return redirect('/')
    return render_template('index.html', form=form)
