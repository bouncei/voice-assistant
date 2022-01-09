from __future__ import print_function
from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import random
from datetime import datetime
from datetime import date

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv("API_KEY")


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTION = ["rd", "th", "st"]

