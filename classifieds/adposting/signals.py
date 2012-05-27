"""
  $Id$


"""

from paypal.standard.signals import payment_was_successful
from models import Payment
        
def make_payment(sender, **kwargs):
  payment = Payment.objects.get(pk=sender.item_number)
	payment.paid = True
	payment.paid_on = datetime.datetime.now()
	payment.save()
	payment.ad.make_payment(payment)

payment_was_successful.connect(make_payment)
