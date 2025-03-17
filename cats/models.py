from django.db import models

class Cat(models.Model):
    cat_id = models.CharField(max_length=255, unique=True) # ID кошки с API
    url = models.URLField() # URL изображения
    # Дополнительные поля, если нужно (например, породы)

    def __str__(self):
        return self.cat_id