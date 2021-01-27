from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='media/', default='/media/default.jpg')
    email_id = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False)
    room_no = models.CharField(max_length=5)
    subject = models.TextField()

    class Meta:
        managed = True
        db_table = 'teacher'
