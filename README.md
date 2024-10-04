# SUBLIME AUTO COMMIT

A script to auto popup a form for input commit message on sublime text when save a file.

# Install
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
