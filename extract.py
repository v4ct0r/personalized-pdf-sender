import pdfplumber
import os
def remove_first_three(s):
    return s[3:]


def extract_transaction_details(pdf_path):
    full_text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text()

    lines = full_text.split('\n')
    for line in lines:
        if 'ΑΙΤΙΟΛΟΓΙΑ' in line:
           return remove_first_three(line[line.index('ΑΙΤΙΟΛΟΓΙΑ')+len('ΑΙΤΙΟΛΟΓΙΑ'):].strip())

    exit(1)

import os

def delete_pdf_files(pdf_paths):
    for path in pdf_paths:
        try:
            os.remove(path)
            print(f"Deleted {path}")
        except FileNotFoundError:
            print(f"File not found: {path}")
        except PermissionError:
            print(f"Permission denied while deleting {path}. Check if the file is open or write-protected.")
        except Exception as e:
            print(f"An error occurred while deleting {path}: {e}")
import os
import shutil
import time
from custom_exit import custom_exit
def move_pdf_files(pdf_paths, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    date_str = time.strftime("%d-%m-%Y")
    destination_dir_with_date = os.path.join(destination_dir, date_str)
    if not os.path.exists(destination_dir_with_date):
        os.makedirs(destination_dir_with_date)
    for path in pdf_paths:
        try:
            filename = os.path.basename(path)
            destination_path = os.path.join(destination_dir_with_date, filename)
            shutil.move(path, destination_path)
            print(f"Moved {path} to {destination_path}")
        except FileNotFoundError:
            custom_exit(f"File not found: {path}")
        except PermissionError:
            custom_exit(f"Permission denied while moving {path}. Check if the file is open or write-protected.")
        except Exception as e:
            custom_exit(f"An error occurred while moving {path}: {e}")