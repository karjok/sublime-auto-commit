# sublime script for auto commit when save the file
# This file is generated with ChatGPT :)

import sublime
import sublime_plugin
import subprocess
import os
import re



class SublimeGitAutoCommitCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Save the current file
        self.view.run_command('save')

        # Generating Commit Message using AI
        last_commit_message = self.generate_commit_message_for()

        # Prompt for commit message with last commit message as the default text
        self.view.window().show_input_panel("Commit Message:", last_commit_message, self.on_done, None, None)

    def on_done(self, commit_message):
        if commit_message:
            file_path = self.view.file_name()
            file_dir = os.path.dirname(file_path)
            project_root = self.get_project_root(file_dir)
            if project_root:
                # Run git add command
                add_result = subprocess.run(["git", "add", file_path], cwd=project_root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                if add_result.returncode != 0:
                    sublime.error_message(f"Git add failed: {add_result.stderr}")
                    return

                # Run git commit command
                commit_result = subprocess.run(["git", "commit", "-m", commit_message], cwd=project_root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if commit_result.returncode != 0:
                    sublime.error_message(f"Git commit failed: {commit_result.stderr}")
                else:
                    self.save_last_commit_message(commit_message)

    def get_project_root(self, file_dir):
        # Get the root directory of the git repository
        result = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=file_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            sublime.error_message(f"Git repository not found: {result.stderr}")
            return None

    def load_last_commit_message(self):
        settings = sublime.load_settings("SublimeGitAutoCommit.sublime-settings")
        return settings.get("last_commit_message", "")

    def save_last_commit_message(self, commit_message):
        settings = sublime.load_settings("SublimeGitAutoCommit.sublime-settings")
        settings.set("last_commit_message", commit_message)
        sublime.save_settings("SublimeGitAutoCommit.sublime-settings")

    def generate_commit_message_for(self):
        file_path = self.view.file_name()
        file_dir = os.path.dirname(file_path)
        diff = subprocess.run(["git", "diff", "--", file_path], cwd=file_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        script_path = os.path.join(sublime.packages_path(), "User", "SGAC_AI.py")
        script_dir = os.path.dirname(script_path)
        commit_message = subprocess.run(["python3", script_path, file_path], cwd=script_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if commit_message.returncode != 0:
            sublime.error_message(f"Groq AI failed: {commit_message.stderr}")
        
        return commit_message.stdout