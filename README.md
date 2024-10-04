# SUBLIME AUTO COMMIT

A script to auto popup a form for input commit message on sublime text when save a file.

## Install
 - Clone this repo
 - Open Sublime Text
 - Goto `Preferences > Browse Packages`
 - Once Packages folder opened, copy `sublime_git_auto_commit.py` into `User` folder
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

## Usage

Just press `CTRL + S` if you want to show the prompt of input the commit message. Ignore it if you wont commit any message. Press `SHIFT + Enter` or `CTRL + Enter` for new line, and `ENTER` if you want to save the commit message
