from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.






class ICategory(models.Model):

    name = models.CharField('Имя категорий', max_length=255)
    ficon = models.CharField('Для иконки',max_length=255)
    photo = models.ImageField('Фото категорий',blank=True,null=True,upload_to="IcatP/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"

class Ideas(models.Model):
    title = models.CharField("Название идей", max_length=255)
    description = models.TextField("Описание идей")
    created_at = models.DateTimeField('Создано',default=timezone.now)
    author = models.ForeignKey(User,verbose_name="Автор", related_name="ideas",on_delete=models.CASCADE)
    category = models.ForeignKey(ICategory,on_delete=models.CASCADE,blank=True,null=True,default=None,related_name="idea")

    def __str__(self):
        return self.title

    def getall(self):


        idea_id = self.id
        rating = Rating.objects.filter(idea_id=idea_id)
        # try:
        #     rating = Rating.objects.get(user_id=id,idea_id=idea_id)
        # except DoesNotExist:
        #     rating = "Вы уже лайкали"

        return rating
        
   

    def mainRating(self):
        count = 1
        counti = 0
        for rating in self.rating.all():
            count += rating.overall_ratinge()
            counti += 1

        result = int(count/counti)
        return result


    def time(self):
        lastime =timezone.now() - self.created_at
        data = int(lastime.total_seconds())
        totaldata = data / 60
        return int(totaldata)

    class Meta:
        verbose_name = "Идея"
        verbose_name_plural = "Идей"

class Rating(models.Model):
    rating1 = models.IntegerField("Rating1",default=0)
    rating2 = models.IntegerField("Rating2",default=0)
    rating3 = models.IntegerField("Rating3",default=0)
    rating4 = models.IntegerField("Rating4",default=0)
    rating5 = models.IntegerField("Rating5",default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None,related_name="rating")
    idea = models.ForeignKey(Ideas,on_delete=models.CASCADE,blank=True,null=True,default=None,related_name="rating")
    
    
    def getRateBoll(request,self):
        if self.user == request.user:
            return "yes"
        else:
            return "no"
        
          

    def overall_ratinge(self):
        overall_ratings = (self.rating1 + self.rating2 + self.rating3 + self.rating4 + self.rating5) / 5
        return int(overall_ratings)


    def __str__(self):
        overall_rating = self.overall_ratinge()
        return str(overall_rating)

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Photo(models.Model):
    photo = models.ImageField("photo", upload_to="Images/")
    ideas = models.ForeignKey(Ideas, related_name="photo", on_delete=models.CASCADE)

    def __str__(self):
        return self.ideas.title

    

    class Meta:
        verbose_name = "Фото для Идей"
        verbose_name_plural = "Фото для Идей"

