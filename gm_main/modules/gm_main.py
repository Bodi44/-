from gmusicapi import Mobileclient

from class_adt import Array_repr
from builtins import *  # noqa

from getpass import getpass


def ask_for_credentials():
    """Make an instance of the api and attempts to login with it.
    Return the authenticated api.
    """

    # We're not going to upload anything, so the Mobileclient is what we want.
    api = Mobileclient()

    logged_in = False
    attempts = 0

    while not logged_in and attempts < 3:
        email = input('Email: ')
        password = getpass('Password: ')

        logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
        attempts += 1

    return api


def demonstrate():
    """Demonstrate some api features."""

    api = ask_for_credentials()

    ###---------------------MENU OPTIONS:-----------------------#

    library = Array_repr(api.get_all_songs())
    registered_devices = Array_repr(api.get_registered_devices())
    playlist = Array_repr(api.get_all_playlists())
    promoted_songs = Array_repr(api.get_promoted_songs())
    stations = Array_repr(api.get_all_stations())
    browse_history = Array_repr(api.get_browse_podcast_hierarchy())



    research_menu = {'user songs': library, 'user registered devices': registered_devices, 'user playlists': playlist,'promoted songs': promoted_songs, 'user stations':stations, 'user browse history': browse_history}
    if not api.is_authenticated():
        print("Sorry, those credentials weren't accepted.")
        return

    print('Successfully logged in.')
    print()
    answer = 'yes'
    while(answer == 'yes'):
        print("-----Available features-----")

        for feature in research_menu:
            print("-", feature)
        option = input("Choose an option: ")
        assert option in research_menu.keys(), "Sorry, there is no such option!"

    
        print(research_menu[option].print_res())
        print('You`d like to continue research?')
        answer = input('Your answer(yes/no): ')

if __name__ == '__main__':
    demonstrate()