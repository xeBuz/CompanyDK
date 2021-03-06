from app import db


class CompanyModel(db.Model):

    __tablename__ = 'co_company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125))
    address = db.Column(db.String(125))
    city = db.Column(db.String(125))
    country = db.Column(db.String(125))
    email = db.Column(db.String(125))
    phone = db.Column(db.String(25))

    def __init__(self, name, address, city, country, email=None, phone=None):
        """
        Contructor for a new CompanyModel

        :param name:
        :param address:
        :param city:
        :param country:
        :param email:
        :param phone:
        """
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.email = email
        self.phone = phone

    def __repr__(self):
        return str(self.id)

    @property
    def serialize(self):
        """
        Serialize the Model for the JSON responses

        :return: JSON
        """
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'country': self.country,
            'email': self.email,
            'phone': self.phone
        }

    def save(self):
        """
        Add/Save a Company
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete a Company
        """
        db.session.delete(self)
        db.session.commit()
