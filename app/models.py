from app import db


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<id: {}, content: {}>'.format(self.id, self.content)