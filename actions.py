# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
#
#
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

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

class ActionRecordOracleInvoice(Action):

    def name(self) -> Text:
        return "action_record_invoice"

    @staticmethod
    def required_slots(tracker):
        return [
            "oracle_invoice_number",
            "oracle_operating_unit"
        ]

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_template("utter_oracle_ou", tracker)

        value = tracker.latest_message['text']
        return [SlotSet('oracle_invoice_number', value)]

class ActionRecordOracleOU(Action):

    def name(self) -> Text:
        return "action_record_ou"

    @staticmethod
    def required_slots(tracker):
        return [
            "oracle_invoice_number",
            "oracle_operating_unit"
        ]

    def run(self, dispatcher, tracker, domain):

        oracle_invoice_number = tracker.get_slot('oracle_invoice_number')
        oracle_operating_unit_input = tracker.latest_message['text']
        dispatcher.utter_template("utter_oracle_details", tracker, oracle_invoice_number=oracle_invoice_number,
                                  oracle_operating_unit=oracle_operating_unit_input)
        return [SlotSet('oracle_operating_unit', oracle_operating_unit_input)]

