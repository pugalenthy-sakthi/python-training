from config import scheduler
from util.mail_sender import send_mail

@scheduler.task('interval',id='do_advertise',minutes=10)
def advertise_email():
    from application import app
    with app.app_context():
        res = send_mail()
        print(res)
    
        
        