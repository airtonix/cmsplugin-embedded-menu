import os
from setuptools import (
  setup,
  find_packages,
)
import cmsplugin_embeddedmenu


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='cmsplugin-embedded-menu',
    version=cmsplugin_embeddedmenu.__version__,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),
    packages=find_packages(),
    install_requires=(
        'django-cms',
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='DjangoCMS plugin for embedding menus in placeholders',
    long_description = read('README.md'),
    license='BSD',
    keywords='django-cms, plugin',
    url='http://github.com/airtonix/cmsplugin-embedded-menu',
    include_package_data=True,
    zip_safe = False,
)
