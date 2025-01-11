DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f"{env('DB_NAME', default='db')}.sqlite3", # type: ignore
        'TEST': {
            'NAME': f"{env('DB_NAME', default='db')}_test.sqlite3", # type: ignore
        },
    }
}