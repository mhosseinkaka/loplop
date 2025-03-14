from django.urls import path
from bottle.views import add_message, signup, show_message

urlpatterns = [
    path('signup/', signup),
    path('add-message/', add_message),
    path('show-message/', show_message),
]
