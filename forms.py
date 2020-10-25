from flask_wtf import FlaskForm  #flask_wtf is the flak's form module for wt forms
from wtforms import StringField, SubmitField    #StringField is similar to HTML text field & SubmitFiedld is similar to submit input element in HTML
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    title=StringField('Title',validators=[DataRequired()])
    submit=SubmitField('Submit')

class DeleteTaskForm(FlaskForm):
    submit=SubmitField('Delete')