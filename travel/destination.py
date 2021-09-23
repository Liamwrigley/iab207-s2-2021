from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Comment, Destination
from .forms import DestinationForm, CommentForm
from werkzeug.utils import secure_filename
from . import db
import os

bp = Blueprint('destination', __name__, url_prefix="/destination")

@bp.route('/<int:id>')
def show(id):
    form = CommentForm()
    destination = Destination.query.filter_by(id=id).first()
    # if no destinations => send to home page
    if destination is None:
        flash(f'Could not find a destination!', 'warning')
        return redirect(url_for('main.index'))

    # if is destinations => continue to show page
    return render_template('destination/show.html', destination=destination, form=form)

@bp.route('/create', methods=["POST", "GET"])
def create():
    form = DestinationForm()
    # This will only eval to true if we are using POST & all inputs are validated
    if form.validate_on_submit():

        destination = Destination(
            name = form.name.data,
            description = form.description.data,
            currency = form.currency.data,
            image = check_upload_file(form)
        )

        db.session.add(destination)
        db.session.commit()

        flash(f'Successfully created {destination.name}!', 'success')

        return redirect(url_for('destination.show', id=destination.id))
    return render_template('destination/create.html', form=form)

@bp.route('/<int:id>/comment', methods=["GET", "POST"])
def comment(id):
    form = CommentForm()
    if form.validate_on_submit():

        comment = Comment(
            text = form.text.data,
            user_id = 1, # We need to update this later 
            destination_id = id
        )

        db.session.add(comment)
        db.session.commit()

        flash(f'Comment successfully posted!', 'success')

    return redirect(url_for('destination.show', id=id))


def check_upload_file(form):
    #get file data from form  
    fp=form.image.data
    filename=fp.filename
    #get the current path of the module file… store image file relative to this path  
    BASE_PATH=os.path.dirname(__file__)
    #upload file location – directory of this file/static/image
    upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
    #store relative path in DB as image location in HTML is relative
    db_upload_path='/static/image/' + secure_filename(filename)
    #save the file and return the db upload path  
    fp.save(upload_path)
    return db_upload_path