# Boris Johnson Quotes API
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Insipired by [Boris Johnson Bot](https://github.com/volcanicer/varsity/blob/master/Miscellaneous/borisbot.py)

[RESTful](https://restfulapi.net/) API returns a random Boris Johnson quote from `quotes.txt`.

## Running on your own machine
### Requirements:
* cmd (if on linux: terminal emulator & on mac: terminal)
* git (https://git-scm.com/downloads)
* python3 (https://python.org/downloads)

```
git clone https://github.com/MM-coder/boris-quotes-api.git
cd boris-quotes
python3 -m pip install -r requirements.txt
python3 main.py
```

## Documentation

The API is currently deployed to [https://bojo.maurom.dev/](https://bojo.maurom.dev/)

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
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://maurom.dev"><img src="https://avatars1.githubusercontent.com/u/22800592?v=4" width="100px;" alt=""/><br /><sub><b>Mauro M.</b></sub></a><br /><a href="https://github.com/MM-coder/boris-quotes-api/commits?author=MM-coder" title="Code">💻</a></td>
    <td align="center"><a href="https://heyjack.info"><img src="https://avatars0.githubusercontent.com/u/34974801?v=4" width="100px;" alt=""/><br /><sub><b>TheRealHeyJack</b></sub></a><br /><a href="#content-TheRealHeyJack" title="Content">🖋</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!