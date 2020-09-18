# Goals

Python flask webapp to have real time task-list synced with text file.
Useful for stuff like OBS, where you can show your "current task".

## Installation and Setup

Installation and setup is like any other flask project. Either run the python `wsgi.py` file or host the webapp 24/7 with gunicorn and nginx. The former is recommended, even though it is "not meant for production", because *I'm sure you won't need this on 24/7*. Also, host on your machine to get easy access to the `current_goal.txt` file.

### Step-by-step

#### Requirements
- Python3.6 or higher. Get it [here](https://python.org).
- Optional: `git` installed to clone the repo and auto-fetch to update it. (You can also download the repo).

Now, clone the repository or download it:
```shell script
git clone https://github.com/arnu515/goals.git goals
cd goals
```

Install all requirements with:
```shell script
# Use a virtualenv if you want
pip3 install -r requirements.txt
```

Start the server with:
```shell script
py wsgi.py
```

And the webapp should be on your computer's IP address on port 5000! [Check it out!](http://localhost:5000)

---

## Usage

Usage is pretty simple. Use the webgui to add goals with the input box or delete them with the checkmark. To access the text file containing the **top-most** goal, it is located in `src/data` folder of the goals folder you just downloaded. There is also a json file containing all goals.

---

## Credits

- Check out `requirements.txt` for all python3 packages used.