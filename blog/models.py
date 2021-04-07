from django.conf import settings
from django.db import models
from django.utils import timezone

# Post : 모델의 이름, 항상 클래스 이름의 첫 글자는 대문자로 써야함 !
# models 는 Post가 장고 모델임을 의미한다. 이 코드 때문에 장고는 Post가 데이터베이스에
# 저장되어야 한다고 알게 된다.

# Post라는 객체를 생성했으며, 
# post는 author, title, text, created_date, published_date라는 멤버 변수와
# publish, __str__이라는 메서드를 갖는다.

# 장고에서는 특정 명령어를 통해 우리가 만든 모델(객체)를 추가해준다.
# 그럼 장고는 모델(객체)를 db에 저장한다 ! -> 장고의 특이한 부분


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
