#Query to return all the Institutes
from med_app import institutions
from institutions import Institute

institutes = Institute.objects.all()