## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_user_valid_help
* user_valid_user_choice{"user_choice": "oracle"}
    - slot{"user_choice": "oracle"}
    - utter_oracle_invoice_number
* valid_invoice_number
    - action_record_invoice
    - slot{"oracle_invoice_number": "per1000567623"}
* valid_ou_name
    - action_record_ou
    - slot{"oracle_operating_unit": "CRB0000012"}
* affirm
    - utter_goodbye
