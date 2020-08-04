# Boris Johnson Quotes API

Insipired by [Boris Johnson Bot](https://github.com/volcanicer/varsity/blob/master/Miscellaneous/borisbot.py)

[RESTful](https://restfulapi.net/) API returns a random Boris Johnson quote from `quotes.txt`.

## Running on your own machine
### Requirements:
* cmd (if on linux: terminal emulator & on mac: terminal)
* git (https://git-scm.com/downloads)

```
git clone https://github.com/MM-coder/boris-quotes-api.git
cd boris-quotes
python3 -m pip install -r requirements.txt
python3 main.py
```

## Documentation

* `/` - Base URL - Returns a quote, in JSON format 
    - Will return a dictionary with a key `quote` who's corresponding value will be the quote.
        ```
        {
        "quote": "Hilary Clinton has got dyed blonde hair and pouty lips, and a steely blue stare, like a sadistic nurse in a mental hospital."
        }
        ```

## Contributing

If you wish to add quotes, just open a PR (pull request) where you edit `quotes.txt`, please keep in mind each quote should be on its own line

## License

This project is licensed under the MIT license