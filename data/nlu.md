## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- Yes

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:check_For_Oracle
- ORACLE
- oracle
- Oracle
- ora

## intent:check_For_Sap
- SAP
- sap
- Sap

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Hi

## intent:invalid_invoice_number
- xxxxx111
- yyyyy222
- yzzzz222
- yxxxx222
- yxxxy222

## intent:invalid_ou_name
- ouxxxxx111
- ouyyyyy222
- ouyzzzz222
- ouyxxxx222
- ouyxxxy222

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good
- Good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:user_valid_user_choice
- generate new complaint
- new complaint
- gen complaint
- facing issue
- status check
- check status
- (/user_valid_user_choice{"user_choice":"oracle"})
- (/user_valid_user_choice{"user_choice":"sap"})

## intent:valid_invoice_number
- [per1000567623] (invoice_number)
- acc [per1000000012](invoice_number)
- account [per1012262346](invoice_number)
- account: [per1000162987](invoice_number)
- id [per1000567346](invoice_number)
- id: [per1056762346](invoice_number)
- my account id is [per1056762346](invoice_number)
- per1000567623

## intent:valid_ou_name
- [CRB0000012] (ou_name)
- comp: [CRB0000003](ou_name)
- comp number: [CRA0000004](ou_name)
- my complaint number is [CRA0000002](ou_name)
- CRB0000012

## regex: invoice_number
- per\d{10}

## regex: ou_name
- CR[A-C]{1}\d{7}
