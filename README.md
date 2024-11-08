# Joke API (Example)

This is an example for the (not yet official) RaspAPI YSWS program.

## Routes

- `GET /` - Returns this HTML page containing a random joke and the API documentation.
- `POST /` - Returns a random joke in JSON format.
- `POST /puns` - Returns a list of random jokes in JSON format. If number is not given, returns all jokes.
- `POST /joke-of-the-day` - Returns a random joke in JSON format. If date is given, it fetches the joke of the day for that date. If date is not given, it fetches the joke of the day for today.
- `POST /generate-joke` - Returns a random joke in JSON format. If prompt is given, it generates a joke relating to the prompt. If prompt is not given, it generates a random programming related joke. Uses the Llama3.2-3b model from Meta and is hosted on LeptonAI.
- `POST /search-jokes` - Returns a list of jokes in JSON format that contain the query. If limit is given, it returns at most limit jokes. If limit is not given, it returns at most 10 jokes.
- `POST /get-jokes-by-tag` - Returns a list of jokes in JSON format that contain the tag.
