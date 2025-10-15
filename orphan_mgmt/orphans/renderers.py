# Custom DRF Browser Titles
from django.conf import settings
from rest_framework.renderers import BrowsableAPIRenderer

class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    template = 'rest_framework/api.html'
    def get_context(self, data, accepted_media_type, renderer_context):
        context = super().get_context(data, accepted_media_type, renderer_context)
        context['api_title'] = "🌍 Orphan Management System API"
        context['api_description'] = "Manage orphans, courses, enrollments, and goals with Django REST Framework."
        context['api_version'] = "v1.0"
        return context
