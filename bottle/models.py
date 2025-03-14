from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)


class Message(models.Model):
    sender =models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="sent_messages")
    reciever = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="recieved_message", null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


        
    

