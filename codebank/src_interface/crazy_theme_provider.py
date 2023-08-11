import json

class theme_provider():

    def __init__(self) -> None:
        self.load_theme_from_file()

    def load_theme_from_file(self, path: str = "databank/crazy_menu_schemes/crazy_menu_default.json") -> None:
        
        # Opening JSON file & Importing
        file = open(path)
        scheme_data = json.load(file)
        print(scheme_data)
        self.import_scheme(scheme_data)
        file.close()

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
        self.scheme_data = scheme_data

if __name__ == "__main__":
    themer = theme_provider()
    print("theme provider ({themer})")
    for (key, value) in themer.scheme_data.items():
        print(f"    {key}   :   {value}")