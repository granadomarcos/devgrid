# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, jsonify, render_template, request, Response, flash, redirect, url_for, abort
#from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from geoalchemy2 import Geometry
from sqlalchemy import Column
import requests
import json
from datetime import datetime




# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
#moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
#migrate = Migrate(app, db)


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

class WeatherInfo(db.Model):
    
    user_id     = db.Column(db.Integer, unique=True, primary_key=True)
    city_id     = db.Column(db.Integer, unique=True, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity    = db.Column(db.Float, nullable=False)
    timestamp   = db.Column(db.DateTime, nullable=True)
 
    def __repr__(self):
        return '<weather_info %r>' % self.user_id

db.create_all()	


# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


id_list = '3440645'
@app.route('/')
def index():
    url = "https://api.openweathermap.org/data/2.5/group?id="+id_list+"&units=metric&appid=746b57df577be4b85706eebc87f77825"
    print(url)
    response = requests.get(url)
    data = response.json() 
    print(data)
    for i in range(0,len(data)+1):
        try:       
            temperature = data['list'][i]['main']["temp"]
            humidity    = data['list'][i]['main']["humidity"]
            city_id     = data['list'][i]['id']
            timestamp   = data['list'][i]['dt']
            print(temperature)
            weather = WeatherInfo(
                        temperature = temperature,
                        humidity    = humidity,
                        city_id     = city_id,
                        timestamp   = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                        )
            print(weather)       
            db.session.add(weather)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
    return jsonify({'Weather': data})

#if __name__ == "__main__":
#    app.run(debug=True)