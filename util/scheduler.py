from config import scheduler
from util.mail_sender import send_mail
from application import app


@scheduler.task('interval',id='do_advertise',minutes=10)
def advertise_email():
    with app.app_context():
        res = send_mail()
        print(res)
    
        
        