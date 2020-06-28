from django.db import models

class update_info(models.Model):
    version = models.IntegerField()
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    data = models.FileField(upload_to='BinFiles/', default=0)

    def __str__(self):
        return str(self.name) + " " + str(self.version) + " " + str(self.file)
