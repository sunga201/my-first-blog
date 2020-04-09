from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model): #모든 view들은 models.Model을 상속받는다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey : 외래키 설정
    title=models.CharField(max_length=200) #CharField : 글자수가 제한된 필드
    text=models.TextField() # TextField : 글자수에 제한이 없는 필드
    created_date=models.DateTimeField(default=timezone.now) # DateTimeField : 날짜와 시간을 저장하는 필드
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title