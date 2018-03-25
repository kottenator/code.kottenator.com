# code.kottenator.com

A place to host my code experiments.

## What is this?

The goal of this project is to secure my experimental code and provide access only to a specific group of people.

It's based on [Django authentication](https://docs.djangoproject.com/en/2.0/topics/auth/) (Django users with access keys) and on Nginx [X-Accel-Redirect](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/) header which allows me to:

* Manage users, keys and projects in Django.
* Serve the actual static files by Nginx.

Read more in [project's Wiki](https://github.com/kottenator/code.kottenator.com/wiki).
