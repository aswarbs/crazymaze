from codebank.src_logic.crazy_controller import controller
from codebank.src_scriptrunner.crazy_script_scanner import *
from codebank.logger import *

if __name__ == "__main__":

    
    x = find_scripts("scriptbank/", True)

    controller = controller()
    exit()