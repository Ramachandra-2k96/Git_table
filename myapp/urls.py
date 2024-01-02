from django.urls import path
from myapp.views import home,form_input,random1,stxt
urlpatterns = [
    path('',form_input),
    path('random',random1,name="random"),
    path('home/<str:file>', home, name='home'),
    path('sampletext/', stxt, name='sampletext'),
]