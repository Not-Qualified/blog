"""webgym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from post import views as post_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Post App Routing
    path("", post_views.PostListView.as_view(), name="post-home"),
    path("user/<str:username>", post_views.UserPostListView.as_view(), name="user-post"),
    path("post/<int:pk>/", post_views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", post_views.PostCreateView.as_view(), name="post-create"),
    path("post/update/<int:pk>/", post_views.PostUpdateView.as_view(), name="post-update"),
    path("post/delete/<int:pk>/", post_views.PostDeleteView.as_view(), name="post-delete"),
    path('about/', post_views.about, name="post-about"),

    # User App Routing
    path('register/', user_views.register, name="user-register"),
    # Login & Logout View will going to be of auth_views
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name="user/login.html"),
         name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),
    path('profile/', user_views.profile, name="user-profile"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"),
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),
         name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
