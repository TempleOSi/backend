## Installation and Running the Application

The application is currently fully functional when used locally. Follow the instructions below to install it:

1. Clone this repository to your local environment and ensure that you meet the prerequisites.

### Backend Setup

2. Navigate to the "backend" folder.

3. Create a virtual environment to install Python dependencies.

```shell
python3 -m venv venv
```

4. Activate the virtual environment.

```shell
source venv/bin/activate
```

5. Install the necessary dependencies for the project within the virtual environment. These dependencies are listed in the "requirements.txt" file.

```shell
pip install -r requirements.txt
```

6. Create a "db_config.json" file and enter the following MongoDB credentials needed for your remote or local database

```json
{
    "db": {
            "url" : "mongodb://localhost:27017/",
            "name" :"templeos-dev",
            "user" :"",
            "password" :""
    }
}
```

7. Run the script using the following command:

```shell
python app.py
```

Done! The backend configuration is ready.