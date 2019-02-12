from flask import Flask,render_template,redirect,url_for,request
#create the application object
app=Flask(__name__)

@app.route('/')
def homepage():
    return "Hello world"

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!='admin'or request.form['password']!='admin':
            error='Invalid credentials'
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html',error=error)

app.run(debug=True)
        
