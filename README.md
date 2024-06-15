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
