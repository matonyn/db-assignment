from django.contrib import admin
from .models import Users, Publicservant, Patients, Doctor, Specialize, Record, Patientdisease, Disease, Diseasetype

admin.site.register(Users)
admin.site.register(Publicservant)
admin.site.register(Patients)
admin.site.register(Doctor)
admin.site.register(Specialize)
admin.site.register(Record)
admin.site.register(Patientdisease)
admin.site.register(Disease)
admin.site.register(Diseasetype)

