from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.

# User.__setattr__{'email':unique=True}

def validatePositive(value):
    if value < 1:
        raise ValidationError(
            _('Invalid number')
        )



class phone(models.Model):
    # gb = 'GB'
    # mb =' MB'
    
    PhoneId = models.AutoField(primary_key = True)
    Brand = models.CharField(max_length=50,default='')
    Price = models.IntegerField(validators=[validatePositive])
    In_the_box = models.CharField(max_length=400,default='Handset,Charger,Battery,User Manual')
    Model_name = models.CharField(max_length=60,default='')
    Model_number = models.CharField(max_length=60,default='')
    Color = models.CharField(max_length=50,default='')
    Quantity = models.IntegerField(default=1,validators=[validatePositive])
    categoryList = [('basic','Basic phone'),('smart','Smart phone')]
    Category = models.CharField(choices=categoryList,default='basic',max_length=12)
    Date = models.DateTimeField(default=timezone.now)
    Sim_type = models.CharField(max_length=50,default='Dual Sim')
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    Display_size = models.CharField(default='',max_length=60)
    Resolution = models.CharField(max_length=30,default='')
    
    Front_image = models.ImageField(upload_to='mobsms/images',default='')
    Back_image = models.ImageField(upload_to='mobsms/images',default='')
    Other_image = models.ImageField(upload_to='mobsms/images',default='',blank=True)
    Other_image2 = models.ImageField(upload_to='mobsms/images',default='',blank=True)
    @property
    def fullName(self):
        return f"{self.Brand} {self.Model_name}"
    def __str__(self):
        return f"{self.Brand} {self.Model_name} ({self.Color})"
    
class basic(phone):
    Internal_storage = models.IntegerField(validators=[validatePositive])
    Ram = models.IntegerField(blank=True,null=True,validators=[validatePositive])
    Expandable_storage = models.SmallIntegerField(blank=True,null=True,validators=[validatePositive])
    Supported_memorycard_type = models.CharField(default='',blank=True,max_length=30)
    Memorycard_slot_type = models.CharField(max_length=30,default='Dedicated Slot',null=True)
    Primary_camera = models.CharField(default='',null=True,max_length=30,blank=True)
    Supported_networks = models.CharField(max_length=120,default='GSM')
    Sim_size = models.CharField(max_length=50,default='Normal SIM')
    Keypad_type = models.CharField(default='', max_length=50,blank=True)
    Battery_capacity = models.IntegerField(validators=[validatePositive])
    Bluetooth  = models.BooleanField(default=True)
    Audiojack = models.BooleanField(default=True)
    Nonremovable_battery = models.BooleanField(default=True)

class smart(phone):

    Resolution_type = models.CharField(max_length=10,default='HD')
    Gpu = models.CharField(max_length=50,default='',blank=True)
    Other_display_features = models.TextField(default='')
    Operating_system = models.CharField(max_length=30,default='')
    Processor_type = models.CharField(max_length=40,default='')
    Processor_core = models.CharField(max_length=30,default='')
    Primary_clock_speed = models.FloatField()
    Secondary_clock_speed = models.FloatField(blank=True,null=True)
    Internal_storage = models.IntegerField(validators=[validatePositive])
    Ram = models.IntegerField(validators=[validatePositive])
    Expandable_storage = models.SmallIntegerField(blank=True,null=True,validators=[validatePositive])
    Supported_memorycard_type = models.CharField(default='',blank=True,max_length=30)
    Memorycard_slot_type = models.CharField(max_length=30,default='Dedicated Slot',blank=True)
    Primary_camera = models.CharField(max_length=80,default='')
    Primary_camera_features = models.TextField(max_length=1500,default='')
    Secondary_camera = models.CharField(max_length=60,default='',blank=True)
    Secondary_camera_features = models.TextField(max_length=1500,default='',blank=True)
    Flash = models.CharField(max_length=40,default='')
    Dual_camera_lens = models.CharField(max_length=60,default='',blank=True)
    Supported_networks = models.CharField(max_length=90,default='WCDMA, GSM')
    Internet_connectivity = models.CharField(max_length=60,default='')
    Bluetooth_version = models.FloatField(default=4.0,blank=True,null=True)
    Touchscreen_type = models.CharField(max_length=60,default='Multi-touch',blank=True)
    Sim_size = models.CharField(max_length=50,default='Dual Nano SIM')
    User_interface = models.CharField(max_length=60,default='',blank=True)
    Sensors = models.CharField(max_length=500,default='',blank=True)
    Other_features = models.TextField(default='')
    Battery_capacity = models.IntegerField(validators=[validatePositive])
    Battery_type = models.CharField(max_length=60,default='',blank=True)
    Weight = models.IntegerField(blank=True,null=True,validators=[validatePositive])
    Bluetooth  = models.BooleanField(default=True)
    Audiojack = models.BooleanField(default=True)
    Nonremovable_battery = models.BooleanField(default=True)
    Otg_compatible = models.BooleanField(default=True)



def validatePhone(value):
    try:
        int(value)
    except:
        raise ValidationError(_('invalid phone no.'))
    if len(value) < 10:
        raise ValidationError(
            _('phone noumber is less then 10 digits.')
        )


def validateDate(value):
    # print(type(value))
    year = int((value.strftime("%Y")))
    if year >=2000:
        raise ValidationError(_('invalid birth year'))


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phone = models.CharField(default='',max_length=12,validators=[validatePhone])
    DOB = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True,validators=[validateDate])
    image = models.ImageField(upload_to='profile_pic',default='profile_pic/default.png')

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 400 or img.height > 400:
            img.thumbnail((400,400))
            img.save(self.image.path)


    def __str__(self):
        return f"{self.user.username} Profile"


def validatePrice(value):
    if value == 0:
        raise ValidationError()



class checkout(models.Model):
    full_name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    phone_no = models.CharField(max_length=15,validators=[validatePhone])
    cart = models.TextField(blank=False )
    date = models.DateField(auto_now=False, auto_now_add=False,default=timezone.now)
    total_price = models.IntegerField(blank=False,validators=[validatePrice])

    def __str__(self):
        return f"{self.full_name} checkout"
