import csv
import os
import smtplib
import time
from email.message import EmailMessage

# ---- Settings (read from environment variables) ----
my_email = os.environ["GMAIL_ADDRESS"]
my_password = os.environ["GMAIL_APP_PASSWORD"]
sender_name = os.environ.get("SENDER_NAME", "Your Name")
title = "Asia Sports Insider"
read_more_link = "https://akki-27-code.github.io/Asian-Games-2026/"
attach_file = "newsletter.pdf"   # set to None if no attachment
dry_run = True   # True = just print, False = actually send


# read contacts and message
file = open("contacts.csv", newline="", encoding="utf-8")
contacts = list(csv.DictReader(file))
file.close()

msg_file = open("message.txt", encoding="utf-8")
message_template = msg_file.read()
msg_file.close()

print("Found", len(contacts), "contacts")


# makes one email for one person
def make_email(name, company, to_email):
    text = message_template.replace("{{name}}", name).replace("{{company}}", company)

    html_version = """
    <html><body style="font-family:Arial; background:#f4f6f8;">
    <table width="600" align="center" style="background:white; border-radius:8px;">
    <tr><td style="background:#2563eb; color:white; padding:20px; text-align:center; font-size:20px;">
    """ + title + """
    </td></tr>
    <tr><td style="padding:20px; font-size:15px; line-height:1.6;">
    """ + text.replace("\n", "<br>") + """
    <p style="text-align:center;">
    <a href=\"""" + read_more_link + """\" style="background:#2563eb; color:white; padding:10px 20px; border-radius:5px; text-decoration:none;">Read More</a>
    </p>
    </td></tr>
    </table></body></html>
    """

    email = EmailMessage()
    email["From"] = sender_name + " <" + my_email + ">"
    email["To"] = to_email
    email["Subject"] = name + ", your " + title + " is here"
    email.set_content(text)
    email.add_alternative(html_version, subtype="html")

    if attach_file:
        f = open(attach_file, "rb")
        email.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=attach_file)
        f.close()

    return email


# send to everyone
if dry_run:
    print("-- dry run, nothing will be sent --")
    for c in contacts:
        print("would send to:", c["email"])
else:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30)
    server.login(my_email, my_password)

    for c in contacts:
        email = make_email(c["name"], c["company"], c["email"])
        try:
            server.send_message(email)
            print("sent to", c["email"])
        except Exception as e:
            print("failed for", c["email"], "-", e)
        time.sleep(2)

    server.quit()

print("done!")