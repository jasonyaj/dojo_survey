from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'password123'


@app.route('/')
def index():
    if not 'students' in session:
        session['students'] = []
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_form():
    print( request.form )
    new_student = {
        'name' : request.form['name'],
        'dojo_location' : request.form['dojo_location'],
        'favorite_language' : request.form['favorite_language'],
        'comments' : request.form['comments']
    }
    session['students'] = new_student
    return redirect('/result')


@app.route('/result')
def show_submitted_form():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
