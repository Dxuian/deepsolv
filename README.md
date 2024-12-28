# Django Project

This is a Django project.

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-folder>
    ```

<!-- 2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate -->
        ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
5. **Change dir to insta**:
    ```sh
    cd insta
    ```

6. **Install dependencies**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

<!-- 6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ``` -->

7. **Run the development server**:
    Navigate to the [insta](http://_vscodecontentref_/2) folder and run:
    ```sh
    cd insta
    python manage.py runserver
    ```

8. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Additional Commands

- **Run tests**:
    ```sh
    python manage.py test
    ```
<!-- 
- **Collect static files**:
    ```sh
    python manage.py collectstatic
    ``` -->

## License

This project is licensed under the MIT License.