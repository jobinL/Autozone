# AutoZone - Car Service & Spare Parts Management System

## 🚗 Overview

**AutoZone** is a full-stack web application developed to simplify car service appointments and spare parts management. It features dedicated modules for **Users**, **Admins**, and **Mechanics**, ensuring a smooth workflow across the entire system.

## 🔧 Features

### 👤 User Module
- Sign up / Login / Logout
- Book car service appointments
- Browse and purchase spare parts
- View service history and order status
- Track service progress

### 🔐 Admin Module
- Manage user accounts and mechanic profiles
- Add/Edit/Delete services and spare parts
- View all bookings, orders, and platform analytics
- Upload recent datasets (CSV) to update services or inventory

### 🧰 Mechanic Module
- Login and manage assigned service jobs
- View customer booking details
- Update service status (e.g., In Progress, Completed)
- Track service history
- Notify admin/user upon service completion

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3 (or configurable)
- **APIs:** Integrated for location tracking or notifications (optional)

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/autozone.git
   cd autozone
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations and start the server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

5. Open your browser and visit: `http://127.0.0.1:8000/`

## 📂 Project Structure

```
autozone/
├── autozone/             # Django project settings
├── service_app/          # Core app for bookings, users, mechanics
├── static/               # CSS, JS, images
├── templates/            # HTML templates
├── db.sqlite3            # Default database
├── manage.py
└── README.md
```

## ✅ Future Improvements

- Payment gateway integration
- Email/SMS notification system
- Real-time service tracking with maps
- AI-powered maintenance recommendations

## 📄 License

This project is licensed under the [MIT License](LICENSE).

