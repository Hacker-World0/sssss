import requests

# URL of the Discord webhook
webhook_url = "https://discord.com/api/webhooks/1185912541679992872/VJm0IS7eeMOtNwd7BzrGqi-2MZ5WTGTiRoYqvMotJVyV-Iy-p3YcsDgvLhrjnicBbm77"

# The message to be sent
data = {
    "content": "madartod"
}

# Sending the request to the Discord webhook
response = requests.post(webhook_url, json=data)

# Checking if the request was successful
if response.status_code == 204:
    print("Message sent successfully.")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
