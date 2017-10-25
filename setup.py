# -*- coding: utf-8 -*-

# It extends util
from setuptools import setup

# This app version
version = 'v2.3.5'

# Now setup, key-value in param
setup(
    # app name
    name = 'qqbot',
    # change version later
    version = version,
    # Python array
    packages = ['qqbot', 'qqbot.qcontactdb', 'qqbot.plugins'],
    # qqbot, run
    # qqbot, terminal????
    entry_points = {
        'console_scripts': [
            'qqbot = qqbot:RunBot',
            'qq = qqbot:QTerm'
        ]
    },
    # html request
    # certifi, collection of ssl trust vendors
    # like cron
    install_requires = ['requests', 'certifi', 'apscheduler'],
    # des
    description = "QQBot: A conversation robot base on Tencent's SmartQQ",
    # who made
    author = 'pandolia' ,
    #
    author_email = 'pandolia@yeah.net',
    url = 'https://github.com/pandolia/qqbot/',
    download_url = 'https://github.com/pandolia/qqbot/archive/%s.tar.gz' % version,
    keywords = ['QQBot', 'conversation robot', 'tencent', 'qq',
                'web', 'network', 'python', 'http'],
    classifiers = [],
)
