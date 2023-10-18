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

## Usage

- Register a user using the `/register` endpoint.
- Log in with your registered user using the `/login` endpoint.
- Upload files using the `/upload` endpoint (needs authentication).
- Download files using the `/download/<filename>` endpoint (will need authentication).

## Configuration

- Modify the database and other settings in the `config.py` file if you want to customise/modify stuff according to your needs