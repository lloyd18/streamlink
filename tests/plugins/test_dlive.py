import unittest

from streamlink.plugins.dlive import DLive


class TestPluginDLive(unittest.TestCase):
    def test_can_handle_url(self):
        # should match
        self.assertTrue(DLive.can_handle_url("https://dlive.tv/pewdiepie"))
        self.assertTrue(DLive.can_handle_url("https://dlive.tv/p/pdp+K6DqqtYWR"))

        # shouldn't match
        self.assertFalse(DLive.can_handle_url("https://dlive.tv/"))
