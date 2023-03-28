token = ["fhsujfiohfe8jkoie3ujddfj", "hfdusgwudjfedyeq", "gfwesdhewouikfld", "fhisduhyf8eqowkl", "hgwifeskjdl",
          "tgrfwhudjsu","hgdfkgodvskmcx","gyyydsjihuwgydisj","r698qwyodhsn","figywbdkcsalk","giqfuahndkmz"]


import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
if not session.get('logged_in'):
return render_template('login.html')
else:
return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
if request.form['password'] == 'password' and request.form['username'] == 'admin':
session['logged_in'] = True
else:
flash('wrong password!')
return home()

if __name__ == "__main__":
app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)


