from marshmallow import Schema, fields 


class StoreInfoSchema(Schema):
    id = fields.Integer(dump_only=True)
    tipo_piatto_principale = fields.Str()
    prezzo_piatto_principale = fields.Float()
    voto_piatto_principale = fields.Float()
    voto_medio = fields.Float()
    distanza_dal_centro = fields.Float(allow_none=True)



class StoreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    type = fields.Str()
    address = fields.Str()
    info = fields.Nested(StoreInfoSchema, only=(
        "tipo_piatto_principale", 
        "prezzo_piatto_principale", 
        "voto_piatto_principale", 
        "voto_medio",
        "distanza_dal_centro")
         )
