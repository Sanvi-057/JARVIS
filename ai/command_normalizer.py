
def normalize_command(command, command_map):
    command = command.lower().strip()

    for cmd in command_map:
        command_words = set(cmd.split())
        user_words = set(command.split())

        if command_words.issubset(user_words):
            return cmd
