# Fingerprint Door Lock System

a razz pi-based door lock system with fingerprint authentication, password fallback, and access logging!

## Features
- fingerprint authentication (via AS608 sensor)
- password fallback with strength requirements
- lockout after 3 failed attempts
- password reset with identity verification
- csv access logging with timestamps

## Hardware Used
- raspberry pi 3 model b v1.2
- as608 fingerprint sensor (coming soon)
- servo motor (coming soon)
- raspberry pi camera module (coming soon)

## Setup
1. clone this repo
2. create a `password.txt` file with your initial hashed password
3. install dependencies: `pip install -r requirements.txt`
4. run: `python lock.py`

## Notes
picamera2 needs to be installed on the razz pi directly, since it only works on linux!

## Usage
at prompt, enter `fingerprint`, `password`, or `resetpassword`

## Testing
run `python -m pytest test_lock.py`

## Status
🚧 work in progress: pending hardware integration of camera + fingerprint sensor
