#!/bin/sh
sudo apt-get -y install python-pip python-dev build-essential
sudo apt-get -y install python-pip
sudo apt-get -y install python
sudo apt-get -y install python-pyaudio python3-pyaudio
sudo apt-get -y install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get -y install ffmpeg libav-tools
sudo apt-get -y install -qq swig libpulse-dev
sudo apt-get -y install flac
sudo apt-get -y install python-bs4
sudo apt-get -y install pygame
sudo apt-get -y install python-pyglet
sudo apt-get -y install youtube-dl

sudo -H pip install --upgrade virtualenv
sudo -H pip install future --upgrade
sudo -H pip install pyaudio
sudo -H pip install pocketsphinx
sudo -H pip install google-api-python-client
sudo -H pip install monotonic
sudo -H pip install SpeechRecognition
sudo -H pip install pafy
sudo -H pip install python-vlc
sudo -H pip install chatterbot
sudo -H pip install gTTS
sudo -H pip install pygame
sudo -H pip install slackclient
sudo -H pip install apiai
sudo -H pip install flask
sudo -H pip install geocoder

echo !!!!!!!KAREN dependencies installed. Adjust microphone index within code.!!!!!!!!

