#menu 
import os
from check_emails import check_emails
from extract import extract_transaction_details
from find_email import find_email


print("1. Sent Emails")
print("2. Check Emails")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == '1':
    print("Processing...")
elif choice == '2':
    check_emails('emails/test.xlsx')
elif choice == '3':
    exit()