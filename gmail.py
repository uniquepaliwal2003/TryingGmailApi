import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://mail.google.com/"]


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  print("Hello")
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
        # Call the Gmail API
      service = build("gmail", "v1", credentials=creds)
      messages = service.users().messages().list(userId='me', maxResults=3).execute()

      if "messages" not in messages:
        print("No messages found.")
        return

      print("Last three emails:")
      for message in messages["messages"]:
            email = service.users().messages().get(userId='me', id=message["id"]).execute()
            print("Email ID:", email["id"])
            print("Snippet:", email["snippet"])
            print("-" * 20)

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
      print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()