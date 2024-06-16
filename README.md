
# Webhook Repository

This repository serves as the endpoint for GitHub webhook events. It receives events from the action-repo, stores them in MongoDB, and provides an endpoint to retrieve the latest events.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/webhook-repo.git
   cd webhook-repo
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   Create a `.env` file in the root directory with the following content:

   ```
   MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/github_events?retryWrites=true&w=majority
   ```

   Replace `<username>` and `<password>` with your MongoDB Atlas credentials.

5. **Run the application locally:**

   ```bash
   python run.py
   ```

## Usage

1. **Set up the GitHub webhook:**

   Go to your GitHub repository settings, navigate to **Webhooks**, and add a new webhook with the URL of your public server:

   ```
   http://<your-public-server>/webhook/receiver
   ```

2. **Trigger GitHub actions:**

   Perform push, pull request, and merge actions in the action-repo to trigger the webhook.

## Configuration

All configuration is managed through environment variables defined in the `.env` file.

## Endpoints

- **POST /webhook/receiver**

  Receives GitHub webhook events and stores them in MongoDB.

- **GET /webhook/events**

  Retrieves the latest events from MongoDB.

## Deployment

To deploy the application to a public server, follow these steps:

1. **Choose a hosting provider** (e.g., Heroku, AWS, DigitalOcean, etc.) and set up your server.
2. **Clone the repository to your server:**

   ```bash
   git clone https://github.com/your-username/webhook-repo.git
   cd webhook-repo
   ```

3. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment variables:**

   Create a `.env` file in the root directory with the following content:

   ```
   MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/github_events?retryWrites=true&w=majority
   ```

6. **Run the application:**

   ```bash
   python run.py
   ```

7. **Ensure your server allows incoming traffic on the port the Flask application is running on (default is 5000).**

8. **Update the GitHub webhook URL** to point to your public server's endpoint (e.g., `http://your-public-server/webhook/receiver`).

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
