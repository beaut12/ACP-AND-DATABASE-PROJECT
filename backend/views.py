from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import User
import os
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
from .models import Donation
import random

views = Blueprint('views', __name__)

@views.route('/')
def login():
    return render_template('login.html')

@views.route('/signup')
def signup():
    return render_template('signup.html')

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@views.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        food_name = request.form['food_name']
        quantity = request.form['quantity']
        expiration = request.form['expiration']

        ref_id = str(uuid.uuid4())[:4]

        new_donation = Donation(
            ref_id=ref_id,
            food_name=food_name,
            quantity=quantity,
            expiration=expiration,
            status="Available"
        )
        db.session.add(new_donation)
        db.session.commit()

        return redirect(url_for('views.receive'))

    return render_template('donate.html')

@views.route('/receive')
@login_required
def receive():
    search = request.args.get("search", "")

    if search:
        donations = Donation.query.filter(
            Donation.food_name.ilike(f"%{search}%") |
            Donation.status.ilike(f"%{search}%") |
            Donation.location.ilike(f"%{search}%")
        ).all()
    else:
        donations = Donation.query.all()

    return render_template("receive.html", donations=donations)

@views.route('/about')
@login_required
def about():
    return render_template('about.html')

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@views.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():

    if request.method == 'POST':

        current_user.fullname = request.form.get('fullname')

        if 'profile_pic' in request.files:
            img = request.files['profile_pic']

            if img.filename != "":
                filename = secure_filename(img.filename)

                upload_folder = os.path.join('website', 'static', 'uploads')

                os.makedirs(upload_folder, exist_ok=True)

                save_path = os.path.join(upload_folder, filename)
                img.save(save_path)

                current_user.profile_picture = filename

        db.session.commit()
        flash("Profile updated successfully!")
        return redirect(url_for('views.profile'))

    return render_template("edit_profile.html")

@views.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():

    if request.method == 'POST':
        old = request.form.get("old_password")
        new = request.form.get("new_password")

        if not check_password_hash(current_user.password, old):
            flash("Old password is incorrect.")
            return redirect(url_for('views.change_password'))

        current_user.password = generate_password_hash(new)
        db.session.commit()

        flash("Password updated successfully!")
        return redirect(url_for('views.profile'))

    return render_template("change_password.html")

@views.route('/receive-list')
@login_required
def receive_list():
    donations = Donation.query.all()
    return render_template("receive_list.html", donations=donations)

@views.route('/view/<int:id>')
def view_donation(id):
    donation = Donation.query.get_or_404(id)
    return render_template('view.html', donation=donation)

@views.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete_donation(id):
    donation = Donation.query.get(id)

    if donation.user_id != current_user.id:
        flash("You cannot delete this donation.", "error")
        return redirect(url_for('views.receive'))

    db.session.delete(donation)
    db.session.commit()
    flash("Donation deleted successfully.", "success")
    return redirect(url_for('views.receive'))

@views.route('/reserve/<int:id>', methods=['POST'])
@login_required
def reserve_donation(id):
    donation = Donation.query.get(id)

    if donation.reservation_status == "reserved":
        flash("This donation is already reserved.", "error")
        return redirect(url_for('views.receive'))

    donation.reservation_status = "reserved"
    db.session.commit()

    flash("You reserved this donation.", "success")
    return redirect(url_for('views.receive'))
