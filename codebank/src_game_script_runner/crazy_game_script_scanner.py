import os

def load_scripts(path:str="scriptbank/crazy_game_scripts") -> list[str]:
    """
    load the scripts from scriptbank
    """

    # Get list of scripts using os module
    #scripts: list(str)
    #scripts = [os.path.join(root, file) for root, _, files in os.walk(path) for file in files if file.endswith(".py")]

    return os.listdir(path)
