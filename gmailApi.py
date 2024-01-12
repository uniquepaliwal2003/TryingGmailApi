import gmail_api
from gmail_api import GmailAPI # example wrapper library 

# Set up API client 
client = GmailAPI()
client.login('myemail@gmail.com', 'mypassword')

# List labels to find INBOX label id
labels = client.list_labels()
inbox_id = next(l['id'] for l in labels if l['name'] == 'INBOX')

# Fetch last 5 threads in INBOX
threads = client.list_threads(label_ids=[inbox_id], max_results=5) 

# Get messages from threads
messages = []
for t in threads:
  msg = client.get_message(t['id']) 
  messages.append(msg)

# Print message subjects  
for m in messages:
  print(m['subject'])