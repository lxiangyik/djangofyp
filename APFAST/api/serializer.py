from rest_framework.serializers import ModelSerializer
from APFAST.models import Announcement


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
