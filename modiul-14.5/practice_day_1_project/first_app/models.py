from django.db import models
from django.core import validators

# Create your models here.
class MyModel(models.Model):
    roll=models.AutoField(primary_key=True)
    # big_auto=models.BigAutoField()
    name=models.CharField(max_length=100)
    fathername=models.TextField()
    address=models.TextField()
    big_int=models.BigIntegerField()
    binary_field=models.BinaryField()
    check_field=models.BooleanField()
    # comma_separated=models.CharField(validators=['comma_separated_validator'], max_length=100)
    date=models.DateField()
    date_time=models.DateTimeField()
    # decimal_field=models.DecimalField()
    duration=models.DurationField()
    email=models.EmailField()
    # file=models.FileField(upload_to='files/')
    # path=models.FilePathField(path='/path/to/file')
    float=models.FloatField()
    # foriegn_key=models.ForeignKey('otherModel',on_delete=models.CASCADE)
    ip_addr=models.GenericIPAddressField()
    img=models.ImageField()
    int=models.IntegerField()
    json_field=models.JSONField()
    # many_to_many=models.ManyToManyField('otherModel')
    # null_bool=models.models.models.NullBooleanField()
    # one_to_one=models.OneToOneField('otherModel',on_delete=models.CASCADE)
    positive_int=models.PositiveIntegerField()
    positive_small=models.PositiveSmallIntegerField()
    slug_field=models.SlugField()
    small_int=models.SmallIntegerField()
    text=models.TextField(blank=True,null=True)
    time=models.TimeField()
    url=models.URLField()
    uuid=models.UUIDField()



