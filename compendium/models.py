from django.db import models
from utils.image import image_resize

# Create your models here.
class Races(models.Model):
    image = models.ImageField(upload_to='races_pics/', blank=True, null=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    traits = models.TextField()
    #sorting
    class Meta:
        ordering = ['name']
        verbose_name = 'race'
        verbose_name_plural = 'races'
        db_table = 'races'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_resize(self.image.path)

    def __str__(self):
        return self.name

class Spells(models.Model):
    name = models.CharField(max_length=300)
    level = models.IntegerField()
    description = models.TextField()
    class Meta:
        ordering = ['level','name']
        verbose_name = 'spell'
        verbose_name_plural = 'spells'
        db_table = 'spells'

    def __str__(self):
        return f"level {self.level} - {self.name}"

class Monsters(models.Model):
    image = models.ImageField(upload_to='monsters_pics/', blank=True, null=True)
    name = models.CharField(max_length=300)
    danger = models.IntegerField()
    armor_class = models.IntegerField()
    description = models.TextField()
    class Meta:
        ordering = ['name']
        verbose_name = 'monster'
        verbose_name_plural = 'monsters'
        db_table = 'monsters'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_resize(self.image.path)

    def __str__(self):
        return self.name

class CharactersClass(models.Model):
    name = models.CharField(max_length=300)
    spells = models.ManyToManyField(Spells)
    description = models.TextField()
    class Meta:
        ordering = ['name']
        verbose_name = 'character class'
        verbose_name_plural = 'characters classes'
        db_table = 'characters_classes'

    def __str__(self):
        return self.name