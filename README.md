## Installation

Note - you need python installed before starting installation.

Start by cloning this repo to your computer.

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
pip install -r requirements.txt
```

Change directory to flask_app and run the flask server

```
cd flask_app
flask run
```

Now we need to run the vue app.
In a new terminal window

```
cd frontend
npm run dev
```

## Notes

To backup the database run this command in the db directory

```commandline
sqlite3 tracker.db ".backup tracker.db.bak"
```
