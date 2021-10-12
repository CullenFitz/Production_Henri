from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mysql.connector
#from text import text
from chatterbot import ChatBot



#Connect to Henri DB
db = mysql.connector.connect(user='cullenf', password='ff@47NiwvAGF6rJ',
                             host='cullenf.mysql.pythonanywhere-services.com',
                             database='cullenf$HenriDB'
)


Henri = ChatBot('Henri')

cursor0 = db.cursor()


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def incoming_sms():
    body = request.values.get('Body', None)
    bodyLower = body.lower()
    from_number = str(request.values.get('From'))
    resp = MessagingResponse()

    cursor0.execute("SELECT name FROM Contacts WHERE number = {}".format(from_number))
    name = cursor0.fetchall()
    name=[i[0] for i in name]
    name = str(name[0])
    henri_response = Henri.get_response(bodyLower)
    henri_response_conf = henri_response.confidence
    if henri_response_conf > 0.8:
        try:
            resp.message(str(henri_response))
        except:
            resp.message("I am having trouble")
    else:
        resp.message("I'm not sure what that means. Do you need something?")



    return str(resp)
