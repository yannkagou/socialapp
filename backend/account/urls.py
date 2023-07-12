from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api


urlpatterns = [
    # path('meinfo/', api.meinfo, name='me'),
    path('signup/', api.registerView, name='signup'),
    path('login/', api.loginView, name='login'),
    path('refresh/', api.CookieTokenRefreshView.as_view()),
    path('logout/', api.logoutView),
    path("user/", api.user),
    # path('user/', api.user_view, name='user'),
    path('users/', api.user_list, name='user_list'),
    path('friends/<uuid:pk>/', api.friends, name='friends'), 
    path('friends/<uuid:pk>/request/', api.send_friend_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
]


