from setuptools import setup, find_packages

setup(
    name='django-object-tools',
    version='1.11.0',
    description='Django app enabling painless creation of additional admin object tools.',
    long_description=open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Consulting',
    author_email='dev@praekelt.com',
    url='http://github.com/praekelt/django-object-tools',
    packages=find_packages(),
    include_package_data=True,
    tests_require=[
        'django-snippetscream',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
