from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views.user_views import UserViewSet, UserPreferencesView
from events.views.auth_views import SignUpView, LoginView, LogoutView, TokenRefreshView
from events.views.category_views import CategoryViewSet

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

category_router = DefaultRouter()
category_router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(user_router.urls)),
    path('preferences/', UserPreferencesView.as_view(), name='user-preferences'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(category_router.urls)),
]
