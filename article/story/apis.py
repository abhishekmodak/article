
from rest_framework import generics
from story.models import Story
from story import serializers as story_serializers


class StoryAPI(generics.ListCreateAPIView):
    """Create and list API of Article
    """
    
    serializer_class = story_serializers.StorySerialiser
    queryset = Story.objects.filter(status=True).order_by('-vote')


class VoteAPI(generics.UpdateAPIView):
    """Vote API
    """

    queryset = Story.objects.filter(status=True)
    serializer_class = story_serializers.VoteSerialiser