from pipe import Pipe
from notification import Notification
from config import ALERTS_TOKEN, PIPE_NAME
from donationalerts import Alert
from donationalerts.donationalerts import Event
from transliterator import transliterate, trim

alert = Alert(ALERTS_TOKEN)

try:
	pipe = Pipe(PIPE_NAME)
except:
	print("Unable to run Pipe! Maybe you forgot to inject 'notifications-in-gd.dll'?")
	input("")
	exit(1)
	

pipe.send_string(Notification("GDonationAlerts started!", "Waiting for new donations...").as_gd_format())

@alert.event()
def new_donation(event: Event):
	print(transliterate(event.username))
	pipe.send_string(
		Notification(
            "New donation!", 
            f"{trim(transliterate(event.username), 20)} donated you {event.amount_formatted} {event.currency}!"
	    ).as_gd_format()
	)