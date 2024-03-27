from django.db import models


class Category(models.Model):
    name = models.CharField('Nom', max_length=100)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Figurine(models.Model):
    name = models.CharField(verbose_name='Nom', max_length=100, help_text='Entrez un nom')
    image = models.ImageField(verbose_name='Image')
    price = models.DecimalField(verbose_name='Prix €', max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name='Description', validators=[])
    recommended_age = models.PositiveIntegerField(verbose_name='Âge recommandé', default=3)
    features = models.CharField(verbose_name='Caractéristiques', max_length=255)
    have_it = models.BooleanField(verbose_name='Je l\'ai', default=False)
    liked = models.PositiveIntegerField(verbose_name='J\'aimes', default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Figurine'
        verbose_name_plural = 'Figurines'

    def __str__(self):
        return self.name
