from flask import Flask, render_template, url_for
app = Flask(__name__)


post ={
	 "name":"Felister",
	 "story":"vhdvsawuvwvabuwbvwabwu vdjksjsd biiwi bifbdhhcwccb"

}

@app.route('/')
def hello_world():
    return 'Hello, Chebet to day am learning Flask dev!'
@app.route('/Home')
def Home():

	return render_template('index.html',post=post)

if __name__ == '__main__':
	app.run(debug=True)