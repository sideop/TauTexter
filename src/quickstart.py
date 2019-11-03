from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc16695dcdd43a77dbb7f42478a27ff3f'
auth_token = '1708536a7fe2874d50351d9d8fbc994f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="does this work? uwuwu.",
                     from_='+16144544702',
                     to='+14087867789'
                 )

print(message.sid)
