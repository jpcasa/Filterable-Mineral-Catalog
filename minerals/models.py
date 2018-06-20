from django.db import models

# Create your models here.
class Mineral(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_filename = models.CharField(max_length=535)
    image_caption = models.CharField(max_length=535)
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    strunz_classification = models.CharField(max_length=255, default='')
    color = models.CharField(max_length=255, default='')
    crystal_system = models.CharField(max_length=255, default='')
    unit_cell = models.CharField(max_length=535, default='')
    crystal_symmetry = models.CharField(max_length=255, default='')
    cleavage = models.CharField(max_length=255, default='')
    mohs_scale_hardness = models.CharField(max_length=255, default='')
    luster = models.CharField(max_length=255, default='')
    streak = models.CharField(max_length=255, default='')
    diaphaneity = models.CharField(max_length=255, default='')
    optical_properties = models.CharField(max_length=255, default='')
    group = models.CharField(max_length=255, default='')
    refractive_index = models.CharField(max_length=535, default='')
    crystal_habit = models.CharField(max_length=535, default='')
    specific_gravity = models.CharField(max_length=535, default='')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', 'name',]

    def __str__(self):
        return self.name
