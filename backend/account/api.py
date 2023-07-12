# from .forms import SignupForm
from django.conf import settings
import jwt
from .models import FriendshipRequest, User
from .serializers import UserSerializer, FriendshipRequestSerializer
from django.shortcuts import render
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework import exceptions, status
from rest_framework.response import Response
from .authenticate import generate_access_token, JWTauthentication


@api_view(['POST'])
def register_view(request, *args, **kwargs):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.APIException("Password Does not match")

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return Response({'Message': 'You are already logged in ...'}, status=400)
    email = request.data.get("email")
    password = request.data.get("password")

    user = (
        User.objects.filter(Q(email__iexact=email)
                            | Q(password__iexact=password))
        .distinct()
        .first()
    )

    if user is None:
        raise exceptions.AuthenticationFailed("user not found")

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed("Incorrect password")

    response = Response()
    token = generate_access_token(user)
    response.set_cookie(key="jwt", value=token, httponly=True)
    response.data = {"jwt": token}
    return response


@api_view(["POST"])
def logout_view(request):
    response = Response()
    response.delete_cookie(key="jwt")
    response.data = {"message": "success logout"}
    return response

@api_view(["GET"])
def user_detail(request):
    token = request.COOKIES.get('jwt')
    
    if not token:
        raise exceptions.AuthenticationFailed('Unauthentivated')
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Unauthentivated')
    
    user = User.objects.filter(id=payload['user_id']).first() 
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []
    
    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user, status= FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data
        
    friends = user.friends.all()
    
    return Response({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests,
    })
    

@api_view(['POST'])
def send_friend_request(request, pk):
    user = User.objects.get(pk=pk)
    
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)
    
    if not check1 and not check2:
        FriendshipRequest.objects.create(created_for=user, created_by=request.user)
        return Response({'message': 'friendship request created'})
    else:
        return Response({'message': 'friendship request already sent'})

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
    
    return Response({'message': 'friendship request updated'})

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    