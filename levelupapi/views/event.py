from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer

class EventView(ViewSet):
    def retrieve(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        events = Event.objects.all()
        event_game = request.query_params.get('game', None)
        if event_game is not None:
            events = events.filter(game_id=event_game) 
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        organizer_id = Gamer.objects.get(user=request.auth.user)
        
        try:
            serializer = CreateEventSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(organizer=organizer_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "game", "description", "date", "time", "organizer")
        depth = 2
        
class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "description", "date", "time", "game" )