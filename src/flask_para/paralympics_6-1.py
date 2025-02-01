""" This is an example of a minimal Flask application."""
# Import the Flask class from the Flask library
from flask import Flask, render_template

# Create an instance of a Flask application
# The first argument is the name of the application’s module or package. __name__ is a convenient shortcut.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


# Add a route for the 'home' page
# use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    """
    This function returns the home page.
    If the option name is added, it displayes a personalised message to the user.
    Args:
        name: String to represent the user's name

    Returns:
        String that displays as the app's home page in the browser.

    """
    # The function returns the message we want to display in the user’s browser.
    # The default content type for a Flask page is HTML. The string will be rendered as an HTML paragraph by the browser.
    if name:
        # You can include HTML tags in the string to format the output.
        return f'<h1>Hello {name}! and welcome to my paralympics app.<h1>'
    else:
        return 'Hello World!'


# A route that uses a template
@app.route('/hello/')
def hello_with_template():
    # The function renders a Jinja2 template that generates the home page using HTML and bootstrap CSS
    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
