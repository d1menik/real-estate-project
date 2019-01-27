from django.shortcuts import render
from .models import Listing


# Create your views here.
def index(req):
    return render(req, 'listings/listings.html')


def listing(req):
    return render(req, 'listings/listing.html')


def search(req):
    return render(req, 'listings/search.html')
