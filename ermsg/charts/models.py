from django.db import models


# Create your models here.
class mychart(models.Model):
    name=models.CharField(max_length=50)
    rank=models.IntegerField()

# class timestamp(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     # class Meta:
#     #      abstract = True

class VolDatabase(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True)  # Field renamed because it started with '_'.
    total_volumerls = models.IntegerField(db_column='total_volumeRls', blank=True, null=True)  # Field name made lowercase.
    total_volumeusdt = models.IntegerField(db_column='total_volumeUsdt', blank=True, null=True)  # Field name made lowercase.
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at_int_timestamp = models.IntegerField(blank=True, null=True)
    created_at_int_datetime = models.IntegerField(blank=True, null=True)
    created_at_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vol_database'
