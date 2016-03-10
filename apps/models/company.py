from app import db


class CompanyModel(db.Model):

    __tablename__ = 'co_company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125))
    address = db.Column(db.String(125))
    city = db.Column(db.String(125))
    email = db.Column(db.String(125))
    phone = db.Column(db.String(25))
    # directors
    # beneficials

    def save(self):
        """Add a Company"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete a Company"""
        db.session.delete(self)
        db.session.commit()

    def __init__(self, name, email, address, city, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.city = city
        self.address = address

    def __repr__(self):
        return self.id