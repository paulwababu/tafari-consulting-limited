from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tutorials import views

urlpatterns = [
    path('tutorials/upload/', views.uploadTutorial, name='upload_tutorial'),
    path('tutorials/', views.tutorialList, name='tutorial_list'),
    path('', views.home, name='home'),
    path('accounts/login/', views.signin, name="login"),#LOGIN_REDIRECT_URL = '/accounts/login/'
    path('accounts/logout/', views.signout, name="logout"),
    path('tutorials/<int:pk>', views.deleteTutorial, name='tutorial'),
]

if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
