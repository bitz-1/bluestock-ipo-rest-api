from django.urls import path
from authUser.views import UserRegistrationView,UserLoginView,UserProfileView,IpoListView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [ 
   path ('register/',UserRegistrationView.as_view(),name='register'),
   path ('login/',UserLoginView.as_view(),name='login'),
   path ('profile/',UserProfileView.as_view(),name='profile'),
   path ('ipo/',IpoListView.as_view(),name='ipo'),
   path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
   path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
   path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]
