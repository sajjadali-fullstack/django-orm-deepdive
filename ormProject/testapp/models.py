from django.db import models

# Create your models here.

class Prisoner(models.Model):
    """Core details of the Prisoner (Personal & Case Info)"""
    STATUS_CHOICES = [
        ('under_trial', 'Under Trial'),
        ('convicted', 'Convicted'),
        ('released', 'Released'),
    ]
    
    prisoner_id = models.CharField(max_length=20, unique=True) # Unique ID (e.g., Prisoner No.)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    
    # Physical Identification
    identification_mark = models.TextField(blank=True, null=True) 
    photo = models.ImageField(upload_to='prisoners_photos/', blank=True, null=True)
    
    # Detention Details
    crimes = models.CharField() # A prisoner can commit multiple crimes
    arrest_date = models.DateField()
    phone_number = models.CharField(max_length=10) # Barrack or Cell identification
    fingerprint = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='under_trial')
    
    # Relationships
    arresting_officer = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.prisoner_id} - {self.first_name} {self.last_name}"
