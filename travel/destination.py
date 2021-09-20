from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Comment, Destination
from .forms import DestinationForm, CommentForm

bp = Blueprint('destination', __name__, url_prefix="/destination")

@bp.route('/<int:id>')
def show(id):
    # here is where you would make some sort of API / DB call
    print(id)
    form = CommentForm()
    new_destination = get_destination()

    return render_template('destination/show.html', destination=new_destination, form=form, id=id)

@bp.route('/create', methods=["POST", "GET"])
def create():
    form = DestinationForm()
    # This will only eval to true if we are using POST & all inputs are validated
    if form.validate_on_submit():
        print("We have made a place!")
        # This is where we would do some database stuff - add to data base -> redirect to new destination
        return redirect(url_for('destination.show', id=1)) # update the ID when we have database
    return render_template('destination/create.html', form=form)

@bp.route('/<int:id>/comment', methods=["GET", "POST"])
def comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        # save to database
        flash(f'Comment successfully posted!', 'success')
        flash(f'Comment successfully posted!', 'danger')

    return redirect(url_for('destination.show', id=id))
    


def get_destination():

    image_url = "https://images.pexels.com/photos/2868242/pexels-photo-2868242.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"

    dest = Destination("Brazil", "Soccer yes very nice", "0.23 Brz", image_url)
    dest.addComment(Comment("user 1", "Sample comment!"))
    dest.addComment(Comment("user 2", "Another sample comment!"))
    dest.addComment(Comment("user 3", "Aaaaaand yet another sample comment!"))

    return dest