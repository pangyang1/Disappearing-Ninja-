from flask import Flask,render_template,request,redirect
app =Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')
@app.route('/ninja/blue')
def ninjablue():
    return render_template('ninjablue.html')
@app.route('/ninja/orange')
def ninjaorange():
    return render_template('ninjaorange.html')
@app.route('/ninja/red')
def ninjared():
    return render_template('ninjared.html')
@app.route('/ninja/purple')
def ninjapurple():
    return render_template('ninjapurple.html')
@app.errorhandler(404)
def notapril(e):
    return render_template('404.html')


app.run(debug=True)
