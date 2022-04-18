from contextlib import redirect_stderr
from crypt import methods
from flask import *
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)
app.config['SECRET_KEY'] = "cat"
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class MyForm(FlaskForm):
    image = FileField("image")

@app.route("/", methods = ["GET", "POST"])
def catpredictor():
    form = MyForm()
    if form.validate_on_submit():
        filename = images.save(form.image.data, "user_upload", "user_upload" + ".")
        flash("upload successful!")
        return render_template("temp2.html",form = form)
    return render_template("temp2.html",form = form)



