#general text function
from twilio.rest import Client


def text(reciever, body):
    account_sid = "ACb2dcf430b080f2089235fe055b11b34d"
    auth_token = "2abf6369e7b4111841965780a04607d1"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=reciever,
        from_="+16302803348",
        body=body)

