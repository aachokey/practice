try:
	from setuptools import setup
except:
	from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Aric Chokey',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'achokey21@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)