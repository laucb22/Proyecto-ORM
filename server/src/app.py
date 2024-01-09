import initialize as init
from flask import Flask
from flask import jsonify
import controllers.brands as brands
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)

@app.route("/")
def helloworld():
    brands_to_send = brands.get_brands()
    brands_to_send = [model_to_dict(brand) for brand in brands_to_send]

    return brands_to_send



if __name__ == "__main__":
    app()