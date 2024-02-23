from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, logout_user, current_user
import requests

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/patient-dashboard", methods=["GET", "POST"])
@login_required
def patient():
    response = requests.get(
    f"http://localhost:3000/vitals_fetch/{current_user.user_id}")
    if response.ok:
        vitals_data = response.json().get("Vitals")
    else:
        vitals_data = None

    if request.method == "POST":
        if request.form["submit_button"] == "Vitals":
            health_data = {
                "user_id": int(current_user.user_id),
                "pulserate": request.form.get("pulse_rate"),
                "syspressure": request.form.get("sys_pressure"),
                "diapressure": request.form.get("dia_pressure"),
                "bloodsugar": request.form.get("blood_sugar"),
                "stepcount": request.form.get("step_count"),
            }

            response = requests.post(
                "http://localhost:3000/vitals_upload/", json=health_data
            )
            if (
                response.json().get("Error")
                == "Vitals can be posted only once per day."
            ):
                return "Vitals can only be posted once per day. Please try again later."
            elif response.ok:
                return "Health data submitted successfully!"
            else:
                return "Error submitting health data."

        if request.form["submit_button"] == "Diet":
            response = requests.get(
                f"http://localhost:3000/vitals_fetch/{current_user.user_id}"
            )
            if response.ok:
                vitals_data = response.json().get("Vitals")[0]
                response = requests.post(
                    "http://localhost:3000/dietPlan/", json=vitals_data
                )
                if response.ok:
                    result = response.json().get("message")
                    return result
                else:
                    return "Error fetching diet plan."

        if request.form["submit_button"] == "Exercise":
            response = requests.get(
                f"http://localhost:3000/vitals_fetch/{current_user.user_id}"
            )
            if response.ok:
                vitals_data = response.json().get("Vitals")[0]
                response = requests.post(
                    "http://localhost:3000/exercisePlan/", json=vitals_data
                )
                if response.ok:
                    result = response.json().get("message")
                    return result
                else:
                    return "Error fetching exercise plan."

        if request.form["submit_button"] == "EODReport":
            response = requests.get(
                f"http://localhost:3000/vitals_fetch/{current_user.user_id}"
            )
            if response.ok:
                vitals_data = response.json().get("Vitals")[0]
                response = requests.post(
                    "http://localhost:3000/EODReport/", json=vitals_data
                )
                if response.ok:
                    result = response.json().get("message")
                    return result
                else:
                    return "Error fetching Report."

    return render_template("patient.html", user=current_user, vitals=vitals_data)


@views.route("/doctor-dashboard")
@login_required
def doctor():
    return render_template("doctor.html", user=current_user)
