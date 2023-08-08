from codebank.src_logic.crazy_controller import controller
from codebank.src_scriptrunner.crazy_script_scanner import *
import logging
import datetime

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, filename=f"logbank/crazymaze-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log", filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

    x = find_scripts("scriptbank/", True)

    controller = controller()
    exit()