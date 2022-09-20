from email.message import EmailMessage
from app2 import email_password
import ssl
import smtplib

class Email():
    emailSender = 'filosofizer42@gmail.com'
    emailPassword = email_password
    emailReceiver = 'chesoc15@gmail.com'

    def emailHelper():
        subject = input("Enter your Email Subject:")
        body = input("Enter the body of the email:")

    def sendEmail(subject, body):
        email = EmailMessage()
        email['From'] = Email.emailSender
        email['To'] = Email.emailReceiver
        email['subject'] = subject
        email.set_content(body)

        context = ssl.create_default_context()

        # connect over SSL encrypted socket
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            # use SMTP to login to our email account
            smtp.login(Email.emailSender, Email.emailPassword)
            # send the email as a string message to sender
            smtp.sendmail(Email.emailSender, Email.emailReceiver, email.as_string())

def main() -> None:
    subject = input("Enter your Email Subject:")
    body = input("Enter the body of the email:")
    Email.sendEmail(subject, body)

if __name__ == "__main__":
    main();