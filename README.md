# I_Know_Where_You_Are
# IP Tracking and Redirection Tool

## 📝 Description
This is a Flask-based web application designed to log a visitor's IP address when they access a specific link (`/track/`). After capturing the IP, the application seamlessly redirects the user to a regular page, creating a smooth and unnoticeable experience.

This tool can be particularly useful for investigative purposes or to monitor link interactions.

---

## 📂 Project Structure

```plaintext
track/
├── app
│   ├── __init__.py          # Application initialization
│   ├── models.py            # Database models (if applicable)
│   ├── routes.py            # Application routes
│   └── templates
│       └── index.html       # Frontend template for the redirected page
├── README.md                # Documentation
├── requirements.txt         # Python dependencies
└── run.py                   # Entry point to start the application

Voici une version complète de ton fichier README.md pour l'application de suivi d'IP et de redirection. J'ai ajouté des sections qui expliquent l'installation, l'utilisation et d'autres détails utiles pour les contributeurs ou utilisateurs potentiels :

# I_Know_Where_You_Are
## IP Tracking and Redirection Tool

### 📝 Description
This is a Flask-based web application designed to log a visitor's IP address when they access a specific link (`/track/`). After capturing the IP, the application seamlessly redirects the user to a regular page, creating a smooth and unnoticeable experience.

This tool can be particularly useful for investigative purposes or to monitor link interactions.

---

### 📂 Project Structure

```plaintext
track/
├── app
│   ├── __init__.py          # Application initialization
│   ├── models.py            # Database models (if applicable)
│   ├── routes.py            # Application routes
│   └── templates
│       └── index.html       # Frontend template for the redirected page
├── README.md                # Documentation
├── requirements.txt         # Python dependencies
└── run.py                   # Entry point to start the application

🚀 Installation

    Clone the repository:

git clone https://github.com/yourusername/I_Know_Where_You_Are.git
cd I_Know_Where_You_Are

Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

    pip install -r requirements.txt

⚙️ Configuration

Before running the application, ensure that you have configured your environment settings correctly. If you plan to use a database, you may need to adjust the models.py file and set up the database.
🏃‍♂️ Usage

To run the application locally:

python run.py

Once the server is running, you can access the application via your browser at:

http://127.0.0.1:5000

To track a user's IP, simply visit the /track/ endpoint. For example:

http://127.0.0.1:5000/track/

After the request is made, the user's IP address will be logged, and they will be redirected to the regular page (/).
🛠️ Dependencies

    Flask
    (List any additional dependencies you may need)

You can find all dependencies in the requirements.txt file.
🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

To contribute:

    Fork the repository
    Create a new branch (git checkout -b feature-branch)
    Make your changes
    Commit your changes (git commit -am 'Add new feature')
    Push to the branch (git push origin feature-branch)
    Create a new pull request

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
