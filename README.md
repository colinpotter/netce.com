# netce.com
## Instructions:
```
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
python3 manage.py test
```
*If you would like to import a few questions and choices into the database,
you can do the following:*
```
mv polls/migrations/0002_load_historical_data.py polls/migrations/disabled
python3 manage.py migrate
```

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
