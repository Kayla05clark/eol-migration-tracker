from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Site(db.Model):
    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))
    milestone = db.Column(db.String(200))
    sla_date = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # One site has many devices
    devices = db.relationship('Device', backref='site', cascade='all, delete-orphan')

    def progress(self):
        total = len(self.devices)
        if total == 0:
            return 0
        completed = sum(1 for d in self.devices if d.status == 'Complete')
        return round((completed / total) * 100)

class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100), nullable=False)
    device_type = db.Column(db.String(100))
    old_model = db.Column(db.String(100))
    new_model = db.Column(db.String(100))
    assigned_tech = db.Column(db.String(100))
    status = db.Column(db.String(50), default='Pending')
    notes = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign key linking device to a site
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)