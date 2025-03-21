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

# Name your content directory posts
ARTICLE_EXCLUDES = ['pages']
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

STATIC_PATHS = ['images']

MENUITEMS = (
  ('Home','/'),
  ('About','/about'),
  ('Projects','/projects'),
)