from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api


urlpatterns = [
    # path('meinfo/', api.meinfo, name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', api.LoginView.as_view(), name='login'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', api.user_view, name='user'),
    path('users/', api.user_list, name='user_list'),
    path('friends/<uuid:pk>/', api.friends, name='friends'), 
    path('friends/<uuid:pk>/request/', api.send_friend_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
]
