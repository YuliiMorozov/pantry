from django.contrib import admin
from django.urls import path

from pantry_proj.views import index, contact, sign_up, sign_in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    # path('json/', json, name='json'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
]
