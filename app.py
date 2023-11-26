
from flask import Flask, request , jsonify
from flask_smorest import Api
from flask_marshmallow import Marshmallow
from schemas import StoreSchema
from db import db
from ma import ma
import models


######################################################
######################################################
# APP SETTING
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
db.init_app(app)
ma.init_app(app)
with app.app_context():
    db.create_all()
# FINE SETTING
######################################################
######################################################







######################################################
######################################################
# ROUTES
@app.route('/', methods=["GET"])
def index():
    return "Homepage"



@app.route('/stores', methods=["GET"])
def get_stores():
        stores = models.StoreModel.query.all()
        schema =  StoreSchema(many=True)
        stores = schema.dump(stores)
        if stores:
            return jsonify(stores), 200
        return jsonify(stores) ,  404



@app.route('/stores', methods=["POST"])
def load_stores():

    data = request.get_json()
    if not data:
        return jsonify({"msg": "no data found on json"}), 400
    try:    
        schema = StoreSchema(many=True)
        stores = schema.load(data)
    except:
        return jsonify({"msg": "bad request"}), 400




    store_obj_list = []
    for store in stores:
        tmp = {**store}
        my_store_obj = models.StoreModel(
            name=tmp['name'], 
            type=tmp['type'], 
            address=tmp['address'], 
            info=models.InfoModel(**tmp['info'])
        )
        store_obj_list.append(my_store_obj)




    try:
        db.session.add_all(store_obj_list)
        db.session.commit()
    except:
        return jsonify({"msg":"en error occured while saving data on db"}), 404


    return jsonify(data), 201

# END ROUTES
######################################################
######################################################




if __name__ == '__main__':
    app.run()

