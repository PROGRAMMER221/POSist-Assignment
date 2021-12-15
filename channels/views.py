from django.db import connection
from django.shortcuts import redirect, render
from .forms import ChannelForm, TagForm, InviteForm
from django.contrib import messages
from .models import Tags, Channel, Message
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def HomeView(request):
    return render(request, 'base.html')

@login_required
def AddTagName(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Add Name Added Successfully')
            return redirect('/add-tag/')
        else:
            messages.error(request, 'Invalid Data Format')
            return redirect('/')
    else:
        form = TagForm()
    return render(request, 'tag.html', context={'form':form})

@login_required
def AddChannel(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Channel Has Successfully Been Created')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Data Format')
            return redirect('/')
    else:
        form = ChannelForm()
    return render(request, 'channel.html', context={'form':form})

@login_required
def JoinChannel(request, id):
    chn = Channel.objects.get(id=id)
    usr = request.user
    usr.channelJoined.add(chn)
    usr.save()
    messages.success(request, 'You are now part of this Channel.')
    return redirect('/')

@login_required
def JoinedChannels(request):
    context = {
        'channels' : request.user.channelJoined
    }
    return render(request, 'joinedChannels.html', context)

@login_required
def MessagePanel(request, id):
    context = {
        'ID' : id,
        'message' : Message.objects.filter(channel=Channel.objects.get(id=id))
    }
    return render(request, 'messagePannel.html', context)

@login_required
def PostMessage(request, id):
    msg = Message()
    msg.message = request.POST['msg']
    msg.usr = request.user.id
    msg.channel = Channel.objects.get(id=id)
    msg.save()
    return redirect('/message-panel/'+id)

def AllChannels(request):
    context = {
        'channels' : Channel.objects.all()
    }
    return render(request, 'allChannel.html', context)

@login_required
def InvitePeople(request):
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your Invitation Has Been Send :) ')
            email = form.cleaned_data.get('email')
            send_mail(
                'Let\'s Talk Invitation',
                'Your Friend Has Invited You to join Let\'s Talk. It\'s very easy click on the link below and get your self registed and enjoy :) \n http://posistassignment.pythonanywhere.com/',
                'aman_22@outlook.com',
                [email],
                fail_silently=False,
            )
            return redirect('/')
        else:
            messages.error(request, 'Invalid Data Format')
            return redirect('/')
    else:
        form = InviteForm()
    
    return render(request, 'send-invite.html', context = {'form':form})