# +--------------+
# | Basic config |
# +--------------+
AUTHOR = "gabonog"
SITENAME = "wedflow"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"


# +-------+
# | Pages |
# +-------+
PAGE_PATHS = ["pages"]
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'


# +------+
# | Blog |
# +------+
ARTICLE_PATHS = ["blog"]
ARTICLE_URL = "blog/{slug}/index.html"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"
BLOG_INDEX_SAVE_AS = "blog/index.html"


# +----------+
# | Weddings |
# +----------+
ARTICLE_PATHS += ["weddings"]
WEDDINGS_URL = "weddings/{slug}/index.html"
WEDDINGS_SAVE_AS = "weddings/{slug}/index.html"
WEDDINGS_INDEX_SAVE_AS = "weddings/index.html"


# +-------+
# | Theme |
# +-------+
THEME = "notmyidea"


# +---------------+
# | Other options |
# +---------------+
DEFAULT_PAGINATION = 10
STATIC_PATHS = ["images", "weddings"]
