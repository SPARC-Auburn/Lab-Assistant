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

"""This module defines the text based template responses to be formatted
and sent to users with the proper data

This is meant to be used with the sample weather agent for API.AI, located at
https://console.api.ai/api-client/#/agent//prebuiltAgents/Weather
"""

WEATHER_ACTIVITY_YES = [
    'What a nice weather for {activity}!'
]

WEATHER_ACTIVITY_NO = [
    'Not the best weather for {activity}.'
]

LIST_YES = [
    'Better have it with you, just in case.',
    'It never hurts to be extra prepared.',
    'Considering the forecast, I\'m going to say yes.',
    'Definitely!',
    'That\'s not a bad idea.'
]

LIST_NO = [
    'No, you should be fine without it.',
    'I don\'t think that will be necessary.',
    'You can bring it if you like, but I doubt you\'ll need it.',
    'It seems pretty unlikely you\'ll need that.'
]

LIST_COLD = [
    'Quite cold out there.',
    'Pretty freezing, I would say.',
    'Don\'t forget your gloves.'
]

LIST_CHILLY = [
    'Quite chilly.',
    'You\'ll need a jacket for sure.'
]

LIST_COOL = [
    'I would say it is a little cool.',
    'It\'s not the warmest of days'
]

LIST_WARM = [
    'Temperature is quite nice.',
    'It is a little warm outside.',
]

LIST_HOT = [
    'Oh, that\'s hot!',
    'You\'ll definitely need sunscreen.'
]

WEATHER_CURRENT = [
    'The temperature in {place} now is {temperature} and {condition}.',
    'Right now it\'s {temperature} and {condition} in {place}.',
    'It\'s currently {temperature} and {condition} in {place}.',
    'The temperature in {place} is {temperature} and {condition}.'
]

WEATHER_DATE = [
    '{place}, {day} will have temperatures ranging between {high} and {low} and will have {condition} conditions.',
    'Expect in {place} {day} to have a high of {high} and a low of {low} along with {condition} conditions.'
]

RESPONSE_WEATHER_CONDITION = [
    'It is {condition} outside.',
    'There\'s a pretty good chance it\'s {condition} outside.'
]