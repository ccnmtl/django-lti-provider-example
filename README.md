# django-lti-provider-example

Example Django application using the django-lti-provider library

## Configuration

1. Clone

    git clone https://github.com/ccnmtl/django-lti-provider-example.git

2. Create & migrate the database

   For Postgres:
     A. Create the database `createdb django-lti-provider-example`
    
   For MySQL:
    @todo

   `./manage.py migrate`

3. Customize settings

    Create a 1local_settings.py1 file in the 1djangoltiproviderexample1 subdirectory.
    Override the variables from `settings_shared.py` that you need to customize for your local installation. At a minimum, you will need to customize your `DATABASES` dictionary.

4. Build the virtual environment

   `make` will build the virtualenv

5. Run

    `make runserver `

## LMS INSTALLATION


