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

