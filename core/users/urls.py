# from django.urls import path, include

# from core.users import admin
# from .views import signup_api, login_api, signup, dashboard
# from django.contrib.auth.views import LoginView

# urlpatterns = [
#     path('signup/', signup_api),
#     path('login/', login_api),
#     path('web/signup/', signup, name='signup'),
#     path('web/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('dashboard/', dashboard, name='dashboard'),
#     path("api/notes/", include("notes.urls")),
# ]

from django.urls import path
from .views import signup_api, login_api, signup, dashboard
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', signup_api),
    path('login/', login_api),
    path('web/signup/', signup, name='signup'),
    path('web/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]