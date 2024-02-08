# Building A Blog With Django

This repository contains the source code and resources needed to build a blog using Django.

## Project description

The project consists of developing a blog using the Django framework, providing a solid structure for creating, viewing, editing and deleting posts.

## Prerequisites

Before you begin, make sure you have installed:

-Python
-Django
- A virtual environment (recommended)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/luisrpavanelli/blog-py-django.git
```

2. Navigate to the project directory:

```bash
cd blog-py-django
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

## Settings

1. Configure the environment variables:
   
    Rename the `.env.example` file to `.env` and fill in the necessary variables.

2. Run Django migrations:

```bash
python manage.py migrate
```

3. Create a superuser:

```bash
python manage.py createsuperuser
```

4. Start the development server:

```bash
python manage.py runserver
```

## Usage

- Access the admin panel at `http://localhost:8000/admin` and log in with your superuser credentials to add, edit or delete posts.

- View the blog at `http://localhost:8000`.

## Contribution

Contributions are welcome! Feel free to open issues or send pull requests.

## Credits

This project was developed based on the course offered by [tomitokko](https://github.com/tomitokko). Special thanks to the instructor for sharing knowledge and resources.

## License

This project is licensed under the [MIT License](LICENSE).