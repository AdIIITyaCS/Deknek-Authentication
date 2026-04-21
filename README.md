# Django Auth Website (PostgreSQL)

A full-stack Django website with:

- User signup, login, logout
- Protected dashboard
- PostgreSQL database integration
- Separate user details table (`accounts_userprofile`)
- Templates and static files inside app structure

## Tech Stack

- Python
- Django
- PostgreSQL
- HTML, CSS

## Project Structure

- `core/` : Django project settings and root URLs
- `accounts/` : Authentication app
- `accounts/templates/accounts/` : App templates
- `accounts/static/accounts/css/` : App CSS
- `accounts/static/accounts/images/` : App images
- `.env` : Environment variables (secret key, DB config)

## Features

- Signup form creates:
- Login credentials in `auth_user`
- User profile in `accounts_userprofile`
- Login and logout using Django authentication
- Dashboard requires authentication
- No-cache protection on auth pages to prevent back-button stale session data after logout

## Environment Variables

Create a `.env` file with:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
