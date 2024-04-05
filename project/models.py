from django.db import models
from user.models import User

# Create your models here.
techChoices = (
("Python","Python"),
("Java","Java"),
("C++","C++"),
("C#","C#"),
)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=techChoices)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.name    

class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)        
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "projectteam"
    
    def __str__(self):
        return self.user.username    
    

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "country"
        
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    
    class Meta:
        db_table = "city"
        
    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    bookImage = models.ImageField(upload_to="uploads/")
    
    
    
    class Meta:
        db_table = "books"
    
    def __str__(self):
        return self.name
    
    
taskPriority = (
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low"),
)    
taskSatatus = (
    ("Not Started","Not Started"),
    ("In Progress","In Progress"),
    ("Completed","Completed"),
)
class Task(models.Model):
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=100,choices=taskPriority)
    status = models.CharField(max_length=100,choices=taskSatatus)
    hours = models.PositiveIntegerField()
    is_assigned = models.BooleanField(default=False)
    
    class Meta:
        db_table = "task"
    
    def __str__(self):
        return self.title    
    

#class name must starts with cap
class user_task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    class Meta:
        db_table = "user_task"
    
    def __str__(self):
        return self.task.title +" - "+self.user.username     

