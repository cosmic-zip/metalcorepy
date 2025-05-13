# MetalCorePy

MetalCorePy is a simple fullstack application with a standard Django and DRF app, along with an Nginx configuration. It includes:

* docker compose setup
* dockerized applications
* the main Django core app using Domain-Driven Design (DDD)
* `.env` file setup
* a `database` folder for data-related scripts
* a `scripts` folder for utility scripts and helpers

**Avoid manually modifying containers or images.** Always use the designated commands to ensure consistency and compatibility. If you prefer not to use the dockerized environment, you can run the application using the traditional Python workflow with `virtualenv` and `runserver` — in this mode, the database will automatically fall back to the default **SQLite** backend.


## Install Locally

```console
python3 -m venv venv
source venv/bin/activate
pip install -m app/requirements.txt
cp scripts/commit-msg .git/hooks/
```

## Run with Python

```console
cd app/
python manage.py runserver
```

### Or use the custom `runfull` command to run makemigrations, migrate, and runserver

```console
cd app/
python manage.py runfull
```

## Run with Docker

```console
docker compose up
```

## Add a New App

```console
python manage.py create_domain domain_name
```

## How to Run Migrations Inside the Container?

### Step 1: Enter the Container

Use the container name as declared in `docker-compose.yml`. In this case:

```bash
docker exec -it metalcorepy_app bash
```

If you're using Alpine or an image without `bash`, use:

```bash
docker exec -it metalcorepy_app sh
```

Now you are **inside the Django container environment**, with access to the code and Python environment with all required packages.

---

### Step 2: Execute the Migrations

Inside the container:

```bash
python manage.py migrate
```

This command will:

* Connect to PostgreSQL using the `.env.dev` configuration
* Create the default Django tables (auth, admin, etc.)
* Apply any custom migrations from your apps

---

### Alternative: Run Directly with `docker compose run`

If you prefer to execute it in a single command without entering the container, you can run:

```bash
docker compose exec web python manage.py migrate
```

Or, if the service is called `metalcorepy_app`:

```bash
docker compose exec metalcorepy_app python manage.py migrate
```

---

### Note: The Database Must Be Ready

Before running `migrate`, make sure PostgreSQL is:

* Accessible on the correct port
* Initialized with the correct user and password
* The database name must already exist (the official PostgreSQL container does this automatically)

If errors persist, run:

```bash
docker compose logs postgres
```
