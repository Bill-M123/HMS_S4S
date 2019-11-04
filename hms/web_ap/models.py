from django.db import models

# Create your models here.
class Participant(models.Model):
    """Model representing a book genre."""
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, help_text='Enter participant first name.',null=True)
    last_name = models.CharField(max_length=20, help_text='Enter participant last name.',null=True)
    siblings = models.CharField(max_length=20,help_text='Participant has siblings.',null=True)
    environmental_exposures = models.CharField(max_length=20,help_text='Genetic Mutations',null=True)
    genetic_mutations = models.CharField(max_length=20,help_text='Genetic Mutations',null=True)

    class Meta:
        ordering = ['last_name']
