from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Rating(models.Model):
    rating1 = models.IntegerField("Rating1",default=0)
    rating2 = models.IntegerField("Rating2",default=0)
    rating3 = models.IntegerField("Rating3",default=0)
    rating4 = models.IntegerField("Rating4",default=0)
    rating5 = models.IntegerField("Rating5",default=0)
    
    def overall_ratinge(self):
        overall_ratings = (self.rating1 + self.rating2 + self.rating3 + self.rating4 + self.rating5) / 5
        return overall_ratings

    def __str__(self):
        overall_rating = self.overall_ratinge()
        return str(overall_rating)

class Ideas(models.Model):

    title = models.CharField("Название идей", max_length=255)
    description = models.TextField("Описание идей")
    author = models.ForeignKey(User,verbose_name="Автор", related_name="ideas",on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating,on_delete=models.CASCADE,related_name="ideas",blank=True,null=True,default=None)

    def __str__(self):
        return self.title

class Photo(models.Model):
    photo = models.ImageField("photo", upload_to="Images/")
    ideas = models.ForeignKey(Ideas, related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return self.ideas.title

