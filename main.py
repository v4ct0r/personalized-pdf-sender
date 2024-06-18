import os
from extract import delete_pdf_files, extract_transaction_details , move_pdf_files
from find_email import find_email 
from find_email import is_valid_email
from sent_email import send_email

greek_to_english_map = {
    'Α': 'A', 'Β': 'B', 'Γ': 'G', 'Δ': 'D', 'Ε': 'E', 'Ζ': 'Z', 'Η': 'H', 'Θ': 'Th', 'Ι': 'I', 'Κ': 'K', 'Λ': 'L', 'Μ': 'M', 'Ν': 'N', 'Ξ': 'X', 'Ο': 'O', 'Π': 'P', 'Ρ': 'R', 'Σ': 'S', 'Τ': 'T', 'Υ': 'Y', 'Φ': 'F', 'Χ': 'Ch', 'Ψ': 'Ps', 'Ω': 'O',
    'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'h', 'θ': 'th', 'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x', 'ο': 'o', 'π': 'p', 'ρ': 'r', 'ς': 's', 'σ': 's', 'τ': 't', 'υ': 'y', 'φ': 'f', 'χ': 'ch', 'ψ': 'ps', 'ω': 'o'
}

def greek_to_eng(text):
    return ''.join(greek_to_english_map.get(char, char) for char in text)

flag = False
directory_path = 'transactions/'
pdf_files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
clients = {}
for pdf_file in pdf_files:
    pdf_path = os.path.join(directory_path, pdf_file)
    print(f'Processing {pdf_path}')
    client = extract_transaction_details(pdf_path)
    if client in clients:
        clients[client]["pdf_paths"].append(pdf_path)
        #print(greek_to_eng(client))
    else:
        clients[client] = {"pdf_paths": [pdf_path]}
        #print(greek_to_eng(client))
        email = find_email(client, 'emails/emails.xlsx')
        clients[client]["email"] = email
for client in clients:
    if not is_valid_email(clients[client]["email"]):
        #add boolean to check if email is valid
        flag = True
        clients[client]["valid_email"] = False
    else:
        clients[client]["valid_email"] = True

if flag:
    print("--------------Invalid email found--------------")
    for client in clients:
        if not clients[client]["valid_email"]:
            print(f'Client: {client}, Email: {clients[client]["email"]}, PDFs: {clients[client]["pdf_paths"]}')
print('\n')

for client in clients:
    if clients[client]["valid_email"]:
        if(send_email(clients[client])):
           # delete_pdf_files(clients[client]["pdf_paths"])
            move_pdf_files(clients[client]["pdf_paths"], 'processed_transactions')
input("Press Enter to close the program")

