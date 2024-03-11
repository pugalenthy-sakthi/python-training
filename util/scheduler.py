
from config import scheduler
from util.mail_sender import send_mail

@scheduler.task('cron',id='do_advertise',minute='*')
def advertise_email():
    res = send_mail()
    print(res)