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
        zipcode = request.form['zipcode']

        if not zipcode:
            error = 'Postcode is required'

        if error:
            flash(error, category='error')

        return redirect(url_for('views.weather', zipcode=zipcode))

    return render_template('views/search.html')


@bp.route('/weather/<zipcode>', methods=('GET', 'POST'))
def weather(zipcode):
    # If POST request, redirect to search (code 307 retains POST)
    if request.method == 'POST':
        return redirect(url_for('views.search'), code=307)

    # try:
    data = WeatherData(zipcode)
    return render_template('views/weather.html', zipcode=zipcode, data=data)

    """except Exception:
        flash('An error occured', category='error')
        return redirect('/')"""
