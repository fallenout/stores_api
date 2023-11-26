from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), )
    address = db.Column(db.String(), )
    info = db.relationship("InfoModel", uselist=False, back_populates="store", lazy="joined")
