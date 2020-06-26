from django.db import models

class Covid(models.Model) :
    date = models.DateField(null=False)# 날짜
    SouthKorea = models.FloatField(null=False)
    US = models.FloatField(null=False)
    UnitedKingdom = models.FloatField(null=False)
    Germany = models.FloatField(null=False)
    France = models.FloatField(null=False)

    def __str__(self):
        return self.date

class Passenger(models.Model):  # 승객 모델
    # 성별 상수 정의
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )

    # 승선_항구 상수 정의
    CHERBOURG = 'C'
    QUEENSTOWN = 'Q'
    SOUTHAMPTON = 'S'
    PORT_CHOICES = (
        (CHERBOURG, 'Cherbourg'),
        (QUEENSTOWN, 'Queenstown'),
        (SOUTHAMPTON, 'Southampton'),
    )

    name = models.CharField(max_length=100, blank=True)                 # 이름
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)           # 성별
    survived = models.BooleanField()                                    # 생존_여부
    age = models.FloatField(null=True)                                  # 연령
    ticket_class = models.PositiveSmallIntegerField()                   # 티켓_등급
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)     # 승선_항구

    def __str__(self):
        return self.name
