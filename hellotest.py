from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def Home():
  return render_template('home.html')
@app.route('/about')
def about():
  return render_template('aboutus.html')

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0')