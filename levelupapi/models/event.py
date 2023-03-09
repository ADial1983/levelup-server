from django.db import models


class Event(models.Model):

    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='host_of_event')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='game_at_event')
    date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
