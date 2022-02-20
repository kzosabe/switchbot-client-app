# switchbot-client-app(pre-alpha)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/switchbot-client-app.svg)](https://pypi.org/project/switchbot-client-app/)
[![PyPI - Library Version](https://img.shields.io/pypi/v/switchbot-client-app.svg)](https://pypi.org/project/switchbot-client-app/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/switchbot-client-app)](https://pypi.org/project/switchbot-client-app)
[![License](https://img.shields.io/badge/license-MIT%2FApache--2.0-informational?style=flat-square)](README.md#License)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An unofficial switchbot client app on Windows and macOS.

This app is **pre-alpha** version and only the minimum functionality has been implemented.  
There are a lot of room for improvement. Any contributions are welcome!

## Table of Contents

- [Authentication](#authentication)
- [License](#license)


## Authentication

Before you start using this client, you need to get an open token.
Please follow the instructions in the official documentation below.

https://github.com/OpenWonderLabs/SwitchBotAPI#authentication

Once you have the token, use one of the following methods to pass the information to the client.

If `config.yml` exists in the same directory which app executable is located 
or `~/.config/switchbot-client/config.yml` exists,  
this app will get the `token` entry from the file and use the value.

### Place the app and the config file in the same folder

For example, if you are using windows, you can use token 
if you put file like below into the same directory which switchbot-client-app.exe exists.
```config.yml
token: your_switchbot_open_token
```

### Place the config file in the specific path

If you are using macOS, you can do like below. 
```shell
mkdir -p ~/.config/switchbot-client
echo "token: your_switchbot_open_token" >>  ~/.config/switchbot-client/config.yml
```


## License

Licensed under either of

- Apache License, Version 2.0
   ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
- MIT license
   ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
