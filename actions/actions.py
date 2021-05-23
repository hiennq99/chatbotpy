from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import re

class info:
    def __init__(self, key, value, score, localtion):
        self.key = key
        self.value = value
        self.score = score
        self.localtion = localtion

list_info = []

list_info.append(info('CNTT','2','21.5','Hà Nam'))
list_info.append(info('Cơ khí','2','24','Hà nội'))

class ActionTesting(Action):
    def name(self) -> Text:
        return "action_test"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        text_input = text.lower()
        check = False
        print(tracker.latest_message['intent'].get('name'))
        dispatcher.utter_message("Nội dung bạn muốn con bot trả lời" + text + list_info[0].key)       
