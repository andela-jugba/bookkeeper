from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app.models import Category, Book
import os


app = create_app(os.getenv('BLOG_CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, Category=Category, Book=Book)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test(coverage=False):
    '''
    Runs Unit tests

    '''
    from subprocess import call
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=app', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])

if __name__ == '__main__':
    manager.run()
