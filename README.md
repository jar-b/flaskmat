# flaskmat

Flask + Materialize = flaskmat. A web application that does nothing, because learning.

## Setup

Create and activate a virtualenv (preferably python3).

```sh
virtualenv venv
source venv/bin/activate
```

Navigate to the `flaskmat` directory, then install required packages and create dummy users.

```sh
# install packages
pip install -r requirements.txt

# create users
python user_mgmt.py -c
```

Finally, start the server.

```sh
python runserver.py              # production, port 8080 (default)
python runserver.py -d -p 8081   # debug, port 8081
```

## To-do

* User authentication, login page
* Make the app do something
