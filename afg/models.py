from django.db import models

# Create your models here.

class DiaryEntry(models.Model):
    report_key = models.CharField(max_length=255, db_index=True, unique=True)
    date = models.DateTimeField(db_index=True)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255, db_index=True)
    tracking_number = models.CharField(max_length=255, db_index=True)
    title = models.TextField(db_index=True)
    # Will get a tsvector full-text-search index
    summary = models.TextField()
    region = models.CharField(max_length=255, db_index=True)
    attack_on = models.CharField(max_length=255, db_index=True)
    complex_attack = models.BooleanField()
    reporting_unit = models.CharField(max_length=255, db_index=True)
    unit_name = models.CharField(max_length=255, db_index=True)
    type_of_unit = models.CharField(max_length=255, db_index=True)
    friendly_wia = models.IntegerField(db_index=True)
    friendly_kia = models.IntegerField(db_index=True)
    host_nation_wia = models.IntegerField(db_index=True)
    host_nation_kia = models.IntegerField(db_index=True)
    civilian_wia = models.IntegerField(db_index=True)
    civilian_kia = models.IntegerField(db_index=True)
    enemy_wia = models.IntegerField(db_index=True)
    enemy_kia = models.IntegerField(db_index=True)
    enemy_detained = models.IntegerField(db_index=True)
    mgrs = models.CharField(max_length=255, db_index=True)
    latitude = models.CharField(max_length=255, db_index=True)
    longitude = models.CharField(max_length=255, db_index=True)
    originator_group = models.CharField(max_length=255, db_index=True)
    updated_by_group = models.CharField(max_length=255, db_index=True)
    ccir = models.CharField(max_length=255, db_index=True)
    sigact = models.CharField(max_length=255, db_index=True)
    affiliation = models.CharField(max_length=255, db_index=True)
    dcolor = models.CharField(max_length=255, db_index=True)
    classification = models.CharField(max_length=255, db_index=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-civilian_kia', '-civilian_wia', '-host_nation_kia',
                '-host_nation_wia', '-friendly_kia', '-friendly_wia',
                'date', 'title']
        verbose_name_plural = 'Diary entries'

class Phrase(models.Model):
    phrase = models.CharField(max_length=255, unique=True, db_index=True)
    entries = models.ManyToManyField(DiaryEntry)
    # denormalization for performance:
    entry_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.phrase
