from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
import requests

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html",user=current_user)

@views.route('/patient-dashboard',methods=['GET','POST'])
@login_required
def patient():
    if request.method == 'POST':
        health_data = {
            'user_id':int(current_user.user_id),
            'pulserate': request.form.get('pulse_rate'),
            'syspressure': request.form.get('pulse_rate'),
            'diapressure': request.form.get('dia_pressure'),
            'bloodsugar': request.form.get('blood_sugar'),
            'stepcount':request.form.get('step_count')
        }

        response = requests.post('http://localhost:3100/vitals_upload/', json=health_data)
        print(response)
        if response.ok:
            return 'Health data submitted successfully!'
        else:
            return 'Error submitting health data.'
    return render_template("patient.html",user=current_user)


@views.route('/doctor-dashboard')
@login_required
def doctor():
    return render_template("doctor.html",user=current_user)