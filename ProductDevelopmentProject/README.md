# BriteCore Engineering Application by [@matheuscas](https://github.com/matheuscas)

This project is a API implementation using Django 2.0, DRF (Django Rest Framework), deployed in AWS Lambda using Zappa. 

## Instaling dependencies

First you must install Pipenv. 

```
pipenv install
```

Then, activate the `env` with:

```
pipenv shell
```

## Applying migrations and run the project locally

Get inside the Django project folder and apply migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Run project with:

```
python manage.py runserver
```

## Setup Zappa

I've used [Zappa](https://github.com/Miserlou/Zappa) to deploy this project to AWS Lambda. It's already installed in this project dependencies. 

### Init Zappa

```
zappa init
```

Then, `zappa_settings.json` should be something like:

```
{
    "dev": {
        "django_settings": DJANGO_SETTINGS_FILE,
        "s3_bucket": BUCKET_NAME
    }
}
```

The final version of this file is presented bellow (**I've not committed the file due to sensitive data in `environment_variables`**):

```
{
    "dev": {
        "aws_region": "us-west-2",
        "django_settings": "ProductDevelopmentProject.settings.production",
        "profile_name": "default",
        "project_name": "productdevelopm",
        "runtime": "python3.6",
        "s3_bucket": "zappa-hewrp6wuu",
        "timeout_seconds": 300, 
        "cors": true,
        "binary_support": true,
        "environment_variables": {
            "SECRET_KEY": SECRET_KEY,
            "POSTGRES_DB": DB_NAME_IN_PRODUCTION,
            "POSTGRES_USER": DB_USERNAME,
            "POSTGRES_PASSWORD": DB_PASSWORD,
            "POSTGRES_HOST": DB_HOST,
            "POSTGRES_PORT": "5432"
        }
    }
}
```

You already can deploy at this point without creating an Amazon RDS instance with:

```
zappa deploy dev
```

The deploy will work, but the app won't, because you need to create an Amazon RDS. I've followed this [link](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html).

After that, get the missing data above, such as db name, username, password and host and add to your `zappa_settings.json`. Remember the migrations? You must send them to your remote application. Try this:

```
zappa manage dev migrate
```

Then,  **update** your deploy:

```
zappa update dev
```

Remmeber that you will receive a different URL from this project. You'll have to change `ALLOWED_HOSTS` in `setting/production.py`. Also, you must change this in the [fron-end project](https://github.com/matheuscas/front-britecore-product-development-hiring-project).

And, keep in mind that the URLs defined in `urls.py` will be accessed by `dev/` prefix, since Zappa deploys to lambda under the project name `dev`. 

After that, you will be able to login into Admin and work with the API. 

## Static files

Oh, and don't forget to create a S3 Bucket and send static files to there. Do not fortget to collect them first, of course.

```
python manage.py collectstatic --no-input
```

Change `AWS_STORAGE_BUCKET_NAME` in `setting/production.py` with your new bucket name. You can just simply drag the folder to S3 and it's done. 