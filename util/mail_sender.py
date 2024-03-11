
from config import config,mail
from flask_mail import Message

def send_mail():
    try:
        subject = 'Temp Advertisement'
        recipient = '20csa40@karpgamtech.ac.in'
        body = 'Hi There, This is a temp advertisement'
        msg = Message(subject,sender='sakthi123msd@gmail.com',recipients=[recipient])
        # msg.body(body)
        # mail.send(msg)
    
        return 'email sent successfully'
    
    except Exception as e:
        print(e)
        return 'Error Occurred While Sending Email'
    
    
    