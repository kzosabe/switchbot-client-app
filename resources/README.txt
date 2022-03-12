switchbot-client-app v0.0.5
=====================

An unofficial switchbot client app on Windows PC and macOS.

This app is **pre-alpha** version and only the minimum functionality has been implemented.
There are a lot of room for improvement. Any contributions are welcome!

https://github.com/kzosabe/switchbot-client-app


Authentication
--------------------

Before you start using this client, you need to get an open token.
Please follow the instructions in the official documentation below.

https://github.com/OpenWonderLabs/SwitchBotAPI#authentication

Once you have the token, use one of the following methods to pass the information to the client.

If `config.yml` exists in the same directory which app executable is located
or `~/.config/switchbot-client/config.yml` exists,
this app will get the `token` entry from the file and use the value.

For example, if you are using windows, you can use token
if you put file like below into the same directory which switchbot-client-app.exe exists.

config.yml
```
token: your_switchbot_open_token
```
