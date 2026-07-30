from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
       upload_to='produits/',
       null=True,
       blank=True
)
def __str__(self):
   return self.nom

class Meta:
    ordering = ['-created_at']