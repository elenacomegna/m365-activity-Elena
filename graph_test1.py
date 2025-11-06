import requests

access_token = 'INSERISCI_IL_TUO_TOKEN_DI_ACCESSO'

url = 'https://graph.microsoft.com/v1.0/me'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Attività registrata con successo!")
    print(response.json())
else:
    print(f"Errore: {response.status_code}")
    print(response.text)
