from flask import Flask, render_template, request, redirect, url_for
from models import db, Site, Device
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create all tables on first run
with app.app_context():
    db.create_all()

# ---------- ROUTES ----------

# Dashboard — shows all sites and overall progress
@app.route('/')
def index():
    sites = Site.query.all()
    return render_template('index.html', sites=sites)

# Add a new site
@app.route('/add-site', methods=['POST'])
def add_site():
    name = request.form.get('name')
    location = request.form.get('location')
    milestone = request.form.get('milestone')
    sla_date = request.form.get('sla_date')
    if name:
        site = Site(name=name, location=location, milestone=milestone, sla_date=sla_date)
        db.session.add(site)
        db.session.commit()
    return redirect(url_for('index'))

# View a single site and its devices
@app.route('/site/<int:site_id>')
def site(site_id):
    site = Site.query.get_or_404(site_id)
    devices = Device.query.filter_by(site_id=site_id).all()
    return render_template('site.html', site=site, devices=devices)

# Add a device to a site
@app.route('/site/<int:site_id>/add-device', methods=['POST'])
def add_device(site_id):
    hostname = request.form.get('hostname')
    device_type = request.form.get('device_type')
    old_model = request.form.get('old_model')
    new_model = request.form.get('new_model')
    assigned_tech = request.form.get('assigned_tech')
    if hostname:
        device = Device(
            hostname=hostname,
            device_type=device_type,
            old_model=old_model,
            new_model=new_model,
            assigned_tech=assigned_tech,
            status='Pending',
            site_id=site_id
        )
        db.session.add(device)
        db.session.commit()
    return redirect(url_for('site', site_id=site_id))

# Update device status
@app.route('/device/<int:device_id>/update', methods=['POST'])
def update_device(device_id):
    device = Device.query.get_or_404(device_id)
    device.status = request.form.get('status')
    device.notes = request.form.get('notes')
    db.session.commit()
    return redirect(url_for('site', site_id=device.site_id))

# Delete a device
@app.route('/device/<int:device_id>/delete', methods=['POST'])
def delete_device(device_id):
    device = Device.query.get_or_404(device_id)
    site_id = device.site_id
    db.session.delete(device)
    db.session.commit()
    return redirect(url_for('site', site_id=site_id))

# Delete a site
@app.route('/site/<int:site_id>/delete', methods=['POST'])
def delete_site(site_id):
    site = Site.query.get_or_404(site_id)
    db.session.delete(site)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)