from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import FriendshipRequest, User
from .serializers import UserSerializer, FriendshipRequestSerializer

@api_view(['GET'])
def meinfo(request):
    user = request.user
    return JsonResponse({
        'id': user.id,
        'name': user.name,
        'email': user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=False)

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