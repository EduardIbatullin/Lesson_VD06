import os
from flask import Blueprint, render_template, redirect, url_for, request, current_app
from werkzeug.utils import secure_filename
from .forms import UserForm

main_bp = Blueprint('main', __name__)

users = []


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        city = form.city.data
        hobby = form.hobby.data
        age = form.age.data
        photo = form.photo.data

        if photo:
            filename = secure_filename(photo.filename)
            photo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            photo.save(photo_path)
            photo_url = url_for('static', filename='uploads/' + filename)
        else:
            photo_url = url_for('static', filename='uploads/placeholder.jpg')

        user = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age,
            'photo': photo_url
        }
        users.append(user)
        return redirect(url_for('main.index'))

    return render_template('index.html', form=form, users=users)
