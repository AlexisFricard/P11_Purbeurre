"""
purbeurre URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import (
    handler400, handler403, handler404, handler500
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('', include('usermanage.urls')),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(       # noqa
            template_name='password_reset_form.html'
        ),
        name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

handler404 = 'usermanage.views.error_404'  # noqa
handler400 = 'usermanage.views.error_400'  # noqa
handler403 = 'usermanage.views.error_403'  # noqa
handler500 = 'usermanage.views.error_500'  # noqa
