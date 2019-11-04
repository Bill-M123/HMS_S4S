
# Participant Web App

This repository contains all the code for a simple Django based app for adding potential patients to a database.  There are four screens that the user has access to within the app:  Login, Landing Page, List Existing Participants, Add new Participant, and Logout.


The app builds a small sqlite database having the following fields:

- Participant Name (text, max len=20)
- Participant Age (text, max len=20)
- Does Participant have any siblings? (text, max len=20, currently limited to Y/N)
- Known environmental exposures (text, max len=20, limited to Pb,SS (2nd hand smoke), and NA)
- Known genetic mutations (text, max len=20, limited to MM (Missense),NS (Nonsense), and NA)

The choices for exposure and mutation type are limited for demonstration purposes, but easily extensible.  The siblings field was implemented as a text field so that future implementations could contain more information than a simple Y/N on sibling existence.

## Installation and Requirements

Start by cloning this directory:  https://github.com/Bill-M123/HMS_S4S/tree/master/hms

- Open a command line. Navigate to ~\hms_coding\hms.  In this directory, you should see a file named: manage.py

- Create a conda environment (see note below if you need help):  __conda create --name__ _myenv_ __--file__ _requirements.txt_ where _myenv_ is the name of your conda environment, and _requirements.txt_ is as described below.

- Activate conda environment: __conda activate__ _myenv_

- Start the django development server:  __python manage.py runserver__

- Open a fresh browser, type http://127.0.0.1:8000/web_ap/

- Login (credentials available elsewhere)

After testing app, you can free up some space on your computer by removing the env that you no longer need with the following commands (on the command line):

- __conda deactivate__
- __conda env remove -n__ _myenv_

__Note__

App was built in an python 3.7 environment from Anaconda.  Anaconda is available here:  https://www.anaconda.com/distribution/

The actual conda env requirements can be found in: requirements.txt (this directory).  

This environment is very heavy and would also be suitable for basic data science (including Question 1 of this test).  It takes a fair bit of time to load, but any recent version of Python(3.7) with django (2.2.1 or later), re, os, and path should work (though is untested at this point due to time constraints.)  

If you are already using Anaconda, try the following from inside your most upto date python env:

__conda install -c anaconda django__

as everything else you need should be resident in the initial distribution.

If you are not using the anaconda python distribution, enter your most up to date virtualenv and run:

__pip install Django--2.2.7__

In either case, after completion, run __python manage.py runserver__.  You may be able to avoid a long anaconda build.  If not, install the full env as above.


__Style Notes:__  App roughly styled based on:  http://syncfor.science/


```python

```
