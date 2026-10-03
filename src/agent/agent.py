import json
import re
from pathlib import Path

from .llm import LocalLLM
from src.tools.apps import open_application


class LeFantome:

    def __init__(self):
        self.llm = LocalLLM()

        # Load commands.json
        base_dir = Path(__file__).resolve().parent.parent
        commands_path = base_dir / "preHelpers" / "commands.json"

        with open(commands_path, "r", encoding="utf-8") as file:
            self.commands_data = json.load(file)

        self.commands = self.commands_data.get("commands", {})

    def normalize_command(self, command: str) -> str:
        """
        Normalize the user's command so small differences
        don't require the LLM.
        """

        command = command.lower().strip()

        # Remove punctuation
        command = re.sub(r"[?!.,]+$", "", command)

        # Remove common polite prefixes
        command = re.sub(
            r"^(please\s+|can you\s+|could you\s+|would you\s+)+",
            "",
            command
        )

        # Remove "the" after an action
        command = re.sub(
            r"^(open|launch|start|close|quit|exit)\s+the\s+",
            r"\1 ",
            command
        )

        # Remove unnecessary app/application at the end
        command = re.sub(
            r"\s+(app|application)$",
            "",
            command
        )

        return command.strip()

    def find_known_command(self, command: str):
        """
        Try to match the user's command against commands.json.
        Returns action data if matched, otherwise None.
        """

        command = self.normalize_command(command)

        for command_name, command_data in self.commands.items():

            phrases = command_data.get("phrases", [])

            for phrase in phrases:

                # Convert {app} / {folder} into a capture group
                pattern = re.escape(phrase)

                pattern = pattern.replace(
                    r"\{app\}",
                    r"(.+)"
                )

                pattern = pattern.replace(
                    r"\{folder\}",
                    r"(.+)"
                )

                match = re.fullmatch(
                    pattern,
                    command,
                    re.IGNORECASE
                )

                if match:
                    action = command_data.get("action", {}).copy()

                    # Extract parameters
                    if "{app}" in phrase:
                        app_name = match.group(1).strip()

                        aliases = command_data.get("apps", {})

                        app_name = aliases.get(
                            app_name,
                            app_name
                        )

                        action["app"] = app_name

                    if "{folder}" in phrase:
                        action["folder"] = match.group(1).strip()

                    return action

        return None

    def execute_action(self, action):
        """
        Execute an action returned by the command router.
        """

        action_type = action.get("type")

        if action_type == "open_application":

            app_name = action.get("app")

            if not app_name:
                return "Application name is missing."

            return open_application(app_name)

        return None

    def process(self, command: str) -> str:

        # ==========================================
        # 1. TRY KNOWN COMMANDS
        # ==========================================

        action = self.find_known_command(command)

        if action:

            result = self.execute_action(action)

            if result is not None:
                return result

        # ==========================================
        # 2. UNKNOWN COMMAND → LLM
        # ==========================================

        response = self.llm.ask(command)

        try:
            data = json.loads(response)

            if data.get("tool") == "open_application":

                app_name = data["arguments"]["app_name"]

                return open_application(app_name)

            return response

        except json.JSONDecodeError:

            return response