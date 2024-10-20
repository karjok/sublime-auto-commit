# SUBLIME TEXT AUTO COMMIT

Simple Extension for Sublime Text to Automatically Generate and Commit Changes

This script automatically triggers a pop-up form for entering a commit message whenever you save a file in Sublime Text. The commit message input prompt displays an AI-generated message by default, summarizing the changes made to the file. You can easily edit this default message to better reflect your intended commit, streamlining your version control process directly from the text editor.

> **Note:** The plugin only work on file inside the folder with `.git` folder in it. If not, an error popup will appear

## Requirements before installing

- `python3` installed on the machine
- `groq` module installed
  > `pip install groq`
- Groq AI API Key
You can generate the API KEY here: [https://console.groq.com/keys](https://console.groq.com/keys)

## Installing the pluggin
 - Clone this repository.
 - Create and Edit `GROQ_API_KEY.txt` file to include your Groq API key, then save the changes.
 - Open Sublime Text
 - Navigate to `Preferences > Browse Packages`
 - Once the Packages folder is open, copy the following files into the `User` folder:
   - `sublime_git_auto_commit.py`
   - `SGAC_AI.py`
   - `GROQ_API_KEY.txt`
 - Set the key bindings by going to `Preferences > Key Bindings`.
 - On right tab, paste following configuration:
   ```json
    [
        {
            "keys": ["ctrl+s"], "command": "sublime_git_auto_commit"
        }
    ]
   ```
 - Save the changes and restart the Sublime Text

## How to use the plugin
- Press `CTRL + S` to save the changed file and trigger the commit message input prompt.
- When the prompt appears, the generated AI commit message will be automatically loaded into the input prompt.
- If the default message is sufficient, press `Enter` to commit the change with the AI-generated commit message.
- If you do not need to commit any changes, simply leave the prompt or press `ESC` to close it.


## The screenshot

![Screenshot-from-2024-10-19-04-59-40.png](https://qu.ax/PXgUt.png)

## The demo video

[![SGAC-Preview-Video](https://qu.ax/kkQj.png)](https://qu.ax/nWKQK.webm)