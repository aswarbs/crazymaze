import json
from codebank.logger import *

# Hard Coded Theme (in-case no theme can be found)
global INBUILT_MENU_THEME_DEFAULT
INBUILT_MENU_THEME_DEFAULT = """{
    "dock_background": "#1A659E",
    "dock_tab_background_unselected": "#004E89",
    "dock_tab_text_unselected": "#002E51",
    "dock_tab_background_selected": "#EFEFD0",
    "dock_tab_text_selected": "#492C00",
    "text_colour": "#492C00",
    "frame_colour": "#EFEFD0",
    "accent": "#F7C59F",
    "title_font": "Times New Roman",
    "body_font": "Arial",
    "play_button": "#53AF62"
}"""


class theme_provider():

    def __init__(self) -> None:
        self.load_theme_from_file()

    def load_theme_from_file(self, path: str = "databank/crazy_menu_schemes/crazy_menu_default.json") -> None:
        
        # Opening JSON file & Importing
        try:
            file = open(path)
            scheme_data = json.load(file)
            print(scheme_data)
            self.import_scheme(scheme_data)
            file.close()
        except Exception as colour_scheme_failure_message:
            # If that fails, use defualt
            logging.debug(f"theme_provider: failed to import menu scheme {path}, exception: {colour_scheme_failure_message}")
            self.import_scheme(INBUILT_MENU_THEME_DEFAULT)

    def import_scheme(self, scheme_data: dict[str, str]) -> None:

        # Associating Variables to their JSON definitions
        self.dock_background = scheme_data["dock_background"]
        self.dock_tab_background_unselected = scheme_data["dock_tab_background_unselected"]
        self.dock_tab_text_unselected = scheme_data["dock_tab_text_unselected"]
        self.dock_tab_background_selected = scheme_data["dock_tab_background_selected"]
        self.dock_tab_text_selected = scheme_data["dock_tab_text_selected"]
        self.text_colour = scheme_data["text_colour"]
        self.frame_colour = scheme_data["frame_colour"]
        self.accent = scheme_data["accent"]
        self.title_font = scheme_data["title_font"]
        self.body_font = scheme_data["body_font"]
        self.play_button = scheme_data["play_button"]
        self.scheme_data = scheme_data

if __name__ == "__main__":
    themer = theme_provider()
    print("theme provider ({themer})")
    for (key, value) in themer.scheme_data.items():
        print(f"    {key}   :   {value}")