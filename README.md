# Quotes And Jokes Restful API

This RESTful API lets you fetch jokes and quotes for use in all sorts of applications.
It has a basic authentication system to prevent unauthorized access.
It is written in [Python](https://www.python.org/) and uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) as a web framework and [PostgreSQL](https://www.postgresql.org/) as a database. It is hosted on [Heroku](https://www.heroku.com/).

## API Endpoints

**API URL:**

You can test the API by sending a request to the following endpoint:

```
https://jokes-and-quotes-api.herokuapp.com/
```

## Basic Authentication

### Register

_Register for an account_

**_POST_** <code>/register</code>

Select form:

* **username**: The username of the user.
* **password**: The password of the user.

<details>
<summary>Example Response</summary>

<pre>
  Successfully Created User
</pre>

</details> <br>

### Login

_Login to your account_

**_POST_** <code>/login</code>

Select Basic Authentication:

<details>
<summary>Example Response</summary>

<pre>
  {
    "token": "random-token-will-be-generated-by-the-server"
}
</pre>

</details> <br>
> Now you can use the token in the Authorization header of all your requests. 

## Quotes

### ALL Quotes

_Retrieves a list of quotes_

**_GET_** <code>/quotes</code>

<details>
<summary>Example Response</summary>

<pre>
[
  {
    "author": "Albert Einstein",
    "quote": "A person who never made a mistake never tried anything new."
  },
  {
    "author": "Ancient Indian Proverb",
    "quote": "Certain things catch your eye, but pursue only those that capture the heart."
  },
  ...
]
</pre>

</details> <br>

### Random Quote

_Retrieve a random quote_

**_GET_** <code>/quotes/random</code>

<details>
<summary>Example Response</summary>

<pre>
{
  "author": "Dalai Lama",
  "quote": "Happiness is not something readymade.  It comes from your own actions."
}
</pre>

</details> <br>

### n random Quotes

_Retrieves a list of n random quotes where n is a whole number._

**_GET_** <code>/quotes/random/<n\></code>

<details>
<summary>Example Response(`10` as <n\>)</summary>

<pre>
[
  {
    "author": "Albert Einstein",
    "quote": "A person who never made a mistake never tried anything new."
  },
  {
    "author": "Benjamin Franklin",
    "quote": "Either write something worth reading or do something worth writing."
  },
  {
    "author": "Les Brown",
    "quote": "Too many of us are not living our dreams because we are living our fears."
  },
  {
    "author": "Aristotle",
    "quote": "There is only one way to avoid criticism: do nothing, say nothing, and be nothing."
  },
  {
    "author": "Chinese Proverb",
    "quote": "The person who says it cannot be done should not interrupt the person who is doing it."
  },
  {
    "author": "Latin Proverb",
    "quote": "If the wind will not serve, take to the oars."
  },
  {
    "author": "Booker T. Washington",
    "quote": "If you want to lift yourself up, lift up someone else."
  },
  {
    "author": "Wayne Gretzky",
    "quote": "You miss 100% of the shots you don’t take."
  },
  {
    "author": "Roger Staubach",
    "quote": "There are no traffic jams along the extra mile."
  },
  {
    "author": "Latin Proverb",
    "quote": "If the wind will not serve, take to the oars."
  }
]
</pre>

</details> <br>

### Random Quote by Author

_Retrieve a random quote by an Author's name_

**_GET_** <code>/quotes/author/<author-name\></code>

<details>
<summary>Example Response(`Albert` as <author\>)</summary>

<pre>
[
  {
    "author": "Albert Einstein",
    "quote": "A person who never made a mistake never tried anything new."
  },
  {
    "author": "Albert Einstein",
    "quote": "Strive not to be a success, but rather to be of value."
  }
]
</pre>

</details> <br>

## Jokes

### All Jokes

_Retrieves a list of jokes_

**_GET_** <code>/jokes</code>

<details>
<summary>Example Response</summary>

<pre>
[
  {
    "punchline": "Dam.",
    "setup": "What did the fish say when it hit the wall?",
    "type": "general"
  },
  {
    "punchline": "You put a little boogie on it.",
    "setup": "How do you make a tissue dance?",
    "type": "general"
  },
  ...
]
</pre>

</details> <br>

### Random Joke

_Retrieve a random jokes_

**_GET_** <code>/jokes/random</code>

<details>
<summary>Example Response</summary>

<pre>
[
  {
    "punchline": "They start coffin.",
    "setup": "How can you tell a vampire has a cold?",
    "type": "general"
  }
]
</pre>

</details> <br>

### n Random Jokes

_Retrieves a list of n random jokes where n is a whole number._

**_GET_** <code>/jokes/random/<n\></code>

<details>
<summary>Example Response(`10` as <n\>)</summary>

<pre>
[
  {
    "punchline": "A stick.",
    "setup": "What's brown and sticky?",
    "type": "general"
  },
  {
    "punchline": "They mostly wrap.",
    "setup": "Have you ever heard of a music group called Cellophane?",
    "type": "general"
  },
  {
    "punchline": "A little shaken.",
    "setup": "How was the snow globe feeling after the storm?",
    "type": "general"
  },
  {
    "punchline": "A fowl smell!",
    "setup": "What do you get when you cross a chicken with a skunk?",
    "type": "general"
  },
  {
    "punchline": "A handful of them.",
    "setup": "How many bones are in the human hand?",
    "type": "general"
  },
  {
    "punchline": "Because they cantaloupe!",
    "setup": "Why did the melons plan a big wedding?",
    "type": "general"
  },
  {
    "punchline": "When they run out of patients.",
    "setup": "When do doctors get angry?",
    "type": "general"
  },
  {
    "punchline": "   Billy Jeans!",
    "setup": "What did Michael Jackson name his denim store?",
    "type": "general"
  },
  {
    "punchline": "Guilty",
    "setup": "Do I enjoy making courthouse puns?",
    "type": "general"
  },
  {
    "punchline": "Because they're so good at it.",
    "setup": "Why do you never see elephants hiding in trees?",
    "type": "general"
  }
]
</pre>

</details> <br>

### All Jokes by Type

_Retrieves a list of all jokes by type_

> The following types are available:
>
> - `general`
> - `programming`
> - `knock-knock`

**_GET_** <code>/jokes/<type\></code>

<details>
<summary>Example Response(`programming` as type )</summary>

<pre>
[
  {
    "punchline": "Even if you're wrong, you're only off by a bit.",
    "setup": "What's the best thing about a Boolean?",
    "type": "programming"
  },
  {
    "punchline": "Inheritance",
    "setup": "What's the object-oriented way to become wealthy?",
    "type": "programming"
  },
  {
    "punchline": "The Foo Bar.",
    "setup": "Where do programmers like to hangout?",
    "type": "programming"
  },
  {
    "punchline": "Because he didn't get arrays.",
    "setup": "Why did the programmer quit his job?",
    "type": "programming"
  },
  {
    "punchline": "Because Oct 31 == Dec 25",
    "setup": "Why do programmers always mix up Halloween and Christmas?",
    "type": "programming"
  },
  {
    "punchline": "'Can I join you?'",
    "setup": "A SQL query walks into a bar, walks up to two tables and asks...",
    "type": "programming"
  },
  {
    "punchline": "None that's a hardware problem",
    "setup": "How many programmers does it take to change a lightbulb?",
    "type": "programming"
  },
  {
    "punchline": "the rest of them will write Perl",
    "setup": "If you put a million monkeys at a million keyboards, one of them will eventually write a Java program",
    "type": "programming"
  },
  {
    "punchline": "(hip hip array)",
    "setup": "['hip', 'hip']",
    "type": "programming"
  },
  {
    "punchline": "You must first understand what recursion is",
    "setup": "To understand what recursion is...",
    "type": "programming"
  },
  {
    "punchline": "Those who understand binary and those who don't",
    "setup": "There are 10 types of people in this world...",
    "type": "programming"
  },
  {
    "punchline": "Can't catch me - Avicii",
    "setup": "Which song would an exception sing?",
    "type": "programming"
  },
  {
    "punchline": "Because they don't C#",
    "setup": "Why do Java programmers wear glasses?",
    "type": "programming"
  },
  {
    "punchline": "Try it out on Internet Explorer",
    "setup": "How do you check if a webpage is HTML5?",
    "type": "programming"
  },
  {
    "punchline": "If you have to explain it then it is not that good.",
    "setup": "A user interface is like a joke.",
    "type": "programming"
  },
  {
    "punchline": "...but you might not get it.",
    "setup": "I was gonna tell you a joke about UDP...",
    "type": "programming"
  },
  {
    "punchline": "Do you know the problem with UDP jokes?",
    "setup": "The punchline often arrives before the set-up.",
    "type": "programming"
  },
  {
    "punchline": "Because they use a strongly typed language.",
    "setup": "Why do C# and Java developers keep breaking their keyboards?",
    "type": "programming"
  },
  {
    "punchline": "A race condition. Who is there?",
    "setup": "Knock-knock.",
    "type": "programming"
  },
  {
    "punchline": "I get to keep telling them until you get them.",
    "setup": "What's the best part about TCP jokes?",
    "type": "programming"
  },
  {
    "punchline": "A full one, in case he gets thirsty, and an empty one, in case he doesn’t.",
    "setup": "A programmer puts two glasses on his bedside table before going to sleep.",
    "type": "programming"
  },
  {
    "punchline": "Those who understand binary, those who don't, and those who weren't expecting a base 3 joke.",
    "setup": "There are 10 kinds of people in this world.",
    "type": "programming"
  },
  {
    "punchline": "It hurts when IP.",
    "setup": "What did the router say to the doctor?",
    "type": "programming"
  },
  {
    "punchline": "He goes nowhere.",
    "setup": "An IPv6 packet is walking out of the house.",
    "type": "programming"
  },
  {
    "punchline": "Bartender says, \"here, but I’ll need that back in an hour!\"",
    "setup": "A DHCP packet walks into a bar and asks for a beer.",
    "type": "programming"
  },
  {
    "punchline": "They couldn't find a table.",
    "setup": "3 SQL statements walk into a NoSQL bar. Soon, they walk out",
    "type": "programming"
  }
]
</pre>

</details> <br>

### Random Joke by Type

_Retrieve a random joke by a type_

> The following types are available:
>
> - `general`
> - `programming`
> - `knock-knock`

**_GET_** <code>/jokes/<type\>/random</code>

<details>
<summary>Example Response(`programming` as type)</summary>

<pre>
{
  "punchline": "Those who understand binary and those who don't",
  "setup": "There are 10 types of people in this world...",
  "type": "programming"
}
</pre>

</details> <br>

### n random Jokes by Type

_Retrieves n random jokes by a type, where n is a whole number_

> The following types are available:
>
> - `general`
> - `programming`
> - `knock-knock`

**_GET_** <code>/jokes/<type\>/random/<n\></code>

<details>
<summary>Example Response(`10` as <n\> )</summary>

<pre>
[
  {
    "punchline": "(hip hip array)",
    "setup": "['hip', 'hip']",
    "type": "programming"
  },
  {
    "punchline": "The Foo Bar.",
    "setup": "Where do programmers like to hangout?",
    "type": "programming"
  },
  {
    "punchline": "You must first understand what recursion is",
    "setup": "To understand what recursion is...",
    "type": "programming"
  },
  {
    "punchline": "Because they don't C#",
    "setup": "Why do Java programmers wear glasses?",
    "type": "programming"
  },
  {
    "punchline": "None that's a hardware problem",
    "setup": "How many programmers does it take to change a lightbulb?",
    "type": "programming"
  },
  {
    "punchline": "Inheritance",
    "setup": "What's the object-oriented way to become wealthy?",
    "type": "programming"
  },
  {
    "punchline": "The Foo Bar.",
    "setup": "Where do programmers like to hangout?",
    "type": "programming"
  },
  {
    "punchline": "Bartender says, \"here, but I’ll need that back in an hour!\"",
    "setup": "A DHCP packet walks into a bar and asks for a beer.",
    "type": "programming"
  },
  {
    "punchline": "Bartender says, \"here, but I’ll need that back in an hour!\"",
    "setup": "A DHCP packet walks into a bar and asks for a beer.",
    "type": "programming"
  },
  {
    "punchline": "Even if you're wrong, you're only off by a bit.",
    "setup": "What's the best thing about a Boolean?",
    "type": "programming"
  }
]
</pre>

</details> <br>

## Contribute to the API

- Fork the repository on [GitHub](https://github.com/Drish-xD/rest-api)
- Add your own joke or quote to the database. `./API/Data/jokes.json` or `./API/Data/quotes.json`
- Make a pull request.

> Also, feel free to report any issues or suggestions.

## References

- Jokes have been taken from [15Dkatz's jokes.json](https://github.com/15Dkatz/official_joke_api/blob/master/jokes/index.json).

- Quotes have been taken from [nasrulhazim's gist](https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80).
