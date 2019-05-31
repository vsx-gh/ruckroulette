# ruckroulette
Flask app to build a GORUCK PT workout. Take the guesswork/cowardice out of your training!

### Setup
Clone this directory where you want to run it. Ideally, you would use a Python virtualenv.
Here's one example of how to do it with Python 3:
```
python3 -m venv <environment_name>
source <environment_name>/bin/activate
pip install Flask
```

Once you have an environment created and sourced, point to the correct app:
`export FLASK_APP=app.py`

Run the app: `flask run`

Hit up a browser and head to `localhost:5000`

Enjoy! Get after it with some [good livin'](http://news.goruck.com/rucking-training/goruck-good-livin-video/).

### Deployment
This app is intended to run on a hosted platform...somewhere. I hope to put it up
on AWS to be served by API Gateway+Lambda, but that will take some time. I'll add
the code to automate that deployment once it exists.

### About the Exercises
DISCLAIMER: I am not affiliated with GORUCK in any manner. I am a customer and a
happy participant in their exercise programs. If you'd like to learn more, please
check them out [here](https://goruck.com).
