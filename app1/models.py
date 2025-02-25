from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=25,blank=False,null=False)
    sname=models.CharField(max_length=25,blank=False,null=False)
    kcpe_marks = models.IntegerField(null=True, blank=True)  # New field
    current_grade = models.CharField(max_length=2, null=True, blank=True)  # New field
    adm = models.CharField(max_length=20, unique=True)  # Enforcing uniqueness  
    age=models.IntegerField()
    classs = models.CharField(max_length=25,blank=False,null=False)
    stream =  models.CharField(max_length=25,blank=False,null=False)
    mistake =      models.TextField(default = "")
    mistake_1 =      models.TextField(default = "")
    punshmentgiven = models.TextField(default = "")
    picture = models.ImageField(upload_to='students_pics/', null=True, blank=True)
    third_mistake = models.TextField(null=True, blank=True)  # ✅ Third Mistake
    blackbook = models.BooleanField(default=False)  # ✅ Blackbook
    
    def save(self, *args, **kwargs):
        """ Automatically update blackbook status based on third_mistake """
        if self.third_mistake:
            self.blackbook = True
        else:
            self.blackbook = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.sname} ({self.adm})"