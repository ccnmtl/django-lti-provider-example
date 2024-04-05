# django-lti-provider-example

[![Actions Status](https://github.com/ccnmtl/django-lti-provider-example/workflows/build-and-test/badge.svg)](https://github.com/ccnmtl/django-lti-provider-example/actions)

Example Django application using the [django-lti-provider](https://github.com/ccnmtl/django-lti-provider) library.

## Configuration

1. Clone

    git clone https://github.com/ccnmtl/django-lti-provider-example.git
    cd django-lti-provider

2. Create the database

   For Postgres:
     * Create a database user/password (if needed)
     * Create the database `createdb django-lti-provider-example`

   For MySQL:
    @todo

3. Customize settings

    * Create a local_settings.py file in the `djangoltiproviderexample` subdirectory OR
    * Copy `djangoltiproviderexample/local_settings.py.example` to `djangoltiproviderexample/local_settings.py`
    * Then, override the variables from `settings_shared.py` that you need to customize for your local installation.
      * Customize your `DATABASES` dictionary
        * e.g. set NAME, HOST, USER, and PASSWORD. remove PORT (unless it's non-standard)
      * Specify ALLOWED_HOSTS = [ 'localhost', '.your.blackboard.or.moodle.domain', '.your.workstation.domain', ]
    * The ``PYLTI_CONFIG`` variable in your ``local_settings.py`` configures the application consumers and secrets. Generate two long random numbers for these values.

       ```
       PYLTI_CONFIG = {
           'consumers': {
               '<random number string>': {
                   'secret': '<random number string>'
               }
           }
       }
       ```
4. Build the virtual environment

   `make` will build the virtualenv

5. Migrate the database

   `./manage.py migrate`

6. Run

    `make runserver`

## LMS INSTALLATION

Canvas installation happens in two steps. First, as a Canvas
admin-level user, you must install the LTI tool's Developer Key. Then,
as a Course admin, you install the LTI App within the course.

### Developer Key installation

In Canvas, go to Settings -> Developer Keys. Click "+ Developer Key",
and choose LTI Key.

Fill out the following fields:

* Key Name: django-lti-provider-example
* Owner Email: your email
* Method: Manual Entry
* Title: (tool title)
* Description: (short description)
* Redirect URIs: `https://<your hostname>/lti/launch/`
* Target Link URI `https://<your hostname>/lti/launch/`
* OpenID Connect Initiation Url: `https://<your hostname>/lti/login/`
* JWK Method: Public JWK
* Public JWK: (JSON contents of `/lti/jwks/` route)
* LTI Advantage Services: ?
* Placements: ?

Select LtiDeepLinkingRequest where possible, as this allows for deeper
integration.

### LTI App installation

In Canvas's Course page, click on Settings, then the Apps tab. Click "+ App"
to add a new app, and use the following selections:

* Configuration Type: By URL
* Name: (app name)
* Consumer Key: (key from your PYLTI_CONFIG obj in `djangoltiproviderexample/local_settings.py`)
* Consumer Secret: (secret from PYLTI_CONFIG in your local_settings.py)
* Config URL: `https://<your hostname>/lti/launch/` (for LTI 1.1, this
  was `/lti/config.xml`)

### Third-party references

More info is here, which may be helpful:

* https://community.canvaslms.com/docs/DOC-13117-415274482
  * Note: the URL to enter in these steps will be `https://<app hostname>/lti/config.xml`
* LTI 1.3 Canvas configuration docs:
  https://github.com/dmitry-viskov/pylti1.3/wiki/Configure-Canvas-as-LTI-1.3-Platform
