# suite.file
"""
Program Name: weathersuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of responses and functions pertaining to processing weather commands.
"""

import dialogflow
import json

from flask import Flask, make_response, jsonify  # request
from weather.forecast import Forecast, validate_params

APP = Flask(__name__)
LOG = APP.logger

CLIENT_ACCESS_TOKEN = '0559826f1eca414da768262a971df1f8'


class WeatherSuite:
    def __init__(self):
        """Initializes DialogFlow agent"""
        self.agent = dialogflow.Agent(CLIENT_ACCESS_TOKEN)
        self.response = ""
        self.action = ""

    def checkcommand(self, usermsg):
        """
        Sends the DialogFlow agent a message and speaks the response.
        :param usermsg: The message that the user inputted
        :returns response if found
        :returns None if no response is found
        """
        self.agent.sendcommand(usermsg)
        req = self.agent.response
        try:
            action = req.get('result').get('action')
        except AttributeError:
            return 'json error'

        if action == 'weather':
            res = weather(req)
        elif action == 'weather.activity':
            res = weather_activity(req)
        elif action == 'weather.condition':
            res = weather_condition(req)
        elif action == 'weather.outfit':
            res = weather_outfit(req)
        elif action == 'weather.temperature':
            res = weather_temperature(req)
        else:
            return None

        self.response = res
        self.action = action
        print ("Action = " + action)
        return res


def weather(req):
    """Returns a string containing text with a response to the user
    with the weather forecast or a prompt for more information

    Takes the city for the forecast and (optional) dates
    uses the template responses found in weather_responses.py as templates
    """
    parameters = req['result']['parameters']

    print 'API.AI Parameters:'
    print json.dumps(parameters, indent=4)

    # validate request parameters, return an error if there are issues
    error, forecast_params = validate_params(parameters)
    if error:
        return error

    # create a forecast object which retrieves the forecast from a external API
    try:
        forecast = Forecast(forecast_params)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error

    # If the user requests a datetime period (a date/time range), get the
    # response
    if forecast.date_start and forecast.date_end:
        response = forecast.get_date_period_response()
    # If the user requests a specific datetime, get the response
    elif forecast.date_start:
        response = forecast.get_date_response()
    # If the user doesn't request a date in the request get current conditions
    else:
        response = forecast.get_current_response()

    return response


def weather_activity(req):
    """Returns a string containing text with a response to the user
    with a indication if the activity provided is appropriate for the
    current weather or a prompt for more information

    Takes a city, activity and (optional) dates
    uses the template responses found in weather_responses.py as templates
    and the activities listed in weather_entities.py
    """

    # validate request parameters, return an error if there are issues
    error, forecast_params = validate_params(req['result']['parameters'])
    if error:
        return error

    # Check to make sure there is a activity, if not return an error
    if not forecast_params['activity']:
        return 'What activity were you thinking of doing?'

    # create a forecast object which retrieves the forecast from a external API
    try:
        forecast = Forecast(forecast_params)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error

    # get the response
    return forecast.get_activity_response()


def weather_condition(req):
    """Returns a string containing a human-readable response to the user
    with the probability of the provided weather condition occurring
    or a prompt for more information

    Takes a city, condition and (optional) dates
    uses the template responses found in weather_responses.py as templates
    and the conditions listed in weather_entities.py
    """

    # validate request parameters, return an error if there are issues
    error, forecast_params = validate_params(req['result']['parameters'])
    if error:
        return error

    # Check to make sure there is a activity, if not return an error
    if not forecast_params['condition']:
        return 'What weather condition would you like to check?'

    # create a forecast object which retrieves the forecast from a external API
    try:
        forecast = Forecast(forecast_params)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error

    # get the response
    return forecast.get_condition_response()


def weather_outfit(req):
    """Returns a string containing text with a response to the user
    with a indication if the outfit provided is appropriate for the
    current weather or a prompt for more information

    Takes a city, outfit and (optional) dates
    uses the template responses found in weather_responses.py as templates
    and the outfits listed in weather_entities.py
    """

    # validate request parameters, return an error if there are issues
    error, forecast_params = validate_params(req['result']['parameters'])
    if error:
        return error

    # Validate that there are the required parameters to retrieve a forecast
    if not forecast_params['outfit']:
        return 'What are you planning on wearing?'

    # create a forecast object which retrieves the forecast from a external API
    try:
        forecast = Forecast(forecast_params)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error

    return forecast.get_outfit_response()


def weather_temperature(req):
    """Returns a string containing text with a response to the user
    with a indication if temperature provided is consisting with the
    current weather or a prompt for more information

    Takes a city, temperature and (optional) dates.  Temperature ranges for
    hot, cold, chilly and warm can be configured in config.py
    uses the template responses found in weather_responses.py as templates
    """

    parameters = req['result']['parameters']

    # validate request parameters, return an error if there are issues
    error, forecast_params = validate_params(parameters)
    if error:
        return error

    # If the user didn't specify a temperature, get the weather for them
    if 'temperature' not in forecast_params:
        return weather(req)

    # create a forecast object which retrieves the forecast from a external API
    try:
        forecast = Forecast(forecast_params)
    # return an error if there is an error getting the forecast
    except (ValueError, IOError) as error:
        return error

    return forecast.get_temperature_response()
