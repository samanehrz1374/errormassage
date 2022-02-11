# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VolDatabase(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    total_volumerls = models.IntegerField(db_column='total_volumeRls', blank=True, null=True)  # Field name made lowercase.
    total_volumeusdt = models.IntegerField(db_column='total_volumeUsdt', blank=True, null=True)  # Field name made lowercase.
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at_int_timestamp = models.IntegerField(blank=True, null=True)
    created_at_int_datetime = models.IntegerField(blank=True, null=True)
    created_at_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vol_database'
