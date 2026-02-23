from django.db import models

# Create your models here.
class Races(models.Model):
    image = models.ImageField(upload_to='races_pics/', blank=True, null=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    traits = models.TextField()
    #sorting
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Spells(models.Model):
    name = models.CharField(max_length=300)
    level = models.IntegerField()
    description = models.TextField()
    class Meta:
        ordering = ['level','name']

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
    def __str__(self):
        return self.name

class CharactersClass(models.Model):
    name = models.CharField(max_length=300)
    spells = models.ManyToManyField(Spells)
    description = models.TextField()