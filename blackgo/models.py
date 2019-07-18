from django.db import models


class BlackgoCafe(models.Model):
    cafe_name = models.CharField(max_length=100)
    cafe_url = models.URLField('Cafe URL')
    cafe_description = models.CharField(max_length=200)

    def __str__(self):
        return "이름 : " + self.cafe_name + ", 주소 : " + self.cafe_url


class BlackgoUnivEntrance(models.Model):
    univ_name = models.CharField(max_length=100)
    univ_entrance_type = models.CharField(max_length=100)
    univ_entrance_name = models.CharField(max_length=100)
    univ_url = models.URLField('University URL')

    def __str__(self):
        return "학교명 : " + self.univ_name


class BlackgoOnlineAcademy(models.Model):
    site_name = models.CharField(max_length=100)
    site_description = models.CharField(max_length=200)
    site_url = models.URLField()
    offline_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return "사이트명 : " + self.site_name
