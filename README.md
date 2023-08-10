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

6. Create a "config.py" file and enter the following AWS credentials for the DynamoDB environment you will be using:

```python
AWS_ACCESS_KEY_ID = "your_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
AWS_SESSION_TOKEN = "your_session_token"
REGION_NAME = "region_name"
```

7. Run the script using the following command:

```shell
python app.py
```

8. Access the '/create' route in your browser to create the necessary tables in DynamoDB (Do this just once).

9. Access the DynamoDB service from AWS and manually insert the "pool of questions" found in the 'poolQuestions.py' file.

Done! The backend configuration is ready.