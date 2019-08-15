from django.urls import path, reverse_lazy, re_path
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('done/', password_reset_done, name='password_reset_done'),
    re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('complete/', password_reset_complete, name='password_reset_complete')
]