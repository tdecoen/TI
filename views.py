from flask import render_template, flash, redirect, request, session, g, url_for
from flask_login import login_required
from TI import app, lm
from .forms import LoginForm
from .data import Customer
from .da import CustomerDA
from .auth import authenticate

@app.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = {}

@lm.user_loader
def load_user(user_id):
	try:
		return Customer.get(user_id)
	except User.DoesNotExist:
        	return None

@app.route('/')
@app.route('/index')
@login_required
def index():
    	user = {'nickname': 'Miguel'}
    	return render_template('index.html',
                           title='Home',
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if g.user:
		return redirect(url_for('index'))
	if request.method == 'POST':
		if form.validate_on_submit():
			user = form.username.data
			password = form.password.data
			token = form.token.data
			ip = request.remote_addr
			result = authenticate(user, password, token, ip)
			return result
			#if customer:
        		#	test = ldap.bind_user(user, passwd)
        		#	if test is None or passwd == '':
            		#		return 'Invalid credentials'
        		#	else:
            		#		session['user_id'] = form.username.data
            		#		return redirect('/')
	return render_template('login.html',title='Sign In',form=form)

@app.route('/ldap')
@login_required
def ldap_protected():
	return 'Success!'

@app.route('/DBtest')
def DBtest():
	customerDA = CustomerDA()
	return customerDA.findCompany('SpotIT')
