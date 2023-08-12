import requests
import json
import os
import random

from sources.rss3 import get_rss3


class VideoController:
    def get_feed(self):
        return get_rss3()
