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
🚀 Features

    IP Logging: Captures and stores the IP address of visitors accessing the /track/ endpoint.
    Smooth Redirection: Redirects users to a regular page, maintaining a natural user experience.
    Lightweight and Modular: Built using Flask, making it easy to deploy and extend.

🛠️ Installation
Prerequisites

    Python 3.7+
    A virtual environment tool (recommended)
    Flask (specified in requirements.txt)

Steps

    1. Clone the repository:
      git clone <repository-url>
