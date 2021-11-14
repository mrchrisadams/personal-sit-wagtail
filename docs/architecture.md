# Architecture and project layout

The thinking behind this setup - written down here so I don't forget.

This app is written with the expectation that editing content is a different job to serving content, and happens much less frequently.

So, with this in mind, while your authoring experience might be one handled by django, serving the content is probably best done with flat files.




## Directory structure

### `apps`
Functionality related to third party projects, vendored projects I don't want to move into core, to keep updates relatively simple

### `core`

Key functionality related to the site itself. Models to represent pages, tags and so on.

Commands for manipulating and saving content.

Urls live here.

### `settings`

Where the django settings live, as well as config for WSGI servers

### `media`

Local copies of uploads or derived images

### `static`

Files that don't change, but aren't media. Things like favicons or images.

### `templates`

Where the majority of the django templates live. Where possible, templates live here, not in an apps own template directory.

### `tests`

Tests.

----------

## Hidden folders

### `.build`

Generated and shipped up to object storage

### `.venv`

The prefered place for virtual env and libraries


##
