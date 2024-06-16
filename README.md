# Webhook Repository

This repository serves as the endpoint for GitHub webhook events. It receives events from the action-repo, stores them in MongoDB, and provides an endpoint to retrieve the latest events.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

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

5. **Run the application:**

   ```bash
   python run.py
   ```

## Usage

1. **Expose the local server using ngrok:**

   ```bash
   ngrok http 5000
   ```

2. **Set up the GitHub webhook:**

   Go to your GitHub repository settings, navigate to **Webhooks**, and add a new webhook with the ngrok URL:

   ```
   http://<your-ngrok-url>/webhook/receiver
   ```

3. **Trigger GitHub actions:**

   Perform push, pull request, and merge actions in the action-repo to trigger the webhook.

## Configuration

All configuration is managed through environment variables defined in the `.env` file.

## Endpoints

- **POST /webhook/receiver**

  Receives GitHub webhook events and stores them in MongoDB.

- **GET /webhook/events**

  Retrieves the latest events from MongoDB.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

These README files provide a comprehensive guide for setting up, using, and contributing to both repositories. Feel free to modify the content as necessary to fit your specific requirements and preferences.

- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/action-repo.git
   cd action-repo
   ```

2. **Create a new branch for your changes:**

   ```bash
   git checkout -b feature-branch
   ```

3. **Make your changes and commit them:**

   ```bash
   git add .
   git commit -m "Describe your changes"
   ```

4. **Push your changes to GitHub:**

   ```bash
   git push origin feature-branch
   ```

5. **Create a pull request** from your feature branch to the main branch.

## Usage

1. **Trigger Actions:**
   - Push: Make changes to the repository and push them to GitHub.
   - Pull Request: Create a pull request from one branch to another.
   - Merge: Merge a pull request.

2. **Webhooks:**
   - Ensure the webhook is configured to point to the webhook-repo endpoint (e.g., `http://your-public-server/webhook/receiver`).

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.


