from setuptools import setup, find_packages


setup(
    name='django-templateaddons2',
    version='0.1',
    url='https://github.com/maxvyaznikov/django-templateaddons2',
    download_url='https://github.com/maxvyaznikov/django-templateaddons2',
    author='Max Vyaznikov',
    author_email='maxvyaznikov@gmail.com',
    license='LICENSE',
    description="A set of tools for use with templates of the Django " \
                "framework: additional template tags, context processors " \
                "and utilities for template tag development.",
    long_description=open('README.txt').read(),
    platforms='Any',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    packages=find_packages(),
    include_package_data = True,
)
