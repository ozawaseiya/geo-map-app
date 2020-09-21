from django.urls import path
from .views import indexfunc, detailfunc, dangerousfunc

urlpatterns = [
    path('', indexfunc, name='index'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('dangerous/<int:pk>', dangerousfunc, name='dangerous'),
]
