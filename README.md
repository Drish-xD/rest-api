# Quotes And Jokes Restful API

This RESTful API lets you fetch jokes and quotes for use in all sorts of applications.
It is written in [Python](https://www.python.org/), and uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) as a web framework.

# Usage

## Quotes

- **Get JSON of all Quotes**

  ```
  https://jokes-and-quotes-api.herokuapp.com/quotes
  ```

- **Get JSON of a random Quote**

  ```
  https://jokes-and-quotes-api.herokuapp.com/quotes/random
  ```

- **Get JSON of n random Quotes**

  ```
  https://jokes-and-quotes-api.herokuapp.com/quotes/random/<n>
  ```

  eg: `https://jokes-and-quotes-api.herokuapp.com/quotes/random/10`
  This will return 10 random quotes.

- **Get JSON of a random Quote by Author**

  ```
  https://jokes-and-quotes-api.herokuapp.com/quotes/author/<author>
  ```

  eg: `https://jokes-and-quotes-api.herokuapp.com/quotes/author/Albert` This will return all quotes from the author name starting with 'Albert'.

## Jokes

- **Get JSON of all Jokes**

  ```
  https://jokes-and-quotes-api.herokuapp.com/jokes
  ```

- **Get JSON of a random Joke**

  ```
  https://jokes-and-quotes-api.herokuapp.com/jokes/random
  ```

- **Get JSON of n random Jokes**

  ```
  https://jokes-and-quotes-api.herokuapp.com/jokes/random/<n>
  ```

  eg: `https://jokes-and-quotes-api.herokuapp.com/jokes/random/10`
  This will return 10 random jokes.

- **Get JSON of all Jokes by Type**

  ```
  https://jokes-and-quotes-api.herokuapp.com/jokes/<type>
  ```

  eg: `https://jokes-and-quotes-api.herokuapp.com/jokes/programming` This will return all jokes with the Type 'programming'.

  The following types are available:

  - `general`
  - `programming`
  - `knock-knock`

* **Get JSON of a random Joke by Type**

  ```
  https://jokes-and-quotes-api.herokuapp.com/jokes/<type>/random
  ```

  eg: `https://jokes-and-quotes-api.herokuapp.com/jokes/programming/random` This will return a random joke with the Type 'programming'.

* **Get JSON of n random Jokes by Type**

  ```
  https://jokes-and-quotes-api.herokuapp.com/jokes/<type>/random/<n>
  ```

  eg: `https://jokes-and-quotes-api.herokuapp.com/jokes/programming/random/10`
  This will return 10 random jokes with the Type 'programming'.

## Contribute to the API

- Fork the repository on [GitHub](https://github.com/Drish-xD/rest-api)
- Add your own joke or quote to the database. `./Data/jokes.json` or `./Data/quotes.json`
- Make a pull request.

## References

- Jokes have been taken from [15Dkatz's jokes.json](https://github.com/15Dkatz/official_joke_api/blob/master/jokes/index.json).

- Quotes have been taken from [nasrulhazim's gist](https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80).
