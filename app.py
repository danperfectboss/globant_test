from crypt import methods
from distutils.log import debug
from operator import ge
import requests
from flask import Flask, jsonify, request, redirect
from datetime import datetime, date

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def initial():
    return redirect('/get?city=Mexico&country=mx')

@app.route('/get', methods=['GET'])
def get_info():
    '''Function recieves 2 params city and country, get the data from 
    open weather and return especific response readable for the customer.
    In the function includes the api_key '''

    # Read te parms from the URL
    city = str(request.args['city'])
    country = str(request.args['country'])
    # Set the api key
    api_key='ae04adb9c42f89a204fc46f734519610'
    # Set the URl parameterized
    url =  'http://api.openweathermap.org/data/2.5/weather?q=%s,%s&APPID=%s'%(city,country,api_key)
    # Get the data by the request
    data = requests.get(url).json()

    #Validate the response code for the request 
    if str(data['cod']) != '200':
        return "Please enter a valid value for city or country: "+ data['message']
    
    return jsonify({'Response':buil_response(data)})
    
def buil_response(data):
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%Y-%m-%d")
    

    Response = {
            'location_name':data['name'] +' , '+ str(data['sys']['country']).lower(),
            'temperature':str(kelvin_to_celcius(data['main']['temp']))+' Grados Celcius',
            'wind': str(data['wind']['speed']) + ' m/s',
            'cloudiness':str(data['weather'][0]['description']).capitalize(),
            'pressure': str(data['main']['pressure'])+ ' hpa',
            'humidity':str(data['main']['humidity']) + '%',
            'sunrise': transform_unix_to_cst(data['sys']['sunrise']),
            'sunset': transform_unix_to_cst(data['sys']['sunset']),
            'geo_coordinates': '['+ str(data['coord']['lat'])+', ' + str(data['coord']['lon']) +']',
            'requested_time':d1+" "+datetime.now().strftime('%H:%M:%S')
        }

    return Response


def transform_unix_to_cst(hour):
        '''Transforma las horas que viene en formato unix a utc'''

        hour = int(hour)
        #se hace la resta por 21600 ya que representa UTC-6 y con esto tenemos la hora exacta del centro
        hour = hour - 21600 

        #no transforma hora en negativos ni en cero
        if(hour != 0):
            hour = datetime.utcfromtimestamp(hour).strftime('%H:%M:%S')
            # hour = timezone('US/Central').localize(hour)

        return hour

#función que transforma los grados de kelvin a celcius
def kelvin_to_celcius(temp):
    temp = float(temp)
    celcius = temp - 273.15

    return round(celcius,2)

#Run the app in the localhost port 4000   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)