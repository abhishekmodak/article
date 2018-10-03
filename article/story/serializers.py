from rest_framework import serializers 
from story.models import Story

class StorySerialiser(serializers.ModelSerializer):
    """Create and list Serialiser of Article
    """

    vote = serializers.IntegerField(read_only=True)
    class Meta:
        model = Story
        fields = (
                    'id', 'title', 'content', 'author', 'vote'
                )

class VoteSerialiser(serializers.ModelSerializer):
    """Voting serialiser for Article
    """

    class Meta:
        model = Story
        exclude=(
                    'title', 'content', 'author', 'vote', 'status'
                )

    def update(self, instance, validated_data):
        instance.upvote()
        return instance