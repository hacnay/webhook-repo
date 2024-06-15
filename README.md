
### README.md for `webhook-repo`

```markdown
# GitHub Webhook Receiver

This repository contains a Flask application that serves as a webhook receiver for GitHub events. It captures events triggered from your GitHub repository (`action-repo`), stores them in MongoDB Atlas, and provides a clean, real-time interface to visualize the latest updates.

---

## Overview

### Features

- **Webhook Integration**: Receive events like pushes, pull requests, and merges from GitHub.
- **MongoDB Storage**: Persist event data in MongoDB Atlas for reliable storage.
- **Real-time Updates**: Automatically fetch and display the latest events every 15 seconds on the frontend.

---

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/webhook-repo.git
   cd webhook-repo
   ```

2. **Install Dependencies**
   - Set up a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # Activate virtual environment
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure MongoDB Atlas**
   - Create a MongoDB Atlas cluster and obtain your connection URI.
   - Update the `.env` file with your MongoDB URI:
     ```
     MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
     ```

4. **Run the Flask Application**
   - Set Flask app environment variables:
     ```bash
     export FLASK_APP=app.py
     export FLASK_ENV=development  # Optional: Enable development mode
     ```
   - Run the application:
     ```bash
     flask run
     ```
   - The application will start locally at `http://localhost:5000/`.

---

## Endpoints

- **`POST /webhook`**: Receive and process GitHub webhook events.
- **`GET /events`**: Fetch the latest events from MongoDB for display on the frontend.

---

## Frontend

- Open `index.html` in your browser (`webhook-repo/index.html`) to view and monitor real-time GitHub events fetched from MongoDB Atlas.

---

## Deployment

- Deploy the Flask application on a cloud platform (e.g., Heroku, AWS) for production use.
- Update the GitHub webhook URL in your `action-repo` to the deployed endpoint for seamless integration.

---

## Technologies Used

- Python
- Flask
- MongoDB Atlas
- HTML, CSS (for the frontend)

---

## Contributing

- Fork the repository, make your changes, and submit a pull request.
- Report issues or suggest improvements by opening an issue.

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

```

