from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/<name>')
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
@main.route('/hello/')
def hello_with_template():
    # The function renders a Jinja2 template that generates the home page using HTML and bootstrap CSS
    return render_template('index.html')
