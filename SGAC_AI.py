import re
import sys
import os
import subprocess
from groq import Groq

PROMPT = """
Summarize the given diff and Generate infomative commit message for following git diff with maximum 50 characters for TITLE and maximum 70 characters for DESCRIPTION:

```
%s
```

Please add Preffix by category:
- [ADD]: For new features, functions, or files.
- [FIX]: For bug fixes or corrections.
- [UPDATE]: For updates or modifications to existing code.
- [REMOVE]: For deletions of code or functionality.
- [DEBUG]: For general tasks, maintenance, or minor changes.

THE FINAL MESSAGE FORMAT:

```
[$PREFFIX] - $TITLE

$DESCRIPTION
```

DO NOT ANSWER WITH OTHER WORDS, JUST ANSWER WITH THE FINAL MESSAGE FORMAT ONLY
"""


def generate_commit_message_for(API_KEY,diff):
    prompt = PROMPT % diff
    client = Groq(
        api_key= API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    response = chat_completion.choices[0].message.content
    try:
        response = re.search(r"(\[[(['$A-Z]{3,10}\] ?\-? ?.*)\W{0,3}(?:description\:)?(.*)", response, re.IGNORECASE)
        title = response.group(1)
        description = response.group(2)
        return title.replace("$",""), description.strip()
    except:
        return "[ERROR] Error when gerating commit message", response
    
def commit_message_from_AI(file_path):
    file_dir = os.path.dirname(file_path)
    API_KEY = open(os.path.join(file_dir, "GROQ_API_KEY.txt"), "r").read()
    diff = subprocess.run(["git", "diff", "--", file_path], cwd=file_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    title, commit_message = generate_commit_message_for(API_KEY, diff)
    print(title)
    print(commit_message)

if __name__ == "__main__":
    file_path = sys.argv[1]
    commit_message_from_AI(file_path)

    