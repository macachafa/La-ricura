from django.db import models 


class Categoria(models.Model):
  id = models.AutoField(primary_key=True)
  categoria = models.CharField('categoria', max_length = 50)