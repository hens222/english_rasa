import re
import io
import ast
import requests
import numpy as np
import pandas as pd
import random
from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk import FormValidationAction
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
import warnings
from statistics import mean
from os import path, getenv
from datetime import datetime
import matplotlib.pyplot as plt
from botocore.exceptions import ClientError
from boto3.exceptions import S3UploadFailedError
import boto3

class FirstAction(Action):
    def name(self) -> Text:
        return "action_first"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(test="I am the first action")
        return []
