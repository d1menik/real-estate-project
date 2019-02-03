from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages


# Create your views here.
def contact(req):
    if  req.method == 'POST':
        listing_id = req.POST['listing_id']
        listing = req.POST['listing']
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        user_id = req.POST['user_id']
        realtor_email = req.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(req, 'Your request has been submitted, a realtor will get back to you soon.')
        return redirect('/listings/'+listing_id)
