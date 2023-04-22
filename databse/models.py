from app import db

class MIKAUTH(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_type = db.Column(db.String(150))
    port = db.Column(db.Integer)
    ip = db.Column(db.String(150))
    name = db.Column(db.String(150))
    login = db.Column(db.String(150))
    passwd = db.Column(db.String(150))
    timeout = db.Column(db.Integer)
    
    def __repr__(self):
        return '<MIKAUTH id: {}, name: {}>'.format(self.id, self.name)
    