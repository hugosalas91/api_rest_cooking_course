from django.conf.urls import url, include
from course import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Cooking Courses API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cooking-courses', views.CookingCourseViewSet)
router.register(r'pupils', views.PupilViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url('^schema/$', schema_view), 
    url(r'^', include(router.urls)), 
    url(r'^register/$', views.CreateChefView.as_view(), name='chef'), 
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]