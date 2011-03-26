"""Just some family's website."""

from setuptools import setup, find_packages


setup(
    name='Dawsoning',
    version='2.0',
    url='http://dawsoning.com/',
    author='Matt Dawson',
    author_email='matt@dawsoning.com',
    description="Just some family's website.",
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'Django',
        'jellyroll',
        'django-pagination',
        'feedparser',
        'docutils',
    ],
    tests_require='nose',
    test_suite='nose.collector',
)
