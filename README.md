# Fingerprint Door Lock System

A Raspberry Pi-based door lock system with fingerprint authentication, 
password fallback, and access logging.

## Features
- Fingerprint authentication (via AS608 sensor)
- Password fallback with strength requirements
- Lockout after 3 failed attempts
- Password reset with identity verification
- CSV access logging with timestamps

## Hardware Used
- Raspberry Pi 3 Model B V1.2
- AS608 fingerprint sensor (coming soon)
- Servo motor (coming soon)
- Raspberry Pi Camera module (coming soon)

## Setup
1. Clone this repo
2. Create a `password.txt` file with your initial hashed password
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python lock.py`

## Usage
At the prompt, enter `fingerprint`, `password`, or `resetpassword`

## Testing
Run `python -m pytest test_lock.py`

## Status
🚧 Work in progress: pending hardware integration of camera + fingerprint sensor
