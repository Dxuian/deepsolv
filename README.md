# Django Project

This is a Django project.

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-folder>
    ```

### Option 1: Traditional Setup

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Change directory to [insta](http://_vscodecontentref_/1)**:
    ```sh
    cd insta
    ```

4. **Apply migrations**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server**:
    Navigate to the [insta](http://_vscodecontentref_/2) folder and run:
    ```sh
    python manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

### Option 2: Using Docker Compose

2. **Build and run the Docker containers**:
    ```sh
    docker-compose up --build
    ```

 

3. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Additional Commands

- **Run tests**:
    ```sh
    python manage.py test
    ```

## License

This project is licensed under the MIT License.