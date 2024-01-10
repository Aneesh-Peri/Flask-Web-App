from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('FirstName')
        password1 = request.form.get('Password')
        password2 = request.form.get('PassCon')
        filename = request.form.get('FileName')

        if len(email) < 7:
            flash('Email is too short(min 7 characters)', category='error')
        elif len(first_name) < 3:
            flash('Name is too short(min 3 characters)', category='error')
        elif password1 == "" or len(password1) < 7:
            flash("There is no password entered. ", category='error')
        elif password1 != password2:
            flash("Password 2 does not match", category='error')
        elif filename=="":
            flash('You must include a file name',category='error')
        else:
            flash("Account successfully created!! ", category='success')

        file = open(filename+".txt","w")
        file.write("Email: " + email+"\n")
        file.write("Name: " + first_name+"\n")
        file.write("Password: " + password1+"\n")


    return render_template("SignUp.html", boolean=True)


@auth.route("/logout")
def logout():
    return "logout"


@auth.route("/About")
def about():
    return render_template("About_Page.html", boolean=True)
