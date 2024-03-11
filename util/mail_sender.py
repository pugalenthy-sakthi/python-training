import traceback
from config import config,mail
from flask_mail import Message
from database import user_services

def send_mail():
    try:
        subject = 'Temp Advertisement'
        recipient = []
        users = user_services.get_users()
        for user in users:
            recipient.append(user.email)
        body = 'Hi There, This is a temp advertisement'
        msg = Message(subject,sender='sakthi123msd@gmail.com',recipients=recipient)
        msg.body = body
        mail.send(msg)
    
        return 'email sent successfully'
    
    except Exception as e:
        print(traceback.print_exception(e))
        return 'Error Occurred While Sending Email'
    
    
    