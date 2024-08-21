from django.contrib import admin


from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile,ProfileAdmin)

""" def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames' """