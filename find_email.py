import pandas as pd
from custom_exit import custom_exit
import os
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def find_email(name, file_path):
    try:
        df = pd.read_excel(file_path, header=0)
    except Exception as e:
        custom_exit(f"Error reading Excel file: {e}")

    if df.shape[1] < 2:
        return "Error: DataFrame does not have enough columns. Expected at least 2 columns."

    try:
        matched_email = df[df.iloc[:, 0].str[:5] == name[:5]].iloc[:, 1].tolist()
        if len(matched_email) > 1:
            print(f"Multiple emails found for {name}. Please check the Excel file.")
            if(input("Press '1' to exit or Enter to continue: ") == '1'):
                exit(1)
            else:
                print('choose the correct email for name = ', name)
                for i in range(len(matched_email)):
                    print(f"{i+1}: {matched_email[i]}")
                while True:
                    index = int(input("Enter the index of the correct email: ")) - 1
                    if 0 <= index < len(matched_email):
                        break
                    else:
                        print("Invalid index, please try again.")
                
        else:
            index = 0
        if matched_email:
            if pd.isna(matched_email[index]):
                return "Email missing"
            elif is_valid_email(matched_email[index]):
                return matched_email[index]
            else:
                return "Invalid email format"
        else:
            return "Client's name not found in the Excel file"
    except KeyError as e:
        print(f"Key error: {e}")
        return "Error in processing DataFrame"