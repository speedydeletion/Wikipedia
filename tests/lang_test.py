# -*- coding: utf-8 -*-
import unittest

from wikipedia import wikipedia


class TestLang(unittest.TestCase):
  """Test the ability for wikipedia to change the language of the API being accessed."""

  def test_lang(self):
    fr_agent=wikipedia.Agent()
    fr_agent.set_lang("fr")
    self.assertEqual(fr_agent.api_url, 'http://fr.wikipedia.org/w/api.php')
