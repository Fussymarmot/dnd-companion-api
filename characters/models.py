from django.db import models
import uuid
from utils.image import image_resize
from users.models import User
from compendium.models import Races, CharactersClass, Spells

# Create your models here.
class Characters(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')

    image = models.ImageField(default='default_character.jpg', upload_to='characters_pics')
    name = models.CharField(max_length=300)
    race = models.ForeignKey(Races, on_delete=models.CASCADE, related_name='characters')
    character_class = models.ForeignKey(CharactersClass, on_delete=models.CASCADE, related_name='characters')

    world_view = models.TextField()
    health = models.IntegerField()
    weapon = models.CharField(max_length=150)
    armor = models.CharField(max_length=150)
    protection = models.IntegerField()

    backstory = models.TextField()
    spells = models.ManyToManyField(Spells, related_name='characters')
    inventory = models.TextField(blank=True)

    charisma = models.IntegerField()
    dexterity = models.IntegerField()
    bodytype = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    power = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_resize(self.image.path)

    def __str__(self):
        return self.name

