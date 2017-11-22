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

"""This module defines the entities that can be responded to for activities,
conditions and outfits.

This is meant to be used with the sample weather agent for API.AI, located at
https://console.api.ai/api-client/#/agent//prebuiltAgents/Weather
"""

# activity
WINTER_ACTIVITY = [
    'skiing',
    'snowboarding',
    'snowball fighting',
    'snowball fights'
]

SUMMER_ACTIVITY = [
    'cycling',
    'run',
    'swimming',
    'jogging',
    'hiking',
    'skating',
    'parasailing',
    'windsurfing',
    'kayaking',
    'mountain biking',
    'surfing',
    'frisbee',
    'camping',
    'football',
    'tennis',
    'soccer'
]

DEMI_ACTIVITY = [
    'sightseeing',
    'birdwatching',
    'tree climbing',
]

# conditions

CONDITION_DICT = {
    'rain': 'chanceofrain',
    'snow': 'chanceofsnow',
    'wind': 'chanceofwindy',
    'sun': 'chanceofsunshine',
    'fog': 'chanceoffog',
    'foggy': 'chanceoffog',
    'thunderstorm': 'chanceofthunder',
    'overcast': 'chanceofovercast',
    'clouds': 'cloudcover',
}

SUPPORTED = [
    'rain',
    'snow',
    'wind',
    'sun',
    'fog',
    'thunderstorm',
    'overcast',
    'clouds',
    'foggy',
]

UNSUPPORTED = [
    'shower',
    'ice',
    'freezing rain',
    'rain snow',
    'haze',
    'smoke',
]

# outfit
COLD_WEATHER = [
    'coat',
    'jacket',
    'wool socks',
    'wool cap',
    'turtleneck',
    'thermal pants',
    'sweatshirt',
    'sweatpants',
    'sweater',
    'snowboard pants',
    'ski pants',
    'shawls',
    'scarf',
    'jumper',
    'balaclava',
    'beanie',
    'boots',
    'cardigan',
    'fleece top',
    'gloves',
    'parca',
    'jeans',
    'jacket'
]
CHILLY_WEATHER = [
    'coat',
    'jacket',
    'wool socks',
    'sweatshirt',
    'sweatpants',
    'sweater',
    'scarf',
    'boots',
    'cardigan',
    'fleece top',
    'gloves',
    'leggings',
    'jeans',
    'jacket'
]

COOL_WEATHER = [
    'coat',
    'dress pants',
    'dress shirt',
    'jacket',
    'wool socks',
    'sweat shirt',
    'sweat pants',
    'sweater',
    'scarf',
    'boots',
    'cardigan',
    'fleece top',
    'jacket',
    'hoodie',
    'vest',
    'leggings',
    'quarter zip',
    'pull over'
]

WARM_WEATHER = [
    'tennis shoes',
    'lounge wear',
    'socks',
    'sneakers',
    'sleeve shirt',
    'casual shirt',
    'sneakers',
    'shorts',
    't-shirt',
    'tee shirt',
    'dress',
    'gum boots',
    'hat'
]

HOT_WEATHER = [
    'tank top',
    't-shirt',
    'tee shirt',
    'swimwear',
    'swimsuit',
    'swim suite',
    'swim goggles',
    'sunscreen',
    'skirt',
    'shorts',
    'bathing suit',
    'capri',
    'flips flops',
    'pool shoes',
    'sandals',
    'slippers',
]

UNKNOWN_WEATHER = [
    'underwear',
    'tie',
    'neck gaiter',
    'pajama',
    'sleepwear',
    'suit',
]

RAIN = [
    'umbrella',
    'coat',
    'gum boots',
    'hat',
    'jacket',
    'rain coat',
    'rain jacket',
    'rain pants',
]

SNOW = [
    'gloves',
    'fleece top',
    'ski pants',
    'snowboard pants',
]

SUN = [
    'swimwear',
    'swim goggles',
    'bathing suit',
    'flips flops',
    'sandals',
    'sunglasses',
    'sunscreen',
]
