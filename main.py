import requests
from flask import Flask, Response,redirect, request, abort, render_template,render_template_string, send_from_directory
from PIL import Image
import pandas as pd
import os

station_name=['leiden','eindhoven','utrecht','amsterdam']
station_code=['LEDN','EHV','UT','ASD']
df_station = pd.DataFrame(
    {'name': station_name,
     'code': station_code
    })

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])# if HTML contains forms, use GET and Post 
def ns():
    error=None
    stationName = request.args.get('name1', type=str)
    if stationName is None:
        response="what?"
    if type(stationName)==str:
        name_station=df_station.loc[df_station['name'] == stationName, 'code'].values[0]
        username = 'p.kecman@tudelft.nl'
        password = '8NYtYnrTlQCFP7LX33EI-e8lZKj7gcUuqLJf8uHs4vk8_kvWAKoO_g'
        url = 'http://webservices.ns.nl/ns-api-avt?station='+name_station
        response = requests.get(url,auth=requests.auth.HTTPBasicAuth(username,password))#receive HTTp respond code, eg. 200, 401
        response=response.text#receive the content in text
    return render_template('nsdelay.html',error=error, reply=response)

if __name__ == '__main__':
  app.run(debug=True)
