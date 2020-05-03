from django.template.loader import render_to_string
from django.core.signing import Signer
from bboard.settings import ALLOWED_HOSTS

signer = Signer()

def send_activation_notification(user):

	host ='http://' + ALLOWED_HOSTS[0] if ALLOWED_HOSTS else 'http://127.0.0.1:8000'
	context = {'user': user, 'host': host,
			   'sign':signer.sign(user.username)}
	subject = render_to_string('email/activation_letter_subject.txt', context)
	body_text = render_to_string('email/activation_letter_body.txt', context)
	user.email_user(subject, body_text)