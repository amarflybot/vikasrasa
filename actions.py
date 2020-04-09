# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
#
#
# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

class ActionDefault(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):

        print("In action_default_fallback")
        return []


class ActionRecordOracleInvoice(Action):

    def name(self) -> Text:
        return "action_record_invoice"

    def run(self, dispatcher, tracker, domain):

        print("In action_record_invoice")

        value = tracker.latest_message['text']
        dispatcher.utter_template("utter_oracle_ou", tracker)
        return [SlotSet('oracle_invoice_number', value)]

class ActionRecordOracleOU(Action):

    def name(self) -> Text:
        return "action_record_ou"

    def run(self, dispatcher, tracker, domain):
        print("In action_record_ou")
        oracle_invoice_number = tracker.get_slot('oracle_invoice_number')
        oracle_operating_unit_input = tracker.latest_message['text']
        user_choice = tracker.get_slot('user_choice')
        ## Call External service for oracle_response
        url = "http://www.mocky.io/v2/5e8f219f30000094e564c169"
        payload = {}
        headers = {}
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.text.encode('utf8')
            jsonData = json.loads(data)

            response = jsonData[user_choice][oracle_invoice_number][oracle_operating_unit_input]["response"]
            print("Response from Oracle Server : {}".format(response))
            dispatcher.utter_template("utter_oracle_details", tracker, oracle_invoice_number=oracle_invoice_number,
                                      oracle_operating_unit=oracle_operating_unit_input, oracle_response=response)
            return [SlotSet('oracle_operating_unit', oracle_operating_unit_input)]
        except:
            dispatcher.utter_template("utter_bad_oracle_details", tracker, oracle_invoice_number=oracle_invoice_number,
                                      oracle_operating_unit=oracle_operating_unit_input)
            return [SlotSet('oracle_operating_unit', oracle_operating_unit_input)]

