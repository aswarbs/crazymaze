from codebank.logger import *
import os

def find_scripts(directory: str = "scriptbank/", show_errors: bool = False):

    # Get list of scripts using os module
    python_files: list(str)
    python_files = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith(".py")]
    logging.debug(f"crazy_script_scanner: scanning {len(python_files)} files ending in .py in scriptbank/:\n ")

    # For each script, try and run it using a 10x10 test array, to ensure it is a valid file.
    for script_index, script_path in enumerate(python_files):
        logging.debug(f"\tcrazy_script_scanner : script {script_index} : testing {script_path} with a 10x10 test maze")

        try:
            # Open the file and read it
            with open(script_path, 'r') as file:
                script_content = file.read()
            
            # Attempt to execute script
            exec(script_content)
            logging.debug(f"\tcrazy_script_scanner : script {script_index} : successfully executed {script_index}\n")

        except Exception as script_failure_message:
            # On exception, flag as None and show error if applicable.
            python_files[script_index] = None
            logging.debug(f"\tcrazy_script_scanner : script {script_index} : failed to run, {script_path} will no longer be selectable" + ("\n" if not show_errors else ""))

            if (show_errors): logging.debug(f"\t\t script {script_index} error: {script_failure_message}\n")

        continue

    # Replace all flagged scripts (erroneous) & return
    python_files = list(filter(lambda value: value is not None, python_files))
    logging.debug(f"crazy_script_scanner: scanning complete, {len(python_files)} scripts passed validation and will be accessible\n")
    return python_files


if __name__ == "__main__":
    print(find_scripts("././scriptbank/", True))