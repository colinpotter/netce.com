# netce.com
## Instructions:
```
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
mv polls/migrations/0002_load_historical_data.py polls/migrations/disabled
python3 manage.py test
```
*we have to disable the 0002_load_historical_data.py file that is used to populate the database.*
*Otherwise, it is migrated at the beginning of the test procedures and breaks them*

## Features added:
- mark poll questions as expired when they are a year old or older
    - they will not show up in the index view
    - they are marked as expired in the admin panel
- added a future column in the questions admin panel

## Tests added:
- expired questions don't show up in the index
- proper message is shown when there are no choices for a question
- message when a choice has negative votes
    - this test fails because I modified the message to not match expected
