# EOL Migration Tracker

A web-based deployment tracking tool built to manage end-of-life 
device migrations across multiple enterprise network sites.

## Background

Built to mirror real-world network deployment experience managing 
multi-site hardware refresh projects, milestone tracking, SLA 
adherence, and cross-functional technician coordination.

## Features

- Add and manage multiple deployment sites
- Track individual devices per site (hostname, device type, old vs new model)
- Assign technicians to devices
- Update device status — Pending, In Progress, Complete
- Auto-calculated progress bar per site based on device completion
- SLA date tracking per site
- Log notes and incident details per device
- Delete sites and devices with confirmation

## Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML/CSS
- Pandas
- ReportLab

## How to Run

**1. Clone the repo:**
git clone https://github.com/YOURUSERNAME/eol-migration-tracker.git
cd eol-migration-tracker

**2. Create and activate virtual environment:**
python -m venv venv
venv\Scripts\activate

**3. Install dependencies:**
pip install -r requirements.txt

**4. Run the app:**
python app.py

**5. Open in browser:**
http://127.0.0.1:5000

## Project Structure

eol-migration-tracker/
├── app.py
├── models.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── site.html
└── static/
    └── style.css

## Author

Built by [Your Name] as part of a network deployment portfolio 
demonstrating real-world project tracking, SLA management, 
and multi-site deployment coordination.