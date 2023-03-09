from django.db import models


class EventAtendee(models.Model):

    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name='event_for_atendee')
    atendee = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='atendee_for_event')
