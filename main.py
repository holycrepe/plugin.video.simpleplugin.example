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
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of videostreams in a given category from some site or server.
    """
    return VIDEOS[category]


@plugin.action()
def root():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories and yield list items for Kodi to display
    for category in categories:
        yield {
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
        }


@plugin.action()
def list_videos(params):
    """
    Create the list of playable videos in the Kodi interface.
    """
    # Get the list of videos in the category.
    videos = get_videos(params.category)
    # Iterate through videos and yield list items for Kodi to display
    for video in videos:
        yield {
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
        }


@plugin.action()
def play(params):
    """
    Play a video by the provided path.

    :param params: plugin call parameters.
    :return: str - a playable path to a videofile.
    """
    path = params.video
    # Return a path for Kodi to play
    return path


if __name__ == '__main__':
    # Run our plugin
    plugin.run()
