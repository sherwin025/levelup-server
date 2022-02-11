from tkinter import CASCADE
from django.db import models

class Game(models.Model):
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    maker = models.CharField(max_length=250)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    num_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    
    @property
    def event_count(self):
        return self.__event_count

    @event_count.setter
    def event_count(self, value):
        self.__event_count = value
        
    @property
    def user_event_count(self):
        return self.__user_event_count

    @user_event_count.setter
    def user_event_count(self, value):
        self.__user_event_count = value