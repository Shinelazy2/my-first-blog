from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    
    # 다른 모델에 대한 링크 (ForeignKey)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 글자수가 제한됝 텍스트 정의
    title = models.CharField(max_length=200)
    
    # 글자 수에 제한이 없는 긴 텍스트
    text = models.TextField()
    
    # 날짜와 시간
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title