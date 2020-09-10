from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators, SubmitField, FloatField

class Addproducts(Form):
    name= StringField('Name',[validators.DataRequired()])
    price = FloatField('Price',[validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('stock', [validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    colors = TextAreaField('Colors', [validators.DataRequired()])

    image_1 = FileField('Image_1', validators=[FileRequired(), FileAllowed(['jpg','png', 'gif', 'jpeg'])])
    image_2 = FileField('Image_2', validators=[FileRequired(), FileAllowed(['jpg','png', 'gif', 'jpeg'])])
    image_3 = FileField('Image_3', validators=[FileRequired(), FileAllowed(['jpg','png', 'gif', 'jpeg'])])        