from django.contrib import admin
from .models import Applicant
from django.contrib import messages
from .change  import adduser, deluser


class ApplicantAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name','student_number','username','permission','apply_time')
	list_editable = ('permission',)
	list_filter = ('permission',)

	actions = ['set_permission', 'delete']


	def set_permission(self, request, queryset):
		for applicant in queryset:
			adduser(applicant.username, applicant.pwd)
			Applicant.objects.filter(name=applicant.name).update(permission=2)

		messages.success(request, '{0}명의 회원을 인증했습니다.'.format(len(queryset)))
                
	def save_model(self, request, obj, form, change):
		if(obj.permission == 2):
			adduser(obj.username, obj.pwd)
		obj.save()


	def delete(self, request, queryset):
		for applicant in queryset:
			deluser(applicant.username)
			Applicant.objects.filter(name=applicant.name).delete()
		messages.success(request, '{0}명의 회원을 삭제했습니다.'.format(len(queryset)))


admin.site.disable_action('delete_selected')
admin.site.register(Applicant, ApplicantAdmin)
