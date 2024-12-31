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
```

## 🚀 Features

    IP Logging: Captures and stores the IP address of visitors accessing the /track/ endpoint.
    Smooth Redirection: Redirects users to a regular page, maintaining a natural user experience.
    Lightweight and Modular: Built using Flask, making it easy to deploy and extend.

## 🛠️ Installation
Prerequisites

    Python 3.7+
    A virtual environment tool (recommended)
    Flask (specified in requirements.txt)

Steps

Clone the repository:

    git clone https://github.com/S1a0m/I_Know_Where_You_Are.git

Navigate to the project directory:

    cd track

Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Run the application:

    python run.py

Access the application in your browser at:

    http://127.0.0.1:5000/track/

## 📖 Usage
```plaintext
    Share the /track/ URL with the target.
    When the target accesses the link:
        Their IP address is logged.
        They are redirected to a normal page (index.html).
    Retrieve and analyze the logged IP addresses (details can be expanded based on your storage method).
```

## 🔄 Future Enhancements
```plaintext
    Database Integration: Store logged IPs in a database (e.g., SQLite, PostgreSQL).
    Dashboard: Add a frontend to visualize captured IP data.
    Customization Options: Allow configuration of redirection URLs.
```

## 🛡️ License

This project is provided "as-is" for educational and research purposes only. Ensure compliance with local laws before using this tool.

## ⚠️ Disclaimer

This tool is intended for ethical and lawful use only. Misuse of this application for malicious purposes is strictly prohibited.

## 📧 Contact

For feedback or collaboration, feel free to reach out:

    Email: precieuxdev1@gmail.com

Thank you for exploring this project! 🎉
