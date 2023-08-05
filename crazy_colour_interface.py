import os

COLOUR_SCHEME_FOLDER = "./crazy_colour_schemes"

def scan_colour_schemes() -> list[str]:
    file_names: list[str]
    file_names = []

    for filename in os.listdir(COLOUR_SCHEME_FOLDER):
        file_path:str
        file_path = os.path.join(COLOUR_SCHEME_FOLDER, filename)

        # Check if the item is a file (not a directory)
        if os.path.isfile(file_path):

            # Remove the file extension before appending to the list
            name_without_extension:str
            name_without_extension = os.path.splitext(filename)[0]
            file_names.append(name_without_extension)

    return file_names