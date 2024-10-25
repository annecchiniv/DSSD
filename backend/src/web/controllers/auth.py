from flask import render_template, Blueprint, redirect, request, url_for, session, flashpip 

login_blueprint = Blueprint("login", __name__, url_prefix="/login")
logout_blueprint = Blueprint("logout", __name__, url_prefix="/logout")

@login_blueprint.get("/")
def login():
    return render_template("auth/login.html")

@login_blueprint.route("/auth", methods=['POST'])
def authenticate():
    params = request.form
    
    user = u.authenticate_user(params)

    if not user:
        flash("Usuario o contraseña incorrecto")
        return redirect(url_for("login.login"))
        
    if not user.state:
        flash("Usuario no activo")
        return render_template("auth/login.html")

    session["user"] = user.email
    return redirect(url_for("home"))

@logout_blueprint.get("/")
def logout():
    auth.logout()
    return redirect(url_for('login.login'))        