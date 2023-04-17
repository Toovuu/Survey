from django.urls import path


from .views import (
    SurveyListView,
    SurveyDetailView,
    ThankYouView,
    EditSurveyView,
    DeleteSurveyView,
    CreateSurveyView,
)

app_name = "survey"

urlpatterns = [
    path("new/", CreateSurveyView.as_view(), name="new"),
    path("<int:pk>/", SurveyDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", EditSurveyView.as_view(), name="edit"),
    path("<int:pk>/delete", DeleteSurveyView.as_view(), name="delete"),
    path("thank-you/", ThankYouView.as_view(), name="thank_you"),
    path("", SurveyListView.as_view(), name="home"),
]
