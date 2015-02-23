__author__ = 'Jason'

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render , render_to_response
from django.template import RequestContext, loader
from pybb import views as bb
import SpaceEngineers_Clansite.settings as settings

def home(request):
    webname = settings.WEBSITE_TITLE
    brand = settings.CLAN_NAME
    return render_to_response('index.html',context_instance=RequestContext(request,{"title":webname,"brand":brand}))

@user_passes_test(lambda u: u.is_staff)
def staff(request):
    return render_to_response('staff.html',context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
def superuser(request):
    return render_to_response('superuser.html',context_instance=RequestContext(request))

"""
def forum(request):
    return bb.render()
"""