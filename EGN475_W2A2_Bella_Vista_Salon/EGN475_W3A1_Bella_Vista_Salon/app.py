from flask import Flask, render_template, abort

app = Flask(__name__)


# SAMPLE SERVICES
SAMPLE_SERVICES = [
    {
        "id": 1,
        "name": "Haircut & Styling",
        "category": "Hair",
        "description": "Professional haircut and styling tailored to your look.",
        "price_cents": 4500,
        "duration": "45 minutes"
    },
    {
        "id": 2,
        "name": "Hair Coloring",
        "category": "Hair",
        "description": "Custom hair color services for a fresh new look.",
        "price_cents": 9500,
        "duration": "2 hours"
    },
    {
        "id": 3,
        "name": "Manicure",
        "category": "Nails",
        "description": "Professional nail care and manicure treatment.",
        "price_cents": 3500,
        "duration": "45 minutes"
    },
    {
        "id": 4,
        "name": "Pedicure",
        "category": "Nails",
        "description": "Relaxing pedicure with nail care and polish.",
        "price_cents": 5000,
        "duration": "60 minutes"
    },
    {
        "id": 5,
        "name": "Facial Treatment",
        "category": "Skin",
        "description": "A refreshing facial treatment for healthy-looking skin.",
        "price_cents": 6500,
        "duration": "60 minutes"
    },
    {
        "id": 6,
        "name": "Eyebrow Waxing",
        "category": "Beauty",
        "description": "Professional eyebrow shaping and waxing.",
        "price_cents": 2000,
        "duration": "20 minutes"
    }
]


# SAMPLE APPOINTMENTS
SAMPLE_APPOINTMENTS = [
    {
        "id": 1,
        "customer": "Emily Johnson",
        "service": "Haircut & Styling",
        "staff": "Maria Garcia",
        "date": "2026-11-20",
        "time": "10:00 AM",
        "status": "Confirmed"
    },
    {
        "id": 2,
        "customer": "Sophia Martinez",
        "service": "Manicure",
        "staff": "Jessica Williams",
        "date": "2026-11-20",
        "time": "11:30 AM",
        "status": "Confirmed"
    },
    {
        "id": 3,
        "customer": "Olivia Brown",
        "service": "Facial Treatment",
        "staff": "Amanda Davis",
        "date": "2026-11-21",
        "time": "2:00 PM",
        "status": "Pending"
    }
]


# SAMPLE STAFF
SAMPLE_STAFF = [
    {
        "name": "Maria Garcia",
        "role": "Hair Stylist",
        "availability": "9:00 AM - 5:00 PM"
    },
    {
        "name": "Jessica Williams",
        "role": "Nail Technician",
        "availability": "10:00 AM - 6:00 PM"
    },
    {
        "name": "Amanda Davis",
        "role": "Esthetician",
        "availability": "9:00 AM - 4:00 PM"
    }
]


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# SERVICES PAGE
@app.route("/services")
def services():
    return render_template(
        "services.html",
        services=SAMPLE_SERVICES
    )


# SERVICE DETAIL PAGE
@app.route("/services/<int:service_id>")
def service_detail(service_id):

    service = next(
        (
            service for service in SAMPLE_SERVICES
            if service["id"] == service_id
        ),
        None
    )

    if service is None:
        abort(404)

    return render_template(
        "service_detail.html",
        service=service
    )


# BOOKING PAGE
@app.route("/book")
def book():
    return render_template(
        "book.html",
        services=SAMPLE_SERVICES
    )


# STAFF CALENDAR
@app.route("/calendar")
def calendar():
    return render_template(
        "calendar.html",
        appointments=SAMPLE_APPOINTMENTS,
        staff=SAMPLE_STAFF
    )


# APPOINTMENTS PAGE
@app.route("/appointments")
def appointments():
    return render_template(
        "appointments.html",
        appointments=SAMPLE_APPOINTMENTS
    )


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)