from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC356e06339444c589aed4f09342d73aca"
# Your Auth Token from twilio.com/console
auth_token  = "3d99721e4252da8c84944969e26f4374"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917042224751", 
    from_="+12183669862",
    body="Hi Douchebag!")

print(message.sid)
