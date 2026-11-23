from flask import Blueprint, request, render_template

from app.rps import determine_outcome, generate_computer_choice

rps_routes = Blueprint("rps_routes", __name__)

@rps_routes.route("/rps/form")
def rps_form():
    print("RPS FORM...")
    return render_template("rps_form.html")


@rps_routes.route("/rps/results", methods=["POST"])
def rps_results():
    print("RPS RESULTS...")
    print("FORM DATA:", dict(request.form))

    user_choice = request.form.get("user_choice")
    computer_choice = generate_computer_choice()
    outcome = determine_outcome(user_choice, computer_choice)

    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )
