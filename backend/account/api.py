from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .authenticate import CustomAuthentication
from .forms import SignupForm
from .models import FriendshipRequest, User
from .serializers import UserSerializer, FriendshipRequestSerializer
# from django.contrib.auth import get_user_model
# from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
import requests
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def user_view(request):
    accessToken = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
    
    if not accessToken:
        return Response({"Unauthenticated, no access token"}, status=status.HTTP_404_NOT_FOUND)
    
    # return Response(accessToken)
    
    response = requests.get('http://localhost:8000/api/user/', headers= {'Authorization': 'Bearer' + accessToken})

    user = response.json()
    return Response(user)



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        response = Response()        
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                                    value = data["access"],
                                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                # response.data = {"Success" : "Login successfully","data":data}
                # return response
                response.data = data
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid email or password!!"}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def meinfo(request):
#     user = request.user
#     return JsonResponse({
#         'id': user.id,
#         'name': user.name,
#         'email': user.email,
#     })


@api_view(['POST'])
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse(serializer.data, safe=False)



# User = get_user_model()

@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []
    
    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user, status= FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data
        
    friends = user.friends.all()
    
    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests,
    }, safe=False)
    

@api_view(['POST'])
def send_friend_request(request, pk):
    user = User.objects.get(pk=pk)
    
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)
    
    if not check1 and not check2:
        FriendshipRequest.objects.create(created_for=user, created_by=request.user)
        return JsonResponse({'message': 'friendship request created'})
    else:
        return JsonResponse({'message': 'friendship request already sent'})

@api_view(['POST'])
def handle_request(request, status, pk):
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship_request.status = status
    friendship_request.save()
    
    user.friends.add(request.user)
    user.friend_count = user.friend_count + 1
    user.save()
    
    request_user = request.user
    request_user.friend_count = request_user.friend_count + 1
    request_user.save()
    
    return JsonResponse({'message': 'friendship request updated'})

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)
    