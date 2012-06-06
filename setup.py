from distutils.core import setup
from generator import __version__

setup (
    name = 'Generator',
    version = __version__,
    description = 'Generator: generators for Django',
    author = 'Bruno Henrique - Garu',
    author_email = 'squall.bruno@gmail.com',
    classifiers = [
                   "Development Status :: 1 - Planning",
                   "Framework :: Django",
                   "Intended Audience :: Developers",
                   "Intended Audience :: System Administrators",
                   "Operating System :: OS Independent",
                   "Topic :: Software Development"
                  ],
    packages = [
              'generator',
              'generator.factory',
              'generator.templates',
              'generator.management',
              'generator.management.commands',
              'generator.tests'
             ],
)
