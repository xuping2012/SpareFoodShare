# payments/admin.py
from django.contrib import admin

# Register your models here.


from django.contrib import admin

from payments.models import *




class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "tel_number",
        "gender",
        "type",
        "balance",
        "nickname",
        "status",
        "version",
        "create_time",
        "modify_time",
    )


admin.site.register(Profile, ProfileAdmin)


admin.site.register(Admin)
admin.site.register(Food)
admin.site.register(Interests)
admin.site.register(User)

sql2 = "INSERT INTO `order` (`Food_ID`, `User_ID`, `Order_Type`, `Order_quantity`, `Order_Amount`) " \
          "VALUES (%s,%s,%s,%s,%s)"