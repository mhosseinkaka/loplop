from django.http.response import HttpResponse 
import json
from bottle.models import User, Message
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    if request.method =="POST":
        data =json.loads(request.body)
        User.objects.create(
            first_name= data.get("first_name"),
            last_name= data.get("last_name"),
            phonenumber= data.get("phonenumber")
            
                    )
        return HttpResponse("user created!")

@csrf_exempt
def add_message(request):
    if request.method =="POST":
        data =json.loads(request.body)
        Message.objects.create(
            sender_id = data.get("sender_id"),
            reciever = None,
            text = data.get("text"),
        )
        return HttpResponse("message sent!")



    




