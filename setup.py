from setuptools import setup, find_packages

setup(
    name='code.kottenator.com',
    version='0.0.3',
    description='A place to host my code experiments',
    url='https://github.com/kottenator/code.kottenator.com',
    author='Rostyslav Bryzgunov',
    author_email='kottenator@gmail.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=['bin/manage.py'],
    install_requires=[
        'Django~=2.0',
        'settings-overrider~=1.0'
    ],
    extras_require={
        'prod': [
            'uwsgi',
            'psycopg2-binary'
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
