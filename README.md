## Installation

Note - you need python installed before starting installation.

In the terminal, navigate to the rebel badge tracker directory.

```
cd ~/Documents/RebelBadgeTracker
```

Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Install requirments

```
pip install -r requirements.txtß
```

Change directory to flask_app and run the flask server

```
cd flask_app
flask run
```

## Notes

To backup the database run this command in the db directory

```commandline
sqlite3 tracker.db ".backup tracker.db.bak"
```
