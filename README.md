# SUBLIME AUTO COMMIT

A script to auto popup a form for input commit message on sublime text when save a file.

> **Note:** The plugin only work on file inside the folder with `.git` folder in it. If not, an error popup will appear

## Requirements before installing

- `python3` installed on the machine
- `groq` module installed
  > `pip install groq`
- Groq AI API Key
  You can generate the API KEY here: ![https://console.groq.com/keys](https://console.groq.com/keys)

## Installing the pluggin
 - Clone this repo
 - Edit file `GROQ_API_KEY.txt` then put your Groq api key and save
 - Open Sublime Text
 - Goto `Preferences > Browse Packages`
 - Once Packages folder opened, copy `sublime_git_auto_commit.py`, `SGAC_AI.py`, and `GROQ_API_KEY.txt` files into `User` folder
 - Then set the Key Bindings on `Preferences > Key Bindings`
 - On right tab, paste these config:
   ```json
    [
        {
            "keys": ["ctrl+s"], "command": "sublime_git_auto_commit"
        }
    ]
   ```
 - Save then restart the Sublime

## How to use the plugin

Just press `CTRL + S` if you want to show the prompt of input the commit message. Ignore it if you wont commit any message. Press `SHIFT + Enter` or `CTRL + Enter` for new line, and `ENTER` if you want to save the commit message

## The screenshot

![image](https://github.com/user-attachments/assets/3e1664a9-75b0-43f6-845a-26c438215022)