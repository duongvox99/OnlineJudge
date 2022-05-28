from django.urls import path

from ..views.oj import (
    ContestAccessAPI, ContestAnnouncementListAPI, ContestAPI, ContestListAPI,
    ContestPasswordVerifyAPI, ContestRankAPI
)

urlpatterns = [
    path("contests/", ContestListAPI.as_view(), name="contest_list_api"),
    path("contest/", ContestAPI.as_view(), name="contest_api"),
    path("contest/password/", ContestPasswordVerifyAPI.as_view(), name="contest_password_api"),
    path("contest/announcement/", ContestAnnouncementListAPI.as_view(), name="contest_announcement_api"),
    path("contest/access/", ContestAccessAPI.as_view(), name="contest_access_api"),
    path("contest_rank/", ContestRankAPI.as_view(), name="contest_rank_api"),
]
