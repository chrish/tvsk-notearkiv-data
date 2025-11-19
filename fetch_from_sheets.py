from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# Specify the ID of your Google Sheet and the range of data to fetch
SPREADSHEET_ID = os.environ['GOOGLE_SHEET_ID']
RANGE_NAME = 'Notearkiv!A1:G1500'  # Adjust the range as needed

# Authenticate using the service account
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = service_account.Credentials.from_service_account_file('service_account.json', scopes=SCOPES)

# Build the Sheets API service
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API to fetch the data
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

# Save the data to a JSON file
import json
with open('spreadsheet_data.json', 'w', encoding='utf-8') as f:
    json.dump(values, f, ensure_ascii=False)

print('Data fetched and saved to spreadsheet_data.json')
