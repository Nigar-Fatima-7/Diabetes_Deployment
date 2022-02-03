from flask import Flask, render_template, request
import joblib

#initialize the app
app = Flask(__name__)
model = joblib.load('dib_79.pkl')
print('[INFO] model loaded')

@app.route('/')
def hello_world():
    return render_template('dataset.html')

@app.route('/welcome')
def welcome():
    return 'hello this is welcome page'

@app.route('/contact')
def contact():
    return 'welcome to contact page'

@app.route('/blog')
def blog():
    return 'welcome to blog page'

@app.route('/gallary')
def gallary():
    return 'welcome to gallary page'

@app.route('/predict', methods = ['post'])
def predict():
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')

    print(first_name)
    print(last_name)
    print(email)
    print(phone)

    return 'Form Submitted'

@app.route('/predict_dia', methods = ['post'])
def predict_dia():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)

    output = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if(output[0]==1):
        ans= 'diabetic'
    else:
        ans= 'not diabetic'

    return render_template('dataset.html', predict = f'the person is {ans}')

#run the app
app.run(debug=True)

