import mailbox
import re
import pandas as pd

# Replace this path with the path to your downloaded .mbox file
mbox_path = "C:\\Users\\vsunn\\Downloads\\Sent.mbox"

# Create a set to store unique email addresses
emails = set()
mbox = mailbox.mbox(mbox_path)

# Extract all 'To' addresses
for msg in mbox:
    if msg['To']:
        found = re.findall(r'[\w\.-]+@[\w\.-]+', msg['To'])
        emails.update([email.lower() for email in found])

# Convert to DataFrame and save to Excel
df = pd.DataFrame(sorted(emails), columns=['Email'])
df.to_excel('recipient_emails.xlsx', index=False)
# ...existing code...
print("All email addresses saved to 'recipient_emails.xlsx'")
# ...existing code...