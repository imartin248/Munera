from django.urls import path
from . import views

app_name = 'giftlist'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/deletegift/', views.deleteGift, name='deletegift'),
    path('groupresults/', views.groupResults, name='groupresults'),
    path('<int:id>/sendrequest/', views.send_group_request, name='send_group_request'),
    path('<int:new_member_id>/<int:requested_group_id>/<int:group_request_id>/acceptrequest/', views.accept_group_request, name='accept_group_request'),
    path('grouprequests/', views.groupRequests, name='grouprequests'),
    path('creategroup', views.createGroup, name='creategroup'),
    path('<group>/grouplist/', views.groupLlist, name='grouplist'),
    path('memberlist/<User>', views.memberGiftList, name='membergiftlist'),
    path('addshoppinglist/<member>/<int:gift>', views.add_gift_to_shoppinglist, name='addshoppinglist'),
    path('<int:id>/<group>/deleteshoppinglist/', views.delete_gift_from_shoppinglist, name='deleteshoppinglist'),
]
