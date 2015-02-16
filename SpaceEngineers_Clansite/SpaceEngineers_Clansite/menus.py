__author__ = 'Jason'

from menu import Menu, MenuItem
from django.core.urlresolvers import reverse
import SpaceEngineers_Clansite.views

# Add two items to our main menu
Menu.add_item("main", MenuItem("Home",
                               reverse("SpaceEngineers_Clansite.views.home"),
                               weight=10,)) # remove brackets here if you wish to specify an icon (current one is not valid)
                               #icon="home"))

Menu.add_item("forum", MenuItem("Forum",
                               reverse("SpaceEngineers_Clansite.views.forum"),
                               weight=20,)) # remove brackets here if you wish to specify an icon (current one is not valid)
                               #icon="report"))

Menu.add_item("admin",
             reverse("admin:index"),
             weight=80,
             separator=True,
             check=lambda request: request.user.is_superuser)



"""
# Add a My Account item to our user menu
Menu.add_item("user", MenuItem("My Account",
                               reverse("accounts.views.myaccount"),
                               weight=10,
                               children=myaccount_children))

# Define children for the my account menu
myaccount_children = (
    MenuItem("Edit Profile",
             reverse("accounts.views.editprofile"),
             weight=10,
             icon="user"),
    MenuItem("Admin",
             reverse("admin:index"),
             weight=80,
             separator=True,
             check=lambda request: request.user.is_superuser),
    MenuItem("Logout",
             reverse("accounts.views.logout"),
             weight=90,
             separator=True,
             icon="user"),
)



"""