
from db import db



class InfoModel(db.Model):
    __tablename__ = "infos"

    id = db.Column(db.Integer, primary_key=True)
    tipo_piatto_principale = db.Column(db.String())
    prezzo_piatto_principale = db.Column(db.Float(precision=2))
    voto_piatto_principale = db.Column(db.Float(precision=2))
    voto_medio = db.Column(db.Float(precision=2))
    distanza_dal_centro = db.Column(db.Float(precision=10))

    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )
    store = db.relationship("StoreModel", back_populates="info")


