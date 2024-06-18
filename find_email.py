import pandas as pd
import os
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def find_email(name, file_path):
    try:
        df = pd.read_excel(file_path, header=0)
    except Exception as e:
        print(f"\033[91mFailed to read Excel file in {file_path}\033[0m")
        return "Failed to read Excel file"

    # Check DataFrame structure
    if df.shape[1] < 2:
        return "Error: DataFrame does not have enough columns. Expected at least 2 columns."

    # Attempt to find the client's email
    try:
        name_sliced = name[:25]
        # Compare 'name_sliced' with the first 25 characters of each name in the first column of the DataFrame
        # Then, select the email from the second column for rows where the names match
        matched_email = df[df.iloc[:, 0].str[:25] == name_sliced].iloc[:, 1].tolist()
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
            # Check if the email is NaN before checking if it's valid
            if pd.isna(matched_email[index]):
                return "Email missing"
            elif is_valid_email(matched_email[index]):
                return matched_email[index]
            else:
                return "Invalid email format"
        else:
            return "Name not found in Excel file"
    except KeyError as e:
        print(f"Key error: {e}")
        return "Error in processing DataFrame"

