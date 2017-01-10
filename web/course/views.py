from course.models import CookingCourse, Pupil
from course.serializers import CookingCourseSerializer, ChefSerializer, PupilSerializer
from django.contrib.auth import get_user_model
from course.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.generics import CreateAPIView
    
    
class CookingCourseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = CookingCourse.objects.all()
    serializer_class = CookingCourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)
    

class CreateChefView(CreateAPIView):
    """
    CreateAPIView provide only POST Method
    """
    model = get_user_model()
    #set Permission as AllowAny user to Register
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChefSerializer
    

class PupilViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
        