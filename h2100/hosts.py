from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    #host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
    #host(r'blog', settings.ROOT_URLCONF, name='blog')
    host(r'(?!www).*', 'h2100.hostsconf.urls', name='wildcard'),
)

'''
from 2100.hostconf import urls as redirect_urls

host_patterns = [
	host(r'www', settings.ROOT_URLCONF, name='www'),
    #host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
    host(r'(?!www).*', 'redirect_urls', name='wildcard'),
]

The (?!...) is a "negative lookahead assertion". In contrast, (?<!...) is a
"negative lookbehind assertion". (?=... is a "lookahead assertion that matches
without consuming", and (?<=...) is "lookbehind assertion that matches if preceded."
'''