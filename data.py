

def load_sample_data():
    members = {
        "M01": "Aarav Sharma",
        "M02": "Diya Nair",
        "M03": "Rohan Verma",
        "M04": "Ananya Iyer",
        "M05": "Karthik Reddy",
        "M06": "Sneha Rao"
    }

    classes = {
        "C101": {
            "title": "Morning HIIT",
            "instructor": "Coach Arjun",
            "schedule": "Mon 7:00 AM",
            "capacity": 2,
            "confirmed": ["M01", "M02"],   # Full class!
            "waitlist": ["M03"],            # M03 is first in line
            "attended": []
        },
        "C102": {
            "title": "Power Yoga",
            "instructor": "Coach Meera",
            "schedule": "Wed 6:00 PM",
            "capacity": 4,
            "confirmed": ["M04"],
            "waitlist": [],
            "attended": []
        },
        "C103": {
            "title": "Indoor Cycling",
            "instructor": "Coach Vikram",
            "schedule": "Fri 5:30 PM",
            "capacity": 3,
            "confirmed": [],
            "waitlist": [],
            "attended": []
        }
    }

    return members, classes