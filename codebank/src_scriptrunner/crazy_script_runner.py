from codebank.logger import *
from queue import Queue
import datetime
import threading

def run_script(script_path: str, rowcols: tuple[int, int], seed: int = None) -> Queue:
    """
    Runs the passed script, proxy function to run_script with non-tuple rows and columns.
    """

    # Parameter overloading, calls base function
    return run_script(script_path, rowcols[0], rowcols[1], seed)

def run_script(script_path: str, rows: int, columns: int, seed: int = 5) -> Queue:
    """
    Runs the passed script on a thread, returns a queue that the resulting data will be
    added to.
    """

    # Gets a reference to the return queue (to run script asynchrnously)
    return_queue = Queue()

    # Tries to open the script path
    file = open(script_path, 'r')
    script_content = file.read()
    file.close()

    # Semi-anonymous function, as Thread needs functional argument
    def thread_function():
        exec(script_content, {'rows': rows, 'columns': columns, 'seed': seed, 'return_queue': return_queue})
    
    # Runs thread
    thread = threading.Thread(target=thread_function)
    thread.start()

    # Returns the return queue, when the script is complete, it will be added here
    return return_queue
