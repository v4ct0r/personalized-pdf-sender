import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from custom_exit import custom_exit
import os
from pdf_funcs import delete_pdf_files


def send_email(client):
    # Email configuration
    email_address = os.environ.get('EMAIL_ADDRESS')
    if email_address is None:
        custom_exit("EMAIL_ADDRESS environment variable is not set.")

    # Correctly retrieve the EMAIL_PASSWORD environment variable
    email_password = os.environ.get('EMAIL_PASSWORD')
    if email_password is None:
        custom_exit("EMAIL_PASSWORD environment variable is not set.")

    print(f"Sending email to {client['email']}...")
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = client['email']
    msg['Subject'] = 'Transaction Details'
    
    body = ' '
    msg.attach(MIMEText(body, 'plain'))
    
    for pdf_path in client['pdf_paths']:
        attachment = open(pdf_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(pdf_path)}')
        msg.attach(part)
    
    import smtplib
    from smtplib import SMTPException
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, client['email'], text)
        print(f"Email sent to {client['email']} successfully")
        return True
    except smtplib.SMTPRecipientsRefused:
        custom_exit(f"Failed to send email: The recipient's email address was refused.")
    except smtplib.SMTPException as e:
        custom_exit(f"Failed to send email due to an SMTP error: {e}")
    except Exception as e:
        custom_exit(f"An unexpected error occurred: {e}")
    finally:
        server.quit()