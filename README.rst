Search by age app
=================

This app's purpose is to search through a collection of artists.

I coded this up as part of a job interview process.

Minimum requirements are:
-------------------------

- find artists that match an age range (minimum to maximum) where results are ordered by best fit.
- the best fit algorithm is should favour artists with ages in the middle of the search range over those at either extreme of the range.
- output should be a JSON encoded structure with a list of matching artist UUIDs and ages.


Setup Instructions
------------------

Mostly vanilla., but added here for completeness sake::

    git clone https://github.com/lvisintini/exercise-search-by-age.git
    cd ./exercise-sign-data-app
    mkvirtualenv exercise-search-by-age
    pip install -r requirements.txt
    python app.py

After that, put `http://127.0.0.1:8000/artist-search/` into your browser thingy and you should be able to test it out yourself.

Tests
-----

There are a few. Run them with ``py.test tests.py``
