from django.shortcuts import redirect, render
from .forms import ChannelForm, TagForm
from django.contrib import messages
from .models import Tags, Channel, Message
from django.contrib.auth.decorators import login_required

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