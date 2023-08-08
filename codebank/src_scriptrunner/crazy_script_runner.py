from codebank.logger import *
from queue import Queue
import datetime

def run_script(script_path: str, rowcols: tuple[int, int], seed: int = None) -> Queue:
    return run_script(script_path, rowcols[0], rowcols[1], seed)

def run_script(script_path: str, rows: int, columns: int, seed: int = None) -> Queue:
    if seed is None: seed = int(datetime.now())