from flask import Flask, render_template 

app = Flask(__name__)

posts = [
    {
        'author': "Daniel RIVIERE",
        'title': "My second flask app",
        'content': "First post content"
    },
    {
        'author': "Test User",
        'title': "Second post message",
        'content': "Second post content"
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)
