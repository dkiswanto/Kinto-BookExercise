try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TeamJ Project',
    'author': 'TeamJ',
    'url': 'http://www.teamj.org',
    'download_url': 'http://www.teamj.org/downloads',
    'author_email': 'teamj@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'teamjproject'
}

setup(**config)

