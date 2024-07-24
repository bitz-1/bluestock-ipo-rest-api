
from django.contrib import admin
from django.urls import path,include

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('administrator/api/v1/',include('ipoApi.urls')),
    path('api/user/',include('authUser.urls'))
    
]
