# Email Bot

Python script that sends personalized HTML newsletter emails with a PDF attachment, using a CSV contact list and Gmail SMTP.

## Setup
1. Copy `contacts.example.csv` to `contacts.csv` and add your contacts.
2. Create a Gmail App Password (Google Account → Security → App passwords).
3. Set environment variables (PowerShell):
   ```powershell
   $env:GMAIL_ADDRESS = "you@gmail.com"
   $env:GMAIL_APP_PASSWORD = "your-16-letter-code"
   $env:SENDER_NAME = "Your Name"
   ```
4. Run `python email_bot.py` (keep `dry_run = True` for testing).

## Related
- Newsletter website: https://akki-27-code.github.io/Asian-Games-2026/
- Website repo: https://github.com/Akki-27-code/Asian-Games-2026
