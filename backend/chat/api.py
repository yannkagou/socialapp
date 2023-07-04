from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Conversation, ConversationMessage
from .serializers import ConversationSerializer, ConversationMessageSerializer, ConversationDetailSerializer
from account.models import User
from account.serializers import UserSerializer

@api_view(['GET'])
def conversation_list(request):
    conversations = Conversation.objects.filter(users__in=list([request.user.id]))
    
    serializers = ConversationSerializer(conversations, many=True)
    
    return JsonResponse(serializers.data, safe=False) 