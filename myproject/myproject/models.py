from django.db import models

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Posts'
    
    def __str__(self):
        return f"{self.title}: {self.content}"
    

# Create your models here.
