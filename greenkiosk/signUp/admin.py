from django.contrib import admin

# Register your models here.
from .models import Sign_in
class SignUp_admin(admin.ModelAdmin):
    list_display=("Email_address","Phone_number","Password","Password_comfirmation")
 
admin.site.register(Sign_in, SignUp_admin)
