from app import db
from api.models.company import CompanyModel


class OwnerModel(db.Model):

    __tablename__ = 'co_owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125))
    company_id = db.Column(db.Integer, db.ForeignKey(CompanyModel.id))
    company = db.relation(CompanyModel)

    def __init__(self, name, company_id):
        """
        Contructor for a new OwerModel

        :param name:
        :param company_id:
        """
        self.name = name
        self.company_id = company_id

    def __repr__(self):
        return str(self.id)

    @property
    def serialize(self):
        """
        Serialize the Model for the JSON responses

        :return: JSON
        """
        return {
            'name': self.name,
            'company_id': self.company_id,
        }

    def save(self):
        """
        Add/Save a Owner
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete a Owner
        """
        db.session.delete(self)
        db.session.commit()
