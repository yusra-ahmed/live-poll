from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

async_mode = None

app = Flask(__name__)

app.secret_key = "Livepollpubnub"

@app.route('/')
def index():
    """Landing page with poll"""

    return render_template('livepoll.html')

@app.route("/error")
def error():

    raise Exception("Error!")


if __name__ == "__main__":
    # debug=True allows for use of DebugToolbarExtension downstream
    app.debug = False

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=5000)
