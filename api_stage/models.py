from django.db import models


# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=250, blank=False, default='')
    last_name = models.CharField(max_length=250, blank=False, default='')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # gender = models.CharField(max_length=1, blank=False, default='')
    date_birth = models.DateField()
    profession = models.CharField(max_length=250, blank=False, default='')
    phone = models.CharField(max_length=12, blank=False, unique=True, default='')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    password = models.CharField(max_length=250, blank=False, default='')
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #
        #    to set table name in database
        #
        db_table = "users"


class Posts(models.Model):
    mots_recherche = models.CharField(max_length=250, blank=False, default='')
    social_media = models.CharField(max_length=250, blank=False, default='')
    type_document = models.CharField(max_length=250, blank=False, default='')
    comment = models.CharField(max_length=250, blank=False, default='')
    # date_created = models.DateField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #
        #    to set table name in database
        #
        db_table = "posts"


class Files(models.Model):
    type_file = models.CharField(max_length=250, blank=False, default='')
    file_name = models.FileField(max_length=250, blank=False, default='')
    comment = models.CharField(max_length=250, blank=False, default='')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #
        #    to set table name in database
        #
        db_table = "files"


class Comments(models.Model):
    title = models.CharField(max_length=250, blank=False, default='')
    comment = models.CharField(max_length=250, blank=False, default='')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #
        #    to set table name in database
        #
        db_table = "comments"