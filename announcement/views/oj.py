from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer
from utils.api import APIView


class AnnouncementAPI(APIView):
    def get(self, request):
        announcements = Announcement.objects.filter(visible=True)
        return self.success(self.paginate_data(request, announcements, AnnouncementSerializer))
