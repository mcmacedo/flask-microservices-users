# manage.py

from flask_script import Manager
from project import app, db


manager = Manager(app)


@manager.command
def recreate_db():
    """Recrie o banco de dados"""
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
