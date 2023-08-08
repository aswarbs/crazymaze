import os

COLOUR_SCHEME_FOLDER: str
COLOUR_SCHEME_FOLDER = "databank/crazy_colour_schemes"

def scan_colour_schemes() -> list[str]:
    """
    Return a list of file names in the colour scheme folder.
    """

    file_names: list[str]
    file_names = []

    # For each file in the colour scheme folder,
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