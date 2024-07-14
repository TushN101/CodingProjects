# Flask Login Page Website

This project is a web application built with Flask that includes user authentication features such as login, registration, password recovery, account locking, rate limiting, and password strength checking.

## Features

- **Dashboard Page**: A personalized dashboard for logged-in users.
- **Login Page**: User login with rate limiting and account locking.
- **Registration Page**: User registration with password strength checking.
- **Forget Password Page**: Password recovery with security questions.
- **Account Locking**: Accounts are locked after multiple failed login attempts.
- **Rate Limiting**: Limits the number of login and registration attempts to prevent abuse.
- **Password Strength Checking**: Ensures passwords meet complexity requirements.

## Requirements

- Python 3.x
- Flask
- Flask-Limiter

## Installation

1. Clone the repository or download the script files.
2. Install the required Python libraries:

   ```sh
   pip install Flask Flask-Limiter
   ```

3. Create a `users.json` file to store user data:

   ```json
   {}
   ```

## Usage

1. Run the Flask application:

   ```sh
   python main.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Register a new account, log in, and check out the login features.

## Screenshots

### Dashboard Page
![pic1](https://github.com/user-attachments/assets/3eb6459d-1e48-42fd-8163-da4b5eb124a4)

### Registration Page
![image](https://github.com/user-attachments/assets/01603876-3a61-43f8-87cf-a68cceb0c4d7)

### Login Page
![pic2](https://github.com/user-attachments/assets/fa36a297-57e0-496d-a285-1ced6313cd4a)

### Recovering Account - Part 1 (Specifying Email)
![pic3](https://github.com/user-attachments/assets/a27d7c8b-658f-45c3-ba61-fd2d2b1a5c1d)

### Recovering Account - Part 2 (Answering Secret Question)
![pic4](https://github.com/user-attachments/assets/ca6af32c-9fef-4506-9837-8f9405433987)

### Logged In
![pic5](https://github.com/user-attachments/assets/6e975dba-f1f9-4d08-b1bf-0c52ddb7e38d)


### Stopping Brute Force with Rate Limiter
![pic6](https://github.com/user-attachments/assets/bb21d035-b8af-4d8a-b120-91f4dfa2ab24)

