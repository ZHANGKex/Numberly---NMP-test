# URL Shortener

This is a simple URL shortener web application. It is built using Django, and it allows users to input a long URL and receive a shortened version of it. Users can then use the shortened URL to be redirected to the original URL.

## Features

- Shorten a long URL
- Redirect from a shortened URL to the original URL
- View all shortened URLs
- Basic validation of URL input
- Unit tests for core functionality

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file should contain the following dependencies:

    ```txt
    asgiref==3.8.1
    coverage==7.5.4
    Django==4.2.14
    sqlparse==0.5.0
    typing-extensions==4.12.2
    tzdata==2024.1
    validators==0.32.0
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

    The application should now be running at `http://localhost:8000`.

## Usage

1. **Shorten a URL**:
    - Navigate to `http://localhost:8000/`
    - Enter a long URL into the form and submit
    - Receive a shortened URL in the format `http://localhost:8000/{slug}`

2. **Redirect using a shortened URL**:
    - Use the shortened URL to navigate to the original URL

3. **View all shortened URLs**:
    - Navigate to `http://localhost:8000/view_urls/` to see a list of all shortened URLs

## Running Tests

To run the tests for this application, use the following command:

```bash
python manage.py test
```

## Running Coverage Tests

To check the test coverage using `coverage.py`, follow these steps:

1. **Install `coverage.py`** (if not already installed):

    ```bash
    pip install coverage
    ```

2. **Run tests with coverage**:

    ```bash
    coverage run manage.py test
    ```

3. **Generate coverage report**:

    ```bash
    coverage report
    ```

    This will output a coverage report in the terminal.

4. **Generate HTML coverage report**:

    ```bash
    coverage html
    ```

    This will create an HTML report in the `htmlcov` directory. Open `htmlcov/index.html` in a browser to view the detailed coverage report.