from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # POST
        # data base queries to check if valid
        flash(f'Welcome, {form.user_name.data}!', 'success')
        return redirect(url_for('main.index'))

    # GET
    return render_template('user.html', heading="Login", form=form)

@bp.route('/register', methods=["POST","GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # POST
        # Check if we can add this user or if it exists
        flash(f'Successfully registered, {form.user_name.data}!', 'primary')

        return redirect(url_for('auth.login'))

    # GET
    return render_template('user.html', heading="Register", form=form)

@bp.route('/logout', methods=["POST","GET"])
def logout():
    flash(f'You have been logged out :(', 'info')
    return render_template('index.html')
