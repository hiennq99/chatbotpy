from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json
import re

class info:
    def __init__(self, key, value, score, location):
        self.key = key
        self.value = value
        self.score = score
        self.location = location

list_info = []

list_info.append(info('Công nghệ thông tin','2','25','Năm 1: Hà Nam, Năm 2,3,4: Hà Nội Khu A'))
list_info.append(info('Cơ khí','2','26','Năm 1: Hà Nam, Năm 2,3,4: Hà Nội Khu A'))
list_info.append(info('Quản trị khih doanh','2','24','Năm 1: Hà Nam, Năm 2,3,4: Hà Nội Khu A'))
list_info.append(info('Điện','2','23','Năm 1: Hà Nam, Năm 2,3,4: Hà Nội Khu A'))
list_info.append(info('Cơ điện tử','2','22','Năm 1: Hà Nam, Năm 2,3,4: Hà Nội Khu A'))
list_info.append(info('May','2','22','Năm 1,2,3,4 : Hà Nội Khu B'))

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

class ActionGetScore(Action):
    def name(self) -> Text:
        return "action_score"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        text_input = text.lower()
        if 'CNTT' in text or 'Công nghệ thông tin' in text or 'cntt' in text or 'cong nghe thong tin' in text or 'công nghệ thông tin' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Điểm của khoa công nghệ thông tin là: " + list_info[0].score)

        if 'CK' in text or 'Cơ khí' in text or 'ck' in text or 'co khi' in text or 'cơ khí' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Điểm của khoa cơ khí là: " + list_info[1].score)
        
        if 'QTKD' in text or 'Quản trị kinh doanh' in text or 'qtkd' in text or 'quan tri kinh doanh' in text or 'quản trị kinh doanh' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Điểm của khoa quản trị kinh doanh là: " + list_info[2].score)

        if 'Điện' in text or 'điện' in text or 'qtkd' in text or 'dien' in text or 'Điệnn' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Điểm của khoa điện là: " + list_info[3].score)
        
        if 'Cơ điện tử' in text or 'cơ điện tử' in text or 'cđt' in text or 'cdt' in text or 'co dien tu' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Điểm của khoa cơ điện tử là: " + list_info[3].score)
        
        if 'May' in text or 'may' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Điểm của khoa may là: " + list_info[3].score)

class ActionGetLocaiton(Action):
    def name(self) -> Text:
        return "action_location"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        text_input = text.lower()
        if 'CNTT' in text or 'Công nghệ thông tin' in text or 'cntt' in text or 'cong nghe thong tin' in text or 'công nghệ thông tin' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Khoa công nghệ thông tin học ở: " + list_info[0].location)

        if 'CK' in text or 'Cơ khí' in text or 'ck' in text or 'co khi' in text or 'cơ khí' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Khoa cơ khí học ở: " + list_info[1].location)
        
        if 'QTKD' in text or 'Quản trị kinh doanh' in text or 'qtkd' in text or 'quan tri kinh doanh' in text or 'quản trị kinh doanh' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Khoa quản trị kinh doanh học ở: " + list_info[2].location)

        if 'Điện' in text or 'điện' in text or 'qtkd' in text or 'dien' in text or 'Điệnn' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Khoa điện học ở: " + list_info[3].location)
        
        if 'Cơ điện tử' in text or 'cơ điện tử' in text or 'cđt' in text or 'cdt' in text or 'co dien tu' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Khoa cơ điện tử học ở: " + list_info[3].location)
        
        if 'May' in text or 'may' in text:
            print(tracker.latest_message['intent'].get('name'))
            dispatcher.utter_message("Khoa may học ở: " + list_info[3].location)

class ActionGetScore(Action):
    def name(self) -> Text:
        return "action_ask_profile"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        text_input = text.lower()
        