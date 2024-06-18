import os
import pandas as pd
from find_email import is_valid_email
from custom_exit import custom_exit

def check_emails(emails_path):
    # Open the file and read names from column A and emails from column B, assuming the file has headers
    if not os.path.exists(emails_path):
        custom_exit(f"File not found: {emails_path}")
    try:
        # Use header=0 to indicate that the first row contains column names
        df = pd.read_excel(emails_path, header=0)
    except Exception as e:
        custom_exit(f"Failed to read Excel file: {e}")
        
    # Check if the DataFrame has the required columns 'Names' and 'Emails'
    if 'Names' not in df.columns or 'Emails' not in df.columns:
        custom_exit("Error: DataFrame does not have the required 'Names' and 'Emails' columns.")

    print()
    try:
        for index, row in df.iterrows():
            name = row['Names']
            email = row['Emails']
            
            # Check for missing values directly using pandas methods
            if pd.isnull(name) or pd.isnull(email):
                print("Name or email is Empty in row", index+2)
                continue  # Skip further processing for this row
        
            # Convert to string and strip after checking for NaN to avoid 'nan' string issues
            name = str(name).strip()
            email = str(email).strip()
            
            if not is_valid_email(email):
                print(f"{email} is not a valid email")
    except KeyError as e:
        custom_exit(f"KeyError: {e}. Check if the correct column names are being accessed.")