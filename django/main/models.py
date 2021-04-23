from django.db import models

# Create your models here.

class Chicken(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Ilsik(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Bunsik(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Yasik(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Jokbal(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Jungsik(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Jimtang(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Cafe(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Fastfood(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Hansik(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()

class Etc(models.Model):
    # 업종명
    category = models.CharField(max_length=10)
    # 광역시도명
    area_name = models.CharField(max_length=20)
    # 시간대별 시간
    time = models.DateTimeField()
    # 배달 주문건수
    predict = models.BigIntegerField()