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
from weather import Weather
from weather_responses import (
    WEATHER_ACTIVITY_YES,
    WEATHER_ACTIVITY_NO,
    LIST_YES,
    LIST_NO,
    LIST_COLD,
    LIST_CHILLY,
    LIST_WARM,
    LIST_HOT,
    WEATHER_CURRENT,
    WEATHER_DATE)
from weather_entities import (
    WINTER_ACTIVITY,
    SUMMER_ACTIVITY,
    DEMI_ACTIVITY,
    UNSUPPORTED,
    COLD_WEATHER,
    WARM_WEATHER,
    HOT_WEATHER,
    RAIN,
    SNOW,
    SUN)

# ---- Constants ----
MAX_FORECAST_LEN = 5
DEFAULT_TEMP_UNIT = 'F'
TEMP_LIMITS = {
    'hot': {'C': 25, 'F': 77},
    'warm': {'C': 15, 'F': 59},
    'chilly': {'C': 15, 'F': 41},
    'cold': {'C': -5, 'F': 23}
}
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class Forecast(object):
    """The Forecast object implements tracking of and forecast retrieval for
    a request for a weather forecast.  Several methods return various human
    readable strings that contain the weather forecast, condition, temperature
    and the appropriateness of outfits and activities to for forecasted weather.

    Attributes:
        city (str): the city for the weather forecast
        date_start (datetime.datetime): forecast start date or datetime
        unit (str): the unit of temperature: Celsius ('C') or Fahrenheit ('F')
        action (dict): any actions in the request (activity, condition, outfit)
    """

    def __init__(self, params):
        """Initializes the Forecast object. Gets the forecast for the provided dates"""
        self.city = params['city']
        self.date_start = params['datetime_start']
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

    def get_date_response(self):
        """Takes a date and forecast
        :returns the forecast for that datetime as a string
        """
        try:
            date_start = self.date_start.date()
        except AttributeError:
            date_start = self.date_start
        days_from_today = date_start - dt.now().date()
        if days_from_today == 0:  # Today
            date = "Today"
        elif days_from_today == 1:  # Tomorrow
            date = "Tomorrow"
        elif days_from_today < 0:  # In the past
            return "I do not remember what the weather was on that day."
        elif days_from_today > MAX_FORECAST_LEN:  # Too far in the future
            return "I cannot look that far into the future."
        else:  # Another day of the week
            date = "on " + DAYS_OF_WEEK[date_start.weekday()]
        output_string = random.choice(WEATHER_DATE)
        response = output_string.format(
            day=date,
            place=self.city,
            high=self.forecasts[0].high(),
            low=self.forecasts[0].low(),
            condition=self.forecasts[0].text())
        return response

    def get_activity_response(self):
        """Takes an activity and a forecast

        returns the appropriateness of activity with the weather as a string
        """

        activity = self.action['activity']

        if activity in DEMI_ACTIVITY:
            resp = random.choice(WEATHER_ACTIVITY_YES).format(
                activity=activity)
        elif activity in WINTER_ACTIVITY:
            if self.forecasts[0].high() <= TEMP_LIMITS['cold'][self.unit]:
                resp = random.choice(WEATHER_ACTIVITY_YES).format(
                    activity=activity)
            else:
                resp = random.choice(WEATHER_ACTIVITY_NO).format(
                    activity=activity)
        elif activity in SUMMER_ACTIVITY:
            if self.forecasts[0].high() >= TEMP_LIMITS['warm'][self.unit]:
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
        """Takes an outfit and a forecast.
        :returns the appropriateness of outfit with the weather as a string
        """
        outfit = self.action['outfit']
        max_temp = self.forecasts[0].high()
        min_temp = self.forecasts[0].low()

        if outfit in COLD_WEATHER:
            answer = LIST_YES if min_temp < TEMP_LIMITS[
                'chilly'][self.unit] else LIST_NO
        elif outfit in WARM_WEATHER:
            answer = LIST_YES if max_temp < TEMP_LIMITS[
                'warm'][self.unit] else LIST_NO
        elif outfit in HOT_WEATHER:
            answer = LIST_YES if max_temp < TEMP_LIMITS[
                'hot'][self.unit] else LIST_NO
        elif outfit in RAIN:
            rain_conditions = [0, 1, 2, 3, 4, 6, 9, 11, 12, 37, 38, 39, 40, 45, 47]
            answer = LIST_YES if rain_conditions.__contains__(self.code) else LIST_NO
        elif outfit in SNOW:
            snow_conditions = [5, 7, 8, 10, 13, 14, 15, 16, 17, 18, 19, 25, 41, 42, 43, 46]
            answer = LIST_YES if snow_conditions.__contains__(self.code) else LIST_NO
        elif outfit in SUN:
            sun_conditions = [29, 30, 31, 32, 33, 34, 36]
            answer = LIST_YES if sun_conditions.__contains__(self.code) else LIST_NO
        else:
            return 'I don\'t know about %s' % outfit
        return random.choice(answer)

    def get_temperature_response(self):
        """Takes a temperature and indicates its severity in a string
        """

        temp = self.condition['temp']

        if temp >= TEMP_LIMITS['hot'][self.unit]:
            resp = LIST_HOT
        elif temp > TEMP_LIMITS['chilly'][self.unit]:
            resp = LIST_WARM
        elif temp > TEMP_LIMITS['cold'][self.unit]:
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

        response = output_string.format(
            place=self.city,
            temperature=temperature,
            condition=condition)
        return response


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
    if not params['unit'] and DEFAULT_TEMP_UNIT:
        params['unit'] = DEFAULT_TEMP_UNIT

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
