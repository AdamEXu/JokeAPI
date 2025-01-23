# Joke API

It's an API that generates jokes! The in-built ones are programming jokes, but using the `/generate-joke` route, you can generate any joke you would like using AI!

Add a little sprinkle of humor into any project easily! This is perfect for inserting a little pun on your homepage, showing users a personalized joke while they wait for something to load, or showing our joke of the day in your footer!

## Routes

Note: better documentation is available on the website.

- `GET /` - Returns this HTML page containing a random joke and the API documentation.
- `POST /` - Returns a random joke in JSON format.
- `POST /puns` - Returns a list of random jokes in JSON format. If number is not given, returns all jokes.
- `POST /joke-of-the-day` - Returns a random joke in JSON format. If date is given, it fetches the joke of the day for that date. If date is not given, it fetches the joke of the day for today.
- `POST /generate-joke` - Returns a random joke in JSON format. If prompt is given, it generates a joke relating to the prompt. If prompt is not given, it generates a random programming related joke. Uses the Llama3.2-3b model from Meta and is hosted on LeptonAI.
- `POST /search-jokes` - Returns a list of jokes in JSON format that contain the query. If limit is given, it returns at most limit jokes. If limit is not given, it returns at most 10 jokes.
- `POST /get-jokes-by-tag` - Returns a list of jokes in JSON format that contain the tag.

## Usage

**I highly recommend using the pre-hosted API rather than self-hosting.**

Clone the repo and install dependencies:

```
git clone https://github.com/AdamEXu/JokeAPI.git
cd JokeAPI
python3 -m pip install -r requirements.txt
```

If you would like to use the generate joke feature, you'll have to grab a **free** API key from [lepton.ai](https://lepton.ai/). Then set the environment variable:

```
export LEPTON_API_TOKEN="YOUR_LEPTON_API_KEY_WHATEVER_BLAH_BLAH_BLAH_YAY"
```

If you are running this on your local machine where port 80 will most likely be protected, set the debug flag.

```
export DEBUG=TRUE
```

Now, you can run the server:

```
python app.py
```

Now, go to [localhost](http://localhost/), or [localhost:8080](http://localhost:8080/) if you have the debug flag on. There will be instructions on how to use the API there.

## Or... Use my hosted API!

I hosted the API on two places:

**Vercel:** [raspapi-jokeapi.vercel.app](https://raspapi-jokeapi.vercel.app/)

**Nest:** [raspapi-example.adamthegreat.hackclub.app](https://raspapi-example.adamthegreat.hackclub.app/)

Note that both of these may stop working at any time. The Vercel hosted one will likely be more reliable (nest outages \*cough\*)

Use the API as much as you want in your projects to add a dash of humor!
