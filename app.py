
from config import db, ma, server

app = server.app


@app.before_first_request
def create_table():
    db.create_all()


db.init_app(app)

if __name__ == '__main__':

    ma.init_app(app)
    server.run()