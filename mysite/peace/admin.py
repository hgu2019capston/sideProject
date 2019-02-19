from django.contrib import admin
from .models import Applicant
from django.contrib import messages


class ApplicantAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name','student_number','username','permission','apply_time')
    list_editable = ('permission',)
    list_filter = ('permission',)

    actions = ['set_permission']

    def set_permission(self, request, queryset):
        for applicant in queryset:
            Applicant.objects.filter(name=applicant.name).update(permission=2)
        messages.success(request, '{0}명의 회원을 인증했습니다.'.format(len(queryset)))


admin.site.register(Applicant, ApplicantAdmin)
