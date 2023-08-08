import logging
import datetime

# Setup the logger
logging.basicConfig(level=logging.DEBUG, filename=f"logbank/crazymaze-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log", filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
