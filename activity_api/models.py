from django.db import models


class Member(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = models.CharField(max_length=60)


class MemberActivity(models.Model):
    member = models.ForeignKey(Member, related_name='member_activity', on_delete=models.CASCADE, null=True)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
