from split_settings.tools import include, optional

include(
    "base.py",
    "apps.py",
    "database.py",
    optional("local.py"),
)