# Joke API

It's an API that generates jokes! The in-built ones are programming jokes, but using the `/generate-joke` route, you can generate any joke you would like using AI!

Add a little sprinkle of humor into any project easily! This is perfect for inserting a little pun on your homepage, showing users a personalized joke while they wait for something to load, or showing our joke of the day in your footer! The AI joke generation is really fast (powered by Groq's inference), allowing this to generate jokes in less than a second (usually fractions of a second)

I have hosted it on my website: [jokeapi.adamxu.net](https://jokeapi.adamxu.net/)

**All features are 100% free to use, including the AI joke generation feature!**

## Routes

Note: better documentation is available [here](https://jokeapi.adamxu.net/).

- `GET /` - Returns a random joke in JSON format. If your user agent seems to be a browser, it will return the HTML page.
- `GET /puns` - Returns a list of random jokes in JSON format. If number is not given, returns all jokes.
- `GET /joke-of-the-day` - Returns a random joke in JSON format. If date is given, it fetches the joke of the day for that date. If date is not given, it fetches the joke of the day for today.
- `GET or POST /generate-joke` - Returns a random joke in JSON format. If prompt is given, it generates a joke relating to the prompt. If prompt is not given, it generates a random programming related joke. Uses the Llama3.2-3b model from Meta and is hosted on LeptonAI.
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

If you would like to use the generate joke feature, you'll have to grab a **free** API key from [groq.com](https://groq.com/). Then set the environment variable:

```
export GROQ_API_KEY="YOUR_GROQ_API_KEY_WHATEVER_BLAH_BLAH_BLAH_YAY"
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

**Vercel:** [jokeapi.adamxu.net](https://jokeapi.adamxu.net/)

**Nest:** [raspapi-example.adamthegreat.hackclub.app](https://raspapi-example.adamthegreat.hackclub.app/) - Note: this version is outdated for now...

Note that both of these may stop working at any time. The Vercel hosted one will likely be more reliable (nest outages \*cough\*) and also auto updates to the latest version.

Use the API as much as you want in your projects to add a dash of humor!
