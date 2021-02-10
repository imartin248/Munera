from django.urls import reverse, resolve
from django.test import RequestFactory
from mixer.backend.django import mixer
from giftlist.views import home, deleteGift
from giftlist.models import Gift, UserGroup, GroupMember
from django.contrib.auth.models import User
import pytest


@pytest.mark.django_db
class TestViews:

    def test_home(self):
        path = reverse('giftlist:home')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    def test_deleteGift(self):
        mixer.blend(Gift)
        path = reverse('giftlist:deletegift', kwargs={'id':1})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    def test_groupResults(self):
        path = reverse('giftlist:groupresults')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    def test_createGroup(self):
        path = reverse('giftlist:creategroup')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    def test_groupLlist(self):
        mixer.blend(UserGroup)
        path = reverse('giftlist:grouplist', kwargs={'group':'cABEfFWTFGakpILUlzoh'})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    def test_memberGiftList(self):
        path = reverse('giftlist:membergiftlist', kwargs={'User':User})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    