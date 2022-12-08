from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Institute(models.Model):
    
    INSTITUTE_TYPE = (
        ('Medical Clinic', 'Medical Clinic'),
        ('Dentist Clinic', 'Dentist Clinic'),
        ('Hospital', 'Hospital'),
        ('Lab', 'Lab'),
        ('Test Center', 'Test Center')
    )
    
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Closed', 'Closed')
    )

    name = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=18, null=True)
    email = models.CharField(max_length=250, null=True)
    services = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=500, null=True, choices=INSTITUTE_TYPE)
    status = models.CharField(max_length=100, null=True, choices=STATUS)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

'''class User(models.Model):

    TYPE = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Lab Owner', 'Lab Owner'),
        ('Test Center Head', 'Test Center Head')
    )

    related_institute = models.ForeignKey(Institute, null=True, on_delete=models.SET_NULL)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=18, null=True)
    address = models.CharField(max_length=500, null=True)
    type = models.CharField(max_length=300, null=True,choices=TYPE)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.firstname + self.lastname
'''