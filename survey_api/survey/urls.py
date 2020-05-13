from django.urls import re_path, include
from rest_framework import routers
from .views import AdminPollsViewSet, AdminQuestionViewSet, UserPollsViewSet

adminRouter = routers.DefaultRouter()

adminRouter.register(r'polls', AdminPollsViewSet)
adminRouter.register(r'questions', AdminQuestionViewSet)

userRouter = routers.DefaultRouter()
userRouter.register(r'polls', UserPollsViewSet)

urlpatterns = [
    re_path('admin/', include(adminRouter.urls)),
    re_path('user/', include(userRouter.urls))
]
