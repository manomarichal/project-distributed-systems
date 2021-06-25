from flask.cli import FlaskGroup

from project import create_app

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # new

if __name__ == '__main__':
    cli()