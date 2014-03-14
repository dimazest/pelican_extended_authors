from setuptools import setup, find_packages


setup(
    name='pelican_extended_authors',
    version=0.1,
    url='https://github.com/dimazest/pelican_extended_authors',
    author="Maikel Wever",
    author_email="maikel.wever@paylogic.eu",
    maintainer="Dmitrijs Milajevs",
    maintainer_email="dimazest@gmail.com",
    description=(
        "The extended authors plugin for Pelican provides a context "
        "generator so you can include a biography with an author. "
        "It is compatible with the default author pages generator, "
        "so there is very little to modify."
    ),
    long_description=open("README.rst").read(),
    license='Creative Commons. Attribution-ShareAlike 3.0 Unported',
    packages=find_packages(),
    package_data={'': ['LICENSE', 'README.rst']},
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
    zip_safe=True,
    install_requires=[
        'pelican',
    ],
)
