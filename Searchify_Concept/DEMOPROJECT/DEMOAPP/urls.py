from django.urls import path
from . import views
urlpatterns =[
      path('HOME',views.HOME ,name="HOME"),
      path('AboutUs',views.AboutUs,name="AboutUs"),
      path('ContactInfo',views.Contactinfo,name="ContacInfo"),
      path('TEAM',views.TEAM,name="TEAM"), 
      path('SUPPORT',views.SUPPORT,name="SUPPORT"),
      path('Maintanace',views.Maintanace,name="Maintanace"),
      path('signup',views.signup,name="signup"),
      path('team',views.team,name="team"),
]