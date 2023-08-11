from codebank.src_logic.crazy_controller import controller
from codebank.src_scriptrunner.crazy_script_scanner import *
from codebank.src_scriptrunner.crazy_script_runner import *
from codebank.src_interface.crazy_setup_frame_controller import *
from codebank.logger import *

if __name__ == "__main__":
    #start()
    #exit()

    x = find_scripts("scriptbank/", True)

    q = run_script("scriptbank/prim.py", 5, 5)
    while(q.qsize() == 0):
        print(q.qsize())
        time.sleep(0.05)
    print(q.get())

    controller = controller()
    exit()