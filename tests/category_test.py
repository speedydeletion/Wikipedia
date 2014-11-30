#https://en.wikipedia.org/wiki/

import pprint
from wikipedia import wikipedia
agent = wikipedia.Agent()
#agent.set_site_lang('wiki', n)
pg = agent.page('Category:Mountains_of_Kosovo')
pprint.pprint(['page content',pg.category_members()])
