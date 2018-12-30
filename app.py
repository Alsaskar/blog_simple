from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sys
from models import users, beranda
from config import function

user = users.Users()
fct  = function.Function()
brd = beranda.Beranda()

app = Flask(__name__, template_folder='views')

# secret key, don't let know this to more people
app.secret_key = 'blogsimplesecret##' # for example

@app.route('/')
def index():

	# get post
	getpost = brd.showpost()

	getsession = session

	return render_template('index.html', title='Blog Simple', getsession=getsession, getpost=getpost)

# ini halaman register
@app.route('/register', methods=['GET', 'POST'])
def register():
	
	# check, if the user has ben login, then
	if 'user' in session:
		# user can't access in page this
		return redirect(url_for('user.dashboard'))

	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
		email = request.form['email']
		password = request.form['password']
		r_pass = request.form['r_pass']

		if firstname == '':
			flash('Firstname cannot be empty', 'error')
		elif lastname == '':
			flash('Lastname cannot be empty', 'error')
		elif email == '':
			flash('Email cannot be empty', 'error')
		elif password == '':
			flash('Password cannot be empty', 'error')
		elif r_pass == '':
			flash('Reply Password cannot be empty', 'error')
		else:
			if password == r_pass:

				if fct.validemail(email) == True:

					# password hash
					pw_pass = generate_password_hash(password)

					# add user and saving to database
					user.register(firstname, lastname, email, pw_pass)

					flash('You success register. Please login now.', 'success')
					return redirect(url_for('login'))
				else:
					flash('Email is not valid.', 'error')
			else:
				flash('Password is not same with Reply Password', 'error')

		return redirect(url_for('register'))
	else:
		return render_template('register.html', title='Blog Simple - Register')

@app.route('/login', methods=['GET', 'POST'])
def login():

	# check, if the user has ben login, then
	if 'user' in session:
		# user can't access in page this
		return redirect(url_for('user.dashboard'))

	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		login_user = user.login(email)

		if login_user == True:
			flash('Email is wrong', 'error')
		else:

			if check_password_hash(login_user[0][1], password):
				# create session
				session['user'] = email

				# switch to the admin dashboard page
				return redirect('/dashboard')
			else:
				flash('Password is wrong', 'error')

		return redirect(url_for('login'))

	else:
		return render_template('login.html', title='Blog Simple - Login')

# show detail post
@app.route('/view/post/<url>')
def detail_post(url):
	
	# show post per url
	getpost = brd.showpostperurl(url)

	# get session
	getsession = session

	return render_template('view_post.html', title=getpost[0][1], getsession=getsession, getpost=getpost)

# create blueprint 
from user import user as user_blueprint
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
	app.run(debug=True)