# netce.com
## Instructions:
```
$ git clone https://github.com/colinpotter/netce.com.git
$ cd netce.com
$ python3 manage.py migrate
$ python3 manage.py test
```
*If you would like to set up the server to run, check the admin pages, and
import a few sample questions and choices you can do the following:*
```
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
$ mv polls/migrations/disabled/0002_load_historical_data.py polls/migrations/
$ python3 manage.py migrate
$ mv polls/migrations/0002_load_historical_data.py polls/migrations/disabled
```
*We move the load_historical_data file back and forth, so that it won't put the
sample questions in the database when running the test functions. which would
break some of the tests that assume an empty database*


## Features added:
- mark poll questions as expired when they are a year old or older
    - they will not show up in the index view
    - they are marked as expired in the admin panel
- added a future column in the questions admin panel

## Tests added:
- expired questions don't show up in the index
- proper message is shown when there are no choices for a question
- message when a choice has negative votes
    - TEST FAILS: because I modified the message to not match what is expected
