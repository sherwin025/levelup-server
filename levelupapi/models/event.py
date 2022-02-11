from pydoc import describe
from tkinter import CASCADE
from django.db import models

class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField("Gamer", through="EventGamer", related_name="attending")
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
        
    @property
    def attendees_count(self):
        return self.__attendees_count

    @attendees_count.setter
    def attendees_count(self, value):
        self.__attendees_count = value