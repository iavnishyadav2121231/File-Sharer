from django.contrib import admin


from file_share.models import user_file_data, share_file_data

admin.site.register(user_file_data)
admin.site.register(share_file_data)