# FileDrop - File Sharing API

I wanted to have the ability to upload and download files and share them thru multiple devices in my homeserver. so i created this simple API called FileDrop to do so!

## Features

- User registration and login for secure access.
- File upload functionality for storing files on your server.
- File download capability to retrieve uploaded files.
- Basic security measures for user data protection.

## Before Use
To set up and run this API, make sure to set up your `SECRET_KEY` in the `config.py` file
Run The API and
Access the API locally via `http://localhost/`.
i havent included the frontend i amde for this, as i didnt deem it to be necessary. you can create a frontend for this and make sure that your Flask API has an endpoint (for eg; /list) that provides a list of uploaded files as JSON for the front-end to fetch.

## Usage

- Register a user using the `/register` endpoint.
- Log in with your registered user using the `/login` endpoint.
- Upload files using the `/upload` endpoint (needs authentication).
- Download files using the `/download/<filename>` endpoint (will need authentication).

## Configuration

- Modify the database and other settings in the `config.py` file if you want to customise/modify stuff according to your needs