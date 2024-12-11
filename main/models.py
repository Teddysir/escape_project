from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="이미지")
    author = models.CharField(max_length=50, verbose_name="작성자")  # 사용자 이름을 직접 입력
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.title
