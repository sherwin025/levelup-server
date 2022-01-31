from tkinter import CASCADE
from django.db import models

class Game(models.Model):
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    maker = models.CharField(max_length=250)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    num_of_players = models.IntegerField()
    skill_level = models.IntegerField()