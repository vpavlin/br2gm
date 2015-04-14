#!/usr/bin/env python

from __future__ import print_function
import os,sys
import time
from getpass import getpass

from gmusicapi import Mobileclient
import anymarkup

from br2gm.constants import DEFAULT_CREDS

class Playlist():
    api = None
    dryrun = False
    def __init__(self, credentials_path = DEFAULT_CREDS, user = None, dryrun = False, **kwargs):
        
        self.dryrun = dryrun

        self.api = Mobileclient()

        password = None
        if not user:
            user, password = self._loadCredentials(credentials_path)
        else:
            password = self._queryPass(user)

        logged_in = self.api.login(user, password)
        if not logged_in:
            print("Login failed, exiting")
            sys.exit(1)

    def _queryPass(self, user):
        return getpass("Provide password for user %s: " % user)

    def _loadCredentials(self, path = DEFAULT_CREDS):
        credentials = anymarkup.parse_file(path)

        return credentials["credentials"]["user"], credentials["credentials"]["password"]

    def _searchForSong(self, song_item):
        query = "%(artist)s %(title)s" % song_item
        result = self.api.search_all_access(query, 10)
        print("Query: %s, found %d hits" % (query, len(result["song_hits"])))
        first = None
        for item in result["song_hits"]:
            track = item["track"]
            if not first:
                first = track
            if (song_item["title"] in track["title"] or track["title"] in song_item["title"]) and (song_item["artist"] in track["albumArtist"] or\
                                                            song_item["artist"] in track["artist"] or\
                                                            track["artist"] in song_item["artist"] or\
                                                            track["albumArtist"] in song_item["artist"]\
                                                            ):
                return track

        if first:
            print("=> Given title and artist don't match, using first result: %s - %s" % (first["title"], first["artist"]))
            return first

        return None

    def _createPlaylist(self):
        name = "BBC Radio 1 Chart %s" % time.strftime("%Y-%m-%d")
        return self.api.create_playlist(name, public=True)

    def _addToPlaylist(self, playlist_id, song_item):
        self.api.add_songs_to_playlist(playlist_id, song_item["nid"])

    def create(self, songs_list):
        if not self.dryrun:
            playlist_id = self._createPlaylist()
        for song_item in songs_list:
            song = self._searchForSong(song_item)
            if not song:
                print("=> Couldn't find %s" % song_item)
                continue
            if not self.dryrun:
                self._addToPlaylist(playlist_id, song)


