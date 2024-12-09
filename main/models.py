from django.db import models


# 활동 모델 (랜덤 활동 추천용)
class Activity(models.Model):
    name = models.CharField(max_length=100)  # 활동 이름
    description = models.TextField()  # 활동 설명
    difficulty = models.CharField(
        max_length=10,
        choices=[('easy', '쉬움'), ('medium', '보통'), ('hard', '어려움')],
        default='medium',
    )  # 난이도
    location = models.CharField(
        max_length=10,
        choices=[('indoor', '실내'), ('outdoor', '실외')],
        default='indoor',
    )  # 활동 장소

    def __str__(self):
        return self.name


# 활동 인증 게시판 모델
class ActivityCertification(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # 활동 정보
    title = models.CharField(max_length=100)  # 인증 게시물 제목
    content = models.TextField()  # 게시물 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return self.title


# 활동 평가 모델
class ActivityReview(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # 활동 정보
    rating = models.PositiveIntegerField()  # 평가 점수 (1~5)
    review = models.TextField()  # 평가 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간

    def __str__(self):
        return f'{self.activity.name} - {self.rating}점'


# 인증샷 갤러리 모델
class CertificationGallery(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # 활동 정보
    image = models.ImageField(upload_to='certifications/')  # 이미지 파일
    caption = models.CharField(max_length=255, blank=True)  # 이미지 설명
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 업로드 시간

    def __str__(self):
        return f'{self.activity.name} - 인증샷'
    
    
    
    
#### 여기서부터 사용할 모델 추가

class KeyStatus(models.Model):
    user_id = models.CharField(max_length=255, unique=True)  # 고유한 익명 사용자 식별자
    has_key = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} - {'Has Key' if self.has_key else 'No Key'}"