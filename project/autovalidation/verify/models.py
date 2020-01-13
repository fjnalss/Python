# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Oui(models.Model):
    domain_id = models.SmallIntegerField(primary_key=True)
    domain = models.CharField(max_length=30)
    force_max_age = models.CharField(max_length=255, blank=True, null=True)
    rewrite_url = models.CharField(max_length=255, blank=True, null=True)
    gzip_compressed = models.CharField(max_length=1, blank=True, null=True)
    sam = models.TextField(blank=True, null=True)
    objects = models.Manager() #解决views使用类.objects提示没有该属性

    class Meta:
        managed = False
        db_table = 'oui'


class Result(models.Model):
    u_id = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)
    ok = models.CharField(max_length=1, blank=True, null=True)
    error = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'result'


class Url(models.Model):
    domain = models.CharField(max_length=255)
    uri = models.CharField(max_length=255, blank=True, null=True)
    param = models.CharField(max_length=255, blank=True, null=True)
    status_code = models.CharField(max_length=3, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'url'


class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    passwd = models.CharField(max_length=255, blank=True, null=True)
    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'user'
