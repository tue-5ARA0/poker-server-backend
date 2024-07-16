from django.contrib import admin

from pages.models import Announcement

@admin.register(Announcement)
class AnnouncementAdminModelView(admin.ModelAdmin):
    list_display = ('created_at', 'is_hidden', 'title', 'message')
    list_filter  = ('is_hidden', )
    readonly_fields = ('created_at', )