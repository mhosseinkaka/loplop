from django.urls import path
from bottle.views import add_message, signup

urlpatterns = [
    path('signup/', signup),
    path('add-message/', add_message)
]
