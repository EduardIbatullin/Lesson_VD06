from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    hobby = StringField('Хобби', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    photo = FileField('Фотография', validators=[FileAllowed(['jpg', 'png'], 'Только изображения!')])
    submit = SubmitField('Отправить')
