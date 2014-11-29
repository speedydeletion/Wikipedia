# -*- coding: utf-8 -*-
import unittest
import pprint
from wikipedia import wikipedia

class TestData(unittest.TestCase):
  """Test the ability for wikipedia to change the language of the API being accessed."""

  def test_lang(self):
    agent=wikipedia.Agent()
    agent.set_wikidata()
    self.assertEqual(agent.api_url, 'http://www.wikidata.org/w/api.php')

  def test_page(self):
    agent=wikipedia.Agent()
    agent.set_wikidata()
    pprint.pprint(agent.api_url)
    pprint.pprint(agent.page('Q4989296'))
    

    
