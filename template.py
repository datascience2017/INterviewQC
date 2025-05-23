import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
logging.info("hello everyone")
list_of_files = [
    "src/_init_.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py"
    "research/trials.ipynb",
    "app.py"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the files")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)):
        with open(filepath, 'a') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
        
    else:
        logging.info(f"File {filename} already exists.")