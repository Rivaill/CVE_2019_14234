# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from django.db import models

class PostgreSQLModel(models.Model):
    class Meta:
        abstract = True
        required_db_vendor = 'postgresql'

class User(PostgreSQLModel):
    id = models.AutoField(primary_key=True)
    info = JSONField(blank=True, null=True)
