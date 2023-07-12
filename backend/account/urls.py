from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api


urlpatterns = [
    path('signup/', api.register_view, name="register"),
    path('login/', api.login_view, name="login"),
    path('user/', api.user_detail, name='user'),
    path('logout/', api.logout_view, name="logout"),
    path('users/', api.user_list, name='user_list'),
    path('friends/<uuid:pk>/', api.friends, name='friends'), 
    path('friends/<uuid:pk>/request/', api.send_friend_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
]


