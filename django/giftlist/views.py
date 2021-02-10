# Django
from django.http import HttpResponse
from django.shortcuts import ( render, redirect, get_object_or_404 )
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as user_model

# local Django
from .models import GroupMember, Gift, UserGroup, ShoppingList, GroupMemberRequest
from .forms import AddGift, CreateGroup, AddGroupMember



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    """
    Returns the home page if the user is authinticated.
    """

    user = request.user.id
    print("this is from: ")
    print(user)

    if request.method == 'POST':

        request.POST = request.POST.copy()
        request.POST.__setitem__('user',user)
        
        add_gift_form = AddGift(request.POST)
        print("Fuck: ")
        print(request.POST)
       
        if add_gift_form.is_valid():
            gift = add_gift_form.save()
            gift.save()
            return redirect('giftlist:home')

    else:
        user = request.user
        create_group_form = CreateGroup()
        user_groups = GroupMember.objects.filter(member=user)
        print(user)
        gifts = Gift.objects.filter(user=user)
        add_gift_form = AddGift()
        context = {'create_group_form':create_group_form, 'groups':user_groups,'gifts': gifts, 'add_gift_form': add_gift_form}
        print(gifts)
        return render(request, 'giftlist/home.html', context)

def deleteGift(request,id):
    """
    Deletes a gift the logined user gift list.
    """
    object = get_object_or_404(Gift, pk=id)
    object.delete()
    return redirect('giftlist:home')

def groupResults(request):
    """
    Returns a list of groups that the current user is apart of.
    """
    user = request.user

    if request.method == 'POST':
        form = AddGroupMember(request.POST)
        if form.is_valid():
            group_member = form.save(commit=False)
            group_member.member = user
            group_member.save()
            return redirect('giftlist:home')


    else:
        form = AddGroupMember()
        query = request.GET.get('q')
        results = UserGroup.objects.filter(Q(group_name__icontains=query))
        context = {'form': form, 'results': results}
        return render(request, 'group/groupresults.html', context)

def createGroup(request):
    """
    Creates a group and adds the creator of the group as the first member.
    """
    user = request.user
    user_id = user.id
    request.POST = request.POST.copy()
    request.POST.__setitem__('admin',user_id)
    group_name = request.POST['group_name']
    
    
        
    create_group_form = CreateGroup(request.POST)
       
    if create_group_form.is_valid():
        group = create_group_form.save()
        group.save()

    group = UserGroup.objects.get(group_name=group_name, admin=user_id)
    print("look:")
    print(group.id)
    member = GroupMember.objects.create(member=user, group=group)
    
    return redirect('giftlist:home')

def groupLlist(request, group):
    user = request.user
    group_object = get_object_or_404(UserGroup, group_name=group)
    
    members = GroupMember.objects.filter(group=group_object)
    shoppinglist = ShoppingList.objects.filter(buyer=user)

    context = {'group':group,'members': members, 'shoppinglist':shoppinglist}
    return render(request, 'giftlist/grouplist.html', context)

def memberGiftList(request, User):
    member = User
    print("this member was sent thru the url:"+ member)

    person = user_model.objects.get(username="{0}".format(str(member)))
    print("I got this user from my query: {0}".format(person.id))
    gifts = Gift.objects.filter(user=person.id)
    context = {'member': member, 'gifts': gifts}
    return render(request, 'giftlist/membergiftlist.html', context)

def add_gift_to_shoppinglist(request, member, gift):
    user = request.user
    gift = Gift.objects.get(pk=gift)
    shoppinglist = ShoppingList.objects.create(gift = gift,buyer = user)
    gift.selected = True
    gift.save()
    return redirect('giftlist:membergiftlist', member)

def delete_gift_from_shoppinglist(request,id,group):
    object = get_object_or_404(ShoppingList, gift=id)
    object.delete()

    gift = Gift.objects.get(pk=id)
    gift.selected = False
    gift.save()
    return redirect('giftlist:grouplist',group)

def groupRequests(request):
    user = request.user.id
    groups = list(UserGroup.objects.filter(admin=user))
    group_requests = list(GroupMemberRequest.objects.filter(to_group__in=groups))
    context = {'group_requests': group_requests}
    return render(request, 'giftlist/grouprequests.html',context)


def send_group_request(request, id):
    requested_group_id = id
    group = get_object_or_404(UserGroup, pk=requested_group_id)
    user = request.user

    obj, created = GroupMemberRequest.objects.get_or_create(
        from_user=user,
        to_group=group
    )
    
    return redirect('giftlist:home') 

def accept_group_request(request, new_member_id, requested_group_id, group_request_id):
    """
    Accept a User's request to a User Group.
    """
    new_member_id = new_member_id
    requested_group_id = requested_group_id
    group_request_id = group_request_id

    new_member = get_object_or_404(user_model, pk=new_member_id)
    requested_group = get_object_or_404(UserGroup, pk=requested_group_id)  

    new_group_member = GroupMember(member=new_member,group=requested_group)
    new_group_member.save()

    group_request = get_object_or_404(GroupMemberRequest, pk=group_request_id)
    group_request.delete()

    return redirect('giftlist:home')
