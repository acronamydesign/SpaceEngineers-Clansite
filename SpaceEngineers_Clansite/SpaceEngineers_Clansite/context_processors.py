__author__ = 'Jason'

from SpaceEngineers_Clansite import settings # import the settings file

def GlobalContext(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'ClanName': settings.CLAN_NAME,'WebsiteTitle':settings.WEBSITE_TITLE}