from django.urls import re_path, path, include
from rest_framework import routers
from .views import AdminPollsViewSet, AdminQuestionViewSet, UserPollsViewSet, get_poll_questions, handle_poll_question, get_user_answers

adminRouter = routers.DefaultRouter()

adminRouter.register(r'polls', AdminPollsViewSet)
adminRouter.register(r'questions', AdminQuestionViewSet)

userRouter = routers.DefaultRouter()
userRouter.register(r'polls', UserPollsViewSet)

urlpatterns = [
    re_path('admin/', include(adminRouter.urls)),
    re_path('user/', include(userRouter.urls)),
    path('user/polls/<int:poll_id>/questions', get_poll_questions),
    path('user/polls/<int:poll_id>/questions/<int:question_id>/', handle_poll_question),
    path('user/polls/answers/<int:user_id>', get_user_answers),
]
