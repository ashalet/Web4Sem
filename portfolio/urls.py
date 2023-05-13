from django.urls import path
from portfolio.views import *
from api.views import *

urlpatterns = [
    path('', home, name='home'),
    path('all/', all_works, name='all_works'),
    path('blog/', blog, name='blog'),
    path('work/<int:pk>/', work, name='detail-work'),
    path('detail_post/<int:pk>/', detail_post, name='detail-post'),
]
