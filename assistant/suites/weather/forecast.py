# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Program Name: forecast.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Derivative of: Google's DialogFlow weather agent
Description: Module that defines the Forecast class and defines helper functions to
process and validate date related to the weather forecast class.  It pulls weather from Yahoo Inc.'s YQL feed via JSON.
"""

import random
from datetime import datetime as dt
from datetime import timedelta
from weather import Weather
from config import (_TEMP_LIMITS, _DEFAULT_TEMP_UNIT)
from weather_responses import (
    LIST_YES,
    LIST_NO,
    LIST_COLD,
    LIST_CHILLY,
    LIST_WARM,
    LIST_HOT,
    WEATHER_CURRENT,
    WEATHER_DATE,
    WEATHER_WEEKDAY,
    WEATHER_DATE_TIME,
    # WEATHER_TIME_PERIOD,
    # WEATHER_TIME_PERIOD_DEFINED,
    # WEATHER_DATE_PERIOD_WEEKEND,
    # WEATHER_DATE_PERIOD,
    WEATHER_ACTIVITY_YES,
    WEATHER_ACTIVITY_NO,
    # RESPONSE_WEATHER_CONDITION,
    RESPONSE_WEATHER_OUTFIT)
from weather_entities import (WINTER_ACTIVITY, SUMMER_ACTIVITY, DEMI_ACTIVITY, UNSUPPORTED, COLD_WEATHER,
                              WARM_WEATHER, HOT_WEATHER, RAIN, SNOW, SUN)


class Forecast(object):
    """The Forecast object implements tracking of and forecast retrieval for
    a request for a weather forecast.  Several methods return various human
    readable strings that contain the weather forecast, condition, temperature
    and the appropriateness of outfits and activities to for forecasted weather.

    Attributes:
        city (str): the city for the weather forecast
        datetime_start (datetime.datetime): forecast start date or datetime
        datetime_end (datetime.datetime): forecast end date or datetime
        unit (str): the unit of temperature: Celsius ('C') or Fahrenheit ('F')
        action (dict): any actions in the request (activity, condition, outfit)
    """

    def __init__(self, params):
        """
        Initializes the Forecast object

        gets the forecast for the provided dates
        """

        self.city = params['city']
        self.datetime_start = params['datetime_start']
        self.datetime_end = params['datetime_end']
        self.unit = params['unit']
        self.action = {
            'activity': params['activity'],
            'condition': params['condition'],
            'outfit': params['outfit'],
        }
        self.weather = Weather()
        self.__get_weather()

    def __get_weather(self):
        location = self.weather.lookup_by_location(str(self.city))
        self.condition = location.condition()
        self.code = self.condition['code']
        self.astronomy = location.astronomy()
        self.atmosphere = location.atmosphere()
        self.units = location.units()
        self.wind = location.wind()
        self.forecasts = location.forecast()

    # def __get_forecast(self):
    #     """
    #     Takes a date or date period and a city
    #
    #     raises an exception when dates are outside what can be forecasted
    #     Returns the weather for the period and city as a dict
    #     """
    #
    #     datetime_start = self.datetime_start
    #     datetime_end = self.datetime_end
    #
    #     if datetime_start and datetime_end:
    #         date_interval = datetime_end - datetime_start
    #         forecast_length = date_interval.days
    #     elif datetime_start:
    #         forecast_length = 1
    #     else:
    #         datetime_start = dt.now().date()
    #         forecast_length = 1
    #
    #     # Get the start date
    #     try:
    #         date_start = datetime_start.date()
    #     except AttributeError:
    #         date_start = datetime_start
    #
    #     # Get the furthest date in the future we can get a forecast for
    #     max_forecast_date = dt.now().date() + timedelta(days=MAX_FORECAST_LEN)
    #     furthest_date_requested = dt.combine(date_start, timedelta(days=forecast_length))
    #
    #     # Check to see that the forecast dates requested are not too far into
    #     # the future
    #     if furthest_date_requested > max_forecast_date:
    #         raise ValueError(
    #             'I couldn\'t find a forecast for that far in the future.')
    #
    #     # Get the weather for each day
    #     for day in self.forecasts:
    #         current_date = date_start + timedelta(days=day)
    #         forecast['weather'].append(day)
    #     return forecast

    # def __call_wwo_api(self, date):
    #     """Calls the wwo weather API for a date
    #
    #     raises an exception for network errors
    #     Returns a dict of the JSON 'data' attribute in the response
    #     """
    #
    #     wwo_data = {
    #         'key': WWO_API_KEY,
    #         'q': self.city,
    #         'format': 'json',
    #         'num_of_days': 1,
    #         'mca': 'no',
    #         'lang': 'en',
    #         'cc': 'yes',
    #         'tp': '1',
    #         'fx': 'yes',
    #         'date': date
    #     }
    #
    #     response = requests.get(
    #         'http://api.worldweatheronline.com/premium/v1/weather.ashx',
    #         params=wwo_data
    #     )
    #
    #     weather_data = response.json()['data']
    #     error = weather_data.get('error')
    #     if error:
    #         raise IOError(error[0]['msg'])
    #     else:
    #         return weather_data

    # def __get_max_min_temp(self):
    #     """Calculate the max and min temperatures for the date range
    #     """
    #
    #     temps = []
    #     for day in self.forecast['weather']:
    #         for hour in day['hourly']:
    #             temps.append(int(hour['temp' + self.unit]))
    #
    #     return (max(temps), min(temps))

    def get_datetime_response(self):
        """Takes a datetime and forecast

        Returns the forecast for that datetime as a string
        """

        max_temp = int(self.forecasts[0].high())
        min_temp = int(self.forecasts[0].low())
        temp = (max_temp + min_temp) / 2
        temperature = str(temp).encode('utf-8') + \
            u'°'.encode('utf-8') + self.unit.encode('utf-8')
        condition = self.forecasts[0].text().lower()

        # Get the start date
        try:
            date_start = self.datetime_start.date()
        except AttributeError:
            date_start = self.datetime_start

        # if the weather forecast is for today and they specified a time
        if (date_start == dt.now().date() and
                isinstance(self.datetime_start, dt)):
            output_string = random.choice(WEATHER_DATE_TIME)
            response = output_string.format(
                place=self.city,
                time=self.datetime_start.strftime('%I:%M%p'),
                temperature=temperature,
                condition=condition,
                day='Today')
        # else
        else:
            # if it's within a week
            time_difference = date_start - dt.now().date()
            if time_difference <= timedelta(days=7):
                # Get the day of the week or set to 'today'
                day = self.datetime_start.strftime('%A')
                if date_start == dt.now().date():
                    day = 'Today'
                # Format Response
                output_string = random.choice(WEATHER_DATE)
                response = output_string.format(
                    place=self.city,
                    day=day,
                    temperature=temperature,
                    condition=condition)
            # if the date is more than a week away
            else:
                output_string = random.choice(WEATHER_WEEKDAY)
                response = output_string.format(
                    place=self.city,
                    condition=condition,
                    temperature=temperature,
                    date=self.datetime_start.strftime('%B %-d'))
        return response

    # def get_datetime_period_response(self):
    #     """Takes a date period and forecast
    #
    #     Returns the forecast for the date period as a string
    #     """
    #
    #     datetime_start = self.datetime_start
    #     datetime_end = self.datetime_end
    #     forecasts = self.forecasts
    #
    #     # datetime period over the same day
    #     if datetime_start.day == datetime_end.day:
    #
    #         # Get the temperature throughout the time period and average it
    #         temps = []
    #         hours = []
    #         # Get the set of hours in military time to average over for the day
    #         for hour in range(datetime_start.hour, datetime_end.hour + 1):
    #             hours.append(str(hour * 100))  # WWO API uses military time
    #         # Get the forecasted temperature for every hour during the period
    #         for hour in forecast['weather'][0]['hourly']:
    #             if hour['time'] in hours:
    #                 temps.append(hour['temp' + self.unit])
    #         # Calculate the average temperature for the time period
    #         avg_temp = sum(temps) / len(temps)
    #         # Make a human readable string of the temperature
    #         temperature = str(avg_temp) + u'°'.encode('utf-8') + self.unit
    #
    #         # Get the conditions for the time period
    #         condition = forecast['weather'][0]['hourly'][
    #             datetime_start.hour + 1]['weatherDesc'][0]['value'].lower()
    #
    #         # Choose the right word to describe the time period
    #         if datetime_start.hour <= 12 and datetime_end.hour <= 16:
    #             time_period = 'afternoon'
    #         elif datetime_start.hour <= 0 and datetime_end.hour <= 8:
    #             time_period = 'night'
    #         elif datetime_start.hour <= 16 and datetime_end.hour <= 23:
    #             time_period = 'tonight'
    #         elif datetime_start.hour <= 8 and datetime_end.hour <= 12:
    #             time_period = 'morning'
    #
    #         # if the time period can be described with a word use it here
    #         if time_period:
    #             output_string = random.choice(
    #                 WEATHER_TIME_PERIOD_DEFINED)
    #             response = output_string.format(
    #                 place=self.city,
    #                 time_period=time_period,
    #                 temperature=temperature,
    #                 condition=condition)
    #
    #         # If the time period cannot be defined by a single word use the
    #         # time the user provided
    #         else:
    #             output_string = random.choice(WEATHER_TIME_PERIOD)
    #             response = output_string.format(
    #                 condition=condition,
    #                 city=self.city,
    #                 temp=temperature,
    #                 time_start=datetime_start.strftime('%I:%M%p'),
    #                 time_end=datetime_end.strftime('%I:%M%p'))
    #
    #     # datetime period over multiple days
    #     else:
    #         # If the user is requesting weather for the weekend
    #         if datetime_start.day == 5 and datetime_end.day == 6:
    #             response = random.choice(WEATHER_DATE_PERIOD_WEEKEND).format(
    #                 city=self.city,
    #                 condition_sun=forecast['weather'][1]['hourly'][
    #                     12]['weatherDesc'][0]['value'].lower(),
    #                 sun_temp_min=forecast['weather'][1]['mintemp' + self.unit],
    #                 sun_temp_max=forecast['weather'][1]['maxtemp' + self.unit],
    #                 condition_sat=forecast['weather'][0]['hourly'][
    #                     12]['weatherDesc'][0]['value'].lower(),
    #                 sat_temp_min=forecast['weather'][0]['mintemp' + self.unit],
    #                 sat_temp_max=forecast['weather'][0]['maxtemp' + self.unit])
    #         # If the user is requesting a non-weekend date range
    #         else:
    #             (max_temp, min_temp) = self.__get_max_min_temp()
    #
    #             # Format temperature strings
    #             max_temp = str(max_temp).encode('utf-8') + \
    #                 u'°'.encode('utf-8') + self.unit.encode('utf-8')
    #             min_temp = str(min_temp).encode('utf-8') + \
    #                 u'°'.encode('utf-8') + self.unit.encode('utf-8')
    #
    #             response = random.choice(WEATHER_DATE_PERIOD).format(
    #                 date_start=datetime_start.strftime('%Y-%m-%d'),
    #                 date_end=datetime_end.strftime('%Y-%m-%d'),
    #                 city=self.city,
    #                 condition=forecast['weather'][0]['hourly'][
    #                     12]['weatherDesc'][0]['value'].lower(),
    #                 degree_list_min=min_temp,
    #                 degree_list_max=max_temp)
    #
    #     return response

    def get_activity_response(self):
        """Takes an activity and a forecast

        returns the appropriateness of activity with the weather as a string
        """

        activity = self.action['activity']

        if activity in DEMI_ACTIVITY:
            resp = random.choice(WEATHER_ACTIVITY_YES).format(
                activity=activity)
        elif activity in WINTER_ACTIVITY:
            if self.forecasts[0].high() <= _TEMP_LIMITS['cold'][self.unit]:
                resp = random.choice(WEATHER_ACTIVITY_YES).format(
                    activity=activity)
            else:
                resp = random.choice(WEATHER_ACTIVITY_NO).format(
                    activity=activity)
        elif activity in SUMMER_ACTIVITY:
            if self.forecasts[0].high() >= _TEMP_LIMITS['warm'][self.unit]:
                resp = random.choice(WEATHER_ACTIVITY_YES).format(
                    activity=activity)
            else:
                resp = random.choice(WEATHER_ACTIVITY_NO).format(
                    activity=activity)
        else:
            resp = 'I don\'t know about %s' % activity

        return resp

    def get_condition_response(self):
        """Takes a condition and returns the probability as a string
        """
        #
        # condition = self.action['condition']
        #
        # if condition in CONDITION_DICT.keys():
        #     condition_chance = self.forecast['weather'][
        #         0]['hourly'][12][CONDITION_DICT[condition]]
        #     resp = random.choice(RESPONSE_WEATHER_CONDITION).format(
        #         condition_original=condition,
        #         condition=condition_chance
        #     )
        # else:
        #     resp = 'I don\'t know about %s' % condition

        return self.forecasts[0].text()

    def get_outfit_response(self):
        """Takes an outfit and a forecast

        returns the appropriateness of outfit with the weather as a string
        """

        outfit = self.action['outfit']
        condition = self.action['condition']
        max_temp = self.forecasts[0].high()
        min_temp = self.forecasts[0].low()
        condition_chance = None

        if outfit in COLD_WEATHER:
            answer = LIST_YES if min_temp < _TEMP_LIMITS[
                'chilly'][self.unit] else LIST_NO
        elif outfit in WARM_WEATHER:
            answer = LIST_YES if max_temp < _TEMP_LIMITS[
                'warm'][self.unit] else LIST_NO
        elif outfit in HOT_WEATHER:
            answer = LIST_YES if max_temp < _TEMP_LIMITS[
                'hot'][self.unit] else LIST_NO
        elif outfit in RAIN:
            condition = 'rain'
            rain_conditions = [0, 1, 2, 3, 4, 6, 9, 11, 12, 37, 38, 39, 40, 45, 47]
            answer = LIST_YES if rain_conditions.__contains__(self.code) else LIST_NO
        elif outfit in SNOW:
            condition = 'snow'
            snow_conditions = [5, 7, 8, 10, 13, 14, 15, 16, 17, 18, 19, 25, 41, 42, 43, 46]
            answer = LIST_YES if snow_conditions.__contains__(self.code) else LIST_NO
        elif outfit in SUN:
            condition = 'sunshine'
            sun_conditions = [29, 30, 31, 32, 33, 34, 36]
            answer = LIST_YES if sun_conditions.__contains__(self.code) else LIST_NO
        else:
            return 'I don\'t know about %s' % outfit

        if condition_chance:
            return random.choice(RESPONSE_WEATHER_OUTFIT).format(
                condition_original=condition,
                condition=condition_chance,
                answer=random.choice(answer))
        else:
            return random.choice(answer)

    def get_temperature_response(self):
        """Takes a temperature and indicates its severity in a string
        """

        temp = self.condition['temp']

        if temp >= _TEMP_LIMITS['hot'][self.unit]:
            resp = LIST_HOT
        elif temp > _TEMP_LIMITS['chilly'][self.unit]:
            resp = LIST_WARM
        elif temp > _TEMP_LIMITS['cold'][self.unit]:
            resp = LIST_CHILLY
        else:
            resp = LIST_COLD

        return random.choice(resp)

    def get_current_response(self):
        """Takes a forecast and returns the current conditions as a string
        """

        # Get the temperature by average the high and low for the day
        temp = self.condition['temp']
        temperature = temp.encode(
            'utf-8') + u'°'.encode('utf-8') + self.unit.encode('utf-8')

        # Get the conditions in the middle of the day
        condition = self.condition['text']

        output_string = random.choice(WEATHER_CURRENT)

        return output_string.format(
            place=self.city,
            temperature=temperature,
            condition=condition
        )


def validate_params(parameters):
    """Takes a list of parameters from a HTTP request and validates them

    Returns a string of errors (or empty string) and a list of params
    """

    # Initialize error and params
    error_response = ''
    params = {}

    # City
    if (parameters.get('address') and
            isinstance(parameters.get('address'), dict)):
        params['city'] = parameters.get('address').get('city')
    else:
        params['city'] = None
        error_response += 'please specify city '

    # Date-time and date-periods
    if parameters.get('date-time') or parameters.get('date-period'):
        # Get the date time or date period (can't be both)
        if parameters.get('date-time'):
            datetime_input = parameters.get('date-time')
        else:
            datetime_input = parameters.get('date-period')

        datetime_start, datetime_end = parse_datetime_input(datetime_input)
        params['datetime_start'] = datetime_start
        params['datetime_end'] = datetime_end

    # Unit
    params['unit'] = parameters.get('unit')
    if not params['unit'] and _DEFAULT_TEMP_UNIT:
        params['unit'] = _DEFAULT_TEMP_UNIT

    # activity
    if parameters.get('activity'):
        activity = parameters.get('activity')
        if (activity not in SUMMER_ACTIVITY and
                activity not in WINTER_ACTIVITY and
                activity not in DEMI_ACTIVITY):
            error_response += 'unknown activity '
    params['activity'] = parameters.get('activity')

    # condition
    params['condition'] = parameters.get('condition')
    if params['condition'] in UNSUPPORTED:
        error_response += 'unsupported condition '

    # outfit
    params['outfit'] = parameters.get('outfit')

    # Special parameters
    # activity
    params['activity'] = parameters.get('activity')

    # condition
    params['condition'] = parameters.get('condition')

    return error_response.strip(), params


def parse_datetime_input(datetime_input):
    """Takes a string containing date/time and intervals in ISO-8601 format

    Returns a start and end Python datetime.datetime object
    datetimes are None if the string is not a date/time
    datetime_end is None if the string is not a date/time interval
    """

    # Date time
    # If the string is length 8 datetime_input has the form 17:30:00
    if len(datetime_input) == 8:
        # if only the time is provided assume its for the current date
        current_date = dt.now().strftime('%Y-%m-%dT')

        datetime_start = dt.strptime(
            current_date + datetime_input,
            '%Y-%m-%dT%H:%M:%S')
        datetime_end = None
    # If the string is length 10 datetime_input has the form 2014-08-09
    elif len(datetime_input) == 10:
        datetime_start = dt.strptime(datetime_input, '%Y-%m-%d').date()
        datetime_end = None
    # If the string is length 20 datetime_input has the form
    # 2014-08-09T16:30:00Z
    elif len(datetime_input) == 20:
        datetime_start = dt.strptime(datetime_input, '%Y-%m-%dT%H:%M:%SZ')
        datetime_end = None

    # Date Periods
    # If the string is length 17 datetime_input has the form
    # 13:30:00/14:30:00
    elif len(datetime_input) == 17:
        # if only the time is provided assume its for the current date
        current_date = dt.now().strftime('%Y-%m-%dT')

        # Split date into start and end times
        datetime_input_start = datetime_input.split('/')[0]
        datetime_input_end = datetime_input.split('/')[1]

        datetime_start = dt.strptime(
            current_date + datetime_input_start, '%Y-%m-%dT%H:%M:%S')
        datetime_end = dt.strptime(
            current_date + datetime_input_end, '%Y-%m-%dT%H:%M:%S')
    # If the string is length 21 datetime_input has the form
    # 2014-01-01/2014-12-31
    elif len(datetime_input) == 21:
        # Split date into start and end times
        datetime_input_start = datetime_input.split('/')[0]
        datetime_input_end = datetime_input.split('/')[1]

        datetime_start = dt.strptime(
            datetime_input_start, '%Y-%m-%d').date()
        datetime_end = dt.strptime(datetime_input_end, '%Y-%m-%d').date()
    # If the string is length 41 datetime_input has the form
    # 2017-02-08T08:00:00Z/2017-02-08T12:00:00Z
    elif len(datetime_input) == 41:
        # Split date into start and end times
        datetime_input_start = datetime_input.split('/')[0]
        datetime_input_end = datetime_input.split('/')[1]

        datetime_start = dt.strptime(
            datetime_input_start, '%Y-%m-%dT%H:%M:%SZ')
        datetime_end = dt.strptime(
            datetime_input_end, '%Y-%m-%dT%H:%M:%SZ')
    else:
        datetime_start = None
        datetime_end = None

    return datetime_start, datetime_end
