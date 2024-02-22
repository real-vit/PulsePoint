from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html",user=current_user)

@views.route('/patient-dashboard')
@login_required
def patient():
    return render_template("patient.html",user=current_user)

@views.route('/doctor-dashboard')
@login_required
def doctor():
    return render_template("doctor.html",user=current_user)