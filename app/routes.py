from flask import Flask, render_template, request, redirect, flash
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'yaco1639dsaj003'

@app.route('/')
@app.route('/index')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required!')
            return render_template('contact.html', form=form)
        else:
            return 'Form posted.'
    elif request.method  == 'GET':
        return render_template('contact.html', form=form)
"""
@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token
"""

if __name__ == '__main__':
	app.run(debug=True)