from codebank.logger import *
from queue import Queue
import datetime
import threading

def run_script(script_path: str, rowcols: tuple[int, int], seed: int = None) -> Queue:
    return run_script(script_path, rowcols[0], rowcols[1], seed)

def run_script(script_path: str, rows: int, columns: int, seed: int = None) -> Queue:
    if seed is None: seed = 5

    return_queue = Queue()

    file = open(script_path, 'r')
    script_content = file.read()
    file.close()

    def thread_function():
        exec(script_content, {'rows': rows, 'columns': columns, 'seed': seed, 'return_queue': return_queue})
    
    thread = threading.Thread(target=thread_function)
    thread.start()
