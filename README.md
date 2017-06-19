# netce.com
## Instructions:
```
$ git clone https://github.com/colinpotter/netce.com.git
$ cd netce.com
$ python3 manage.py migrate
$ python3 manage.py test
```
*If you would like to set up the server to run, check the admin pages, and
import a few sample questions and choices, you can do the following:*
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
- added a link to the admin page and the polls page in the main index

## Tests added:
- test_views.py:QuestionIndexViewTests:test_expired_question()
    - expired questions don't show up in the index
- test_views.py:QuestionDetailViewTests:test_expired_question()
    - expired questions return 404 html response code
- test_views.py:QuestionDetailViewTests:test_for_buttons()
    - a radio button is shown when there is a choice in a detail view
- test_views.py:QuestionDetailViewTests:test_no_choice_question()
    - info message is shown when there are no choices for a question
- test_views.py:test_negative_votes()
    - the proper message is shown when a choice has negative votes
    - TEST FAILS: because I modified the message to not match what is expected
- test_views.py:test_error()
    - a test that has a NameError from an undefined name
    - TEST ERRORS: I used an udefined variable on purpose

- test_models.py:test_was_published_recently_with_expired_question()
    - expired questions are not published recently

- test_forms.py:test_form_response_code()
    - tests that a form post returns a valid 200 code
    - this test saves a question to the database then deletes it
