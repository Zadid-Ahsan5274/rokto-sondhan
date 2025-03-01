# Rokto Sondhan - Blood Donation Management System

## Overview
Rokto Sondhan is a web-based Blood Donation Management System designed to facilitate blood donation and requests efficiently. The platform connects blood donors with patients in need, streamlines donation records, and provides an easy-to-use interface for managing blood stocks and requests.

## Features
- **Donor Management:** Register and manage blood donors.
- **Patient Management:** Store patient details for blood requests.
- **Blood Requests:** Patients can request blood by specifying the required blood type and location.
- **Blood Donations:** Records of donations made by donors.
- **Stock Management:** Maintains available blood stock information.
- **User Authentication:** Admin panel for managing users, donors, and patients.

## Installation

### Prerequisites
- Python 3.x
- Django
- SQLite3 (or any other configured database)

### Setup Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/rokto-sondhan.git
   cd rokto-sondhan
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser (admin account):
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` to access the homepage.
- Admin panel: `http://127.0.0.1:8000/admin/`
- Register as a donor or make a blood request as a patient.

## Database Structure
### Models Used:
- **User:** Manages authentication and user roles.
- **Patient:** Stores patient details and blood request history.
- **Donor:** Manages registered donors and their donations.
- **BloodRequest:** Tracks requests for blood with patient details.
- **BloodDonate:** Stores donor blood donation records.
- **Stock:** Maintains the available blood units for different blood types.

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/donors/` | GET | List all donors |
| `/api/patients/` | GET | List all patients |
| `/api/blood-requests/` | POST | Create a new blood request |
| `/api/donations/` | GET | Retrieve donation records |

## Deployment
To deploy this project on a cloud server:
1. Install **Gunicorn** and **Whitenoise**:
   ```sh
   pip install gunicorn whitenoise
   ```
2. Configure `settings.py` for production:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com']
   ```
3. Use `gunicorn` to run the application:
   ```sh
   gunicorn --bind 0.0.0.0:8000 your_project.wsgi
   ```

## Contributing
- Fork the repository.
- Create a new branch: `git checkout -b feature-branch`
- Commit changes: `git commit -m "Added new feature"`
- Push to the branch: `git push origin feature-branch`
- Create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, contact [your_email@example.com].

