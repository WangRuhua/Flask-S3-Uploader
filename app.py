# IMPORTS
from flask import Flask, render_template, request, flash, redirect,url_for, abort, jsonify
from werkzeug.utils import secure_filename
import os

# CONFIG
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])


from tools import upload_file_to_s3

ALLOWED_EXTENSIONS = app.config["ALLOWED_EXTENSIONS"]

S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(app.config["S3_BUCKET_NAME"])

app.jinja_env.globals['s3_location'] = S3_LOCATION

# ROUTES
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # There is no file selected to upload
        print(request)
        if "user_file" not in request.files:
            return "No user_file key in request.files"

        file = request.files["user_file"]

        # There is no file selected to upload
        if file.filename == "":
            return "Please select a file"

        # File is selected, upload to S3 and show S3 URL
        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            output = upload_file_to_s3(file, app.config["S3_BUCKET_NAME"],app.config["S3_BUCKET_KEY"])
            if output[0] == 0:
                flash(str(output[1]))
                return redirect(url_for('index'))
            else:
                return redirect(url_for('index'))


            #return str(output)
        else:
            flash("file not found, or not supported file")
            return render_template("error.html")
    else:
        return render_template("index.html")
@app.route("/version")
def version():
    try:
        with open("./version.txt",'r') as f:
            version_data = f.readline()
    except Exception as e:
        print("error:",e)
        abort(404)
    return jsonify(version=version_data.strip())