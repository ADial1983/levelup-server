from django.db import models


class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='type_of_game')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
