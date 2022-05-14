from flask import (
    Blueprint, render_template, redirect, request, url_for, flash
)

from .pweather import WeatherData

bp = Blueprint('views', __name__)


@bp.route('/home')
def home():
    return render_template('base.html')


@bp.route('/', methods=('GET', 'POST'))
def search():
    error = None
    if request.method == 'POST':
        postcode = request.form['postcode']

        if not postcode:
            error = 'Postcode is required'

        if error:
            flash(error, category='error')

        return redirect('/weather/<postcode>')

    return render_template('views/search.html')


@bp.route('/weather/<postcode>')
def weather(postcode):
    try:
        data = WeatherData(postcode)
        return render_template('views/weather.html', postcode=postcode, data=data)

    except Exception:
        flash('Invalid postal code!', category='error')
        return redirect('/')
