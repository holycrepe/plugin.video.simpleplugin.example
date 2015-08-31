# -*- coding: utf-8 -*-
# Module: main
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from simpleplugin import Plugin

# Create plugin instance
plugin = Plugin()

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Animals': [{'name': 'Crab',
                       'thumb': 'http://www.vidsplay.com/vids/crab.jpg',
                       'video': 'http://www.vidsplay.com/vids/crab.mp4'},
                      {'name': 'Alligator',
                       'thumb': 'http://www.vidsplay.com/vids/alligator.jpg',
                       'video': 'http://www.vidsplay.com/vids/alligator.mp4'},
                      {'name': 'Turtle',
                       'thumb': 'http://www.vidsplay.com/vids/turtle.jpg',
                       'video': 'http://www.vidsplay.com/vids/turtle.mp4'}
                      ],
            'Cars': [{'name': 'Postal Truck',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4'}
                     ],
            'Food': [{'name': 'Chicken',
                      'thumb': 'http://www.vidsplay.com/vids/chicken.jpg',
                      'video': 'http://www.vidsplay.com/vids/bbqchicken.mp4'},
                     {'name': 'Hamburger',
                      'thumb': 'http://www.vidsplay.com/vids/hamburger.jpg',
                      'video': 'http://www.vidsplay.com/vids/hamburger.mp4'},
                     {'name': 'Pizza',
                      'thumb': 'http://www.vidsplay.com/vids/pizza.jpg',
                      'video': 'http://www.vidsplay.com/vids/pizza.mp4'}
                     ]}


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.
    :return: list
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of videostreams in a given category from some site or server.
    :param category: str
    :return: list
    """
    return VIDEOS[category]


def list_categories(params):
    """
    Create the list of video categories in the Kodi interface.

    :param params: dict - a dictionary with plugin call parameters.
    :return: dict
    """
    listing = []
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        listing.append({
            # Item label
            'label': category,
            # Item thumbnail
            'thumb': VIDEOS[category][0]['thumb'],  # Item thumbnail
            # Item fanart. Here we use the same image as the thumbnail for simplicity's sake.
            'fanart': VIDEOS[category][0]['thumb'],
            # Item callback URL
            'url': plugin.get_url(action='list_videos', category=category),
            # Since this item will open a sub-listing,
            # we don't specify 'is_folder' and 'is_playable' parameters explicitly,
            # leaving them to their default values (True and False respectively).
        })
    # Return the list of video categories for Kodi to display
    # Here we use plugin.create_listing method to specify additional parameter - view_mode.
    # '500' corresponds to Confluence skin 'Thumbnail' view.
    # Note: other skins have their own view_mode numeric codes!
    # Look into 'MyVideoNav.xml' file of your favorite skin
    # to find the necessary view_mode codes.
    return plugin.create_listing(listing, view_mode=500)


def list_videos(params):
    """
    Create the list of playable videos in the Kodi interface.

    :param params: dict - a dictionary with plugin call parameters.
    :return: list
    """
    listing = []
    # Get the list of videos in the category.
    videos = get_videos(params['category'])
    # Iterate through videos.
    for video in videos:
        listing.append({
            # Item label
            'label': video['name'],
            # Item thumbnail
            'thumb': video['thumb'],
            # Item fanart. Here we use the same image as the thumbnail for simplicity's sake.
            'fanart': video['thumb'],
            # Item callback URL
            'url': plugin.get_url(action='play', video=video['video']),
            # The item is playable
            'is_playable': True
        })
    # Return the list of videos in a chosen category for Kodi to display
    # Here we simply return a listing so Kodi will display it with default settings.
    return listing


def play_video(params):
    """
    Play a video by the provided path.

    :param params: dict - a dictionary with plugin call parameters.
    :return: str - a playable path to a videofile.
    """
    path = params['video']
    # Return a path for Kodi to play
    return path


# Map actions
# Note that we map callable objects without brackets ()
plugin.actions['root'] = list_categories  # 'root' item is mandatory!
plugin.actions['list_videos'] = list_videos
plugin.actions['play'] = play_video
if __name__ == '__main__':
    # Run our plugin
    plugin.run()
