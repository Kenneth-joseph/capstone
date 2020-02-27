from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.signin,name = 'sign_in'),
    url(r'^postsign/',views.postsign),
]