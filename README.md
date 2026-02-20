# fingerprint door lock system

a razz pi-based door lock system with fingerprint authentication, password fallback, and access logging!

## features
- fingerprint authentication (via AS608 sensor)
- password fallback with strength requirements
- lockout after 3 failed attempts
- password reset with identity verification
- csv access logging with timestamps

## hardware used
- raspberry pi 3 model b v1.2
- as608 fingerprint sensor (coming soon)
- servo motor (coming soon)
- raspberry pi camera module (coming soon)
- raspberry pi display v1.1
- 3d printed locking mechanism (coming soon)
- as many jumper cables as required + a breadboard

## setup
1. clone this repo
2. create `password.txt` file with your initial hashed password
3. install dependencies: `pip install -r requirements.txt`
4. run: `python lock.py`

## notes
picamera2 needs to be installed on the razz pi directly, since it only works on linux!

## usage
at prompt, enter `fingerprint`, `password`, or `resetpassword`

## testing
run `python -m pytest test_lock.py`

## future steps
🚧 work in progress: pending hardware integration of camera + fingerprint sensor
