from auth_sys import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.AuthPageView.as_view(), name='auth-page'),
    path('register/', views.registration, name='register'),
    path('login/', LoginView.as_view(template_name='auth_sys/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/update/', views.profile_update, name='profile-update'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/add/', views.portfolio_add, name='portfolio-add'),
]