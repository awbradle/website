AUTHOR = 'Andie Bradley'
SITENAME = 'Andie Bradley'
SITEURL = ""

PATH = "content"
THEME = "bootstrap_ab"

TIMEZONE = 'America/Chicago'

#DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/awbradle"),
    ("Embedded AI Systems Lab @ EMU", "https://eas-lab-emich.github.io"),
)

# Social widget
SOCIAL = (
    ("IRC: Libera Chat (pokeysquirrel)", "https://libera.chat"),
)

# Articles per page
DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Whether to display pages on the menu of the template. Templates may or may not honor this setting.
DISPLAY_PAGES_ON_MENU = False
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_EXCLUDES = ['static']

# Name your content directory posts
ARTICLE_EXCLUDES = ['pages', 'static']
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

STATIC_PATHS = ['images', 'static']

MAIN_MENU = True
MENUITEMS = (
  ('Home','/'),
  ('About','/about'),
  ('Projects', '/projects')
  	
)

EXTRA_PATH_METADATA = {
    'static/gol/game.html': {'path': 'projects/gol/index.html'},
    'static/gol/Display.js': {'path': 'projects/gol/Display.js'},
    'static/gol/GameLife.js': {'path': 'projects/gol/GameLife.js'},
}