from django.urls import reverse, resolve
from mixer.backend.django import mixer
from django.contrib.auth.models import User
import pytest



class TestUrls:
    def test_home_url(self):
        path = reverse('giftlist:home')
        assert resolve(path).view_name == 'giftlist:home'

    def test_deletegift_url(self):
        path = reverse('giftlist:deletegift', kwargs={'id':1})
        assert resolve(path).view_name == 'giftlist:deletegift'

    def test_groupresults_url(self):
        path = reverse('giftlist:groupresults')
        assert resolve(path).view_name == 'giftlist:groupresults'

    def test_send_group_request_url(self):
        path = reverse('giftlist:send_group_request', kwargs={'id':1})
        assert resolve(path).view_name == 'giftlist:send_group_request'

    def test_accept_group_request_url(self):
        path = reverse('giftlist:accept_group_request', kwargs={'new_member_id':1, 'requested_group_id':1, 'group_request_id':1})
        assert resolve(path).view_name == 'giftlist:accept_group_request'

    def test_grouprequests_url(self):
        path = reverse('giftlist:grouprequests')
        assert resolve(path).view_name == 'giftlist:grouprequests'

    def test_creategroup_url(self):
        path = reverse('giftlist:creategroup')
        assert resolve(path).view_name == 'giftlist:creategroup'

    def test_grouplist_url(self):
        path = reverse('giftlist:grouplist', kwargs={'group':'family'})
        assert resolve(path).view_name == 'giftlist:grouplist'

    @pytest.mark.django_db
    def test_membergiftlist_url(self):
        user = mixer.blend(User, username="dan")
        path = reverse('giftlist:membergiftlist', kwargs={'User':user})
        assert resolve(path).view_name == 'giftlist:membergiftlist'

    @pytest.mark.django_db
    def test_addshoppinglist_url(self):
        user = mixer.blend(User, username="dan")
        path = reverse('giftlist:addshoppinglist', kwargs={'member':user, 'gift':1})
        assert resolve(path).view_name == 'giftlist:addshoppinglist'

    def test_addshoppinglist_url(self):
        path = reverse('giftlist:deleteshoppinglist', kwargs={'id':1, 'group':'family'})
        assert resolve(path).view_name == 'giftlist:deleteshoppinglist'

    