__author__ = 'Jason'

from SpaceEngineers_Clansite import settings,urls # import the settings file
from django.core.urlresolvers import get_resolver

"""
def ListAllUrls(debug=False):
    resolver = get_resolver(urls)
    links = {}
    for view, regexes in resolver.reverse_dict.iteritems():
        link = "%s: %s" % (view, regexes)
        links += {view:regexes}
        if debug: #to optimize?
            print(link)
        #links.append(linkdict) - testing - to remove
    return links
"""


def GlobalContext(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'ClanName': settings.CLAN_NAME,'WebsiteTitle':settings.WEBSITE_TITLE}
    #return {'ClanName': settings.CLAN_NAME,'WebsiteTitle':settings.WEBSITE_TITLE,'UrlList':ListAllUrls()}


if __name__ == '__main__':
    settings.configure()
    print(ListAllUrls())