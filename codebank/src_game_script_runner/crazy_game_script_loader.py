import os
from tkinter import *
import importlib
import inspect
from scriptbank.crazy_script_base import script_base

def scan_scripts(path: str = "scriptbank/crazy_game_scripts") -> list[str]:
    """
    load the scripts from scriptbank
    """

    # Get list of files in the directory
    file_list = os.listdir(path)

    # Filter the list to include only .py and .pyw files
    py_file_list = [file_name for file_name in file_list if file_name.endswith(".py") or file_name.endswith(".pyw")]



    return py_file_list


def load_script(file_name:str, path:str="scriptbank/crazy_game_scripts",) -> dict[str, Frame]:
    """
    retrieve the setup frame for every script
    """

    # Construct the module name from the file name
    module_name = file_name.replace(".py", "").replace(".pyw", "")
    full_module_name = f"scriptbank.crazy_game_scripts.{module_name}"  # Include the package name

    # Import the module dynamically
    module = importlib.import_module(full_module_name)
    
    # Loop through the attributes of the module
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        
        # Check if the attribute is a class and inherits from ScriptBase
        if inspect.isclass(attribute) and issubclass(attribute, script_base) and attribute is not script_base:

            attribute_instance = attribute()
            return attribute_instance
