from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.signin,name = 'sign_in'),
    url(r'^postsign/',views.postsign),
    url(r'^logoout/',views.logout,name='logout'),
    url(r'^signUp/',views.signUp,name='sign_up'),
    url(r'^postsignup/',views.postsignup,name='postsignup'),
    url(r'^create/',views.create,name='create'),
    url(r'^postcreate/',views.postcreate,name='postcreate'),
]