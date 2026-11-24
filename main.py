from data import load_sample_data
from booking import book_seat, cancel_booking
from management import publish_class, mark_attendance


def display_all_classes(classes, members):
    print("\n" + "=" * 65)
    print("PUBLISHED FITNESS CLASSES")
    print("=" * 65)
    for c_id, info in classes.items():
        confirmed_names = [f"{m} ({members[m]})" for m in info["confirmed"]]
        waitlist_names = [f"{m} ({members[m]})" for m in info["waitlist"]]
        attended_names = [f"{m} ({members[m]})" for m in info["attended"]]

        print(f"[{c_id}] {info['title']} | Instructor: {info['instructor']} | Time: {info['schedule']}")
        print(f"   Seats: {len(info['confirmed'])}/{info['capacity']} confirmed | Waitlist: {len(info['waitlist'])}")
        print(f"   Confirmed List : {', '.join(confirmed_names) if confirmed_names else 'None'}")
        print(f"   Waitlist Queue : {', '.join(waitlist_names) if waitlist_names else 'None'}")
        print(f"   Actual Attended: {', '.join(attended_names) if attended_names else 'Not marked yet'}")
        print("-" * 65)


def display_members(members):
    print("\n--- Registered Members ---")
    for m_id, name in members.items():
        print(f"{m_id}: {name}")
    print("--------------------------")


def main():
    members, classes = load_sample_data()

    while True:
        print("\n=== FITNESS CLASS BOOKING SYSTEM (PHASE 1) ===")
        print("1. View All Classes, Waitlists & Attendance")
        print("2. Publish a New Fitness Class")
        print("3. Book a Class Seat")
        print("4. Cancel a Reservation (Auto-Promotes Waitlist)")
        print("5. Mark Actual Class Attendance")
        print("6. View Registered Members")
        print("0. Exit")

        choice = input("\nEnter your choice (0-6): ").strip()

        if choice == "1":
            display_all_classes(classes, members)

        elif choice == "2":
            c_id = input("Enter new Class ID (e.g., C104): ").strip().upper()
            title = input("Enter Class Title (e.g., Zumba): ").strip()
            instructor = input("Enter Instructor Name: ").strip()
            schedule = input("Enter Schedule (e.g., Sat 10:00 AM): ").strip()
            cap_input = input("Enter Seat Capacity: ").strip()

            if cap_input.isdigit():
                result = publish_class(classes, c_id, title, instructor, schedule, int(cap_input))
                print("\n>>", result)
            else:
                print("\n>> Error: Capacity must be a positive whole number.")

        elif choice == "3":
            display_members(members)
            c_id = input("Enter Class ID to book (e.g., C101): ").strip().upper()
            m_id = input("Enter Member ID (e.g., M05): ").strip().upper()
            result = book_seat(classes, members, c_id, m_id)
            print("\n>>", result)

        elif choice == "4":
            c_id = input("Enter Class ID to cancel from (e.g., C101): ").strip().upper()
            m_id = input("Enter Member ID cancelling (e.g., M01): ").strip().upper()
            result = cancel_booking(classes, members, c_id, m_id)
            print("\n>>", result)

        elif choice == "5":
            c_id = input("Enter Class ID to mark attendance (e.g., C101): ").strip().upper()
            if c_id in classes:
                print("Confirmed members:", classes[c_id]["confirmed"])
                raw_ids = input("Enter present Member IDs separated by commas (e.g., M01, M02): ")
                present_list = raw_ids.split(",")
                result = mark_attendance(classes, members, c_id, present_list)
                print("\n>>", result)
            else:
                print("\n>> Error: Class ID not found.")

        elif choice == "6":
            display_members(members)

        elif choice == "0":
            print("Exiting Fitness Class Booking System. Goodbye!")
            break

        else:
            print("\n>> Invalid choice. Please select a number between 0 and 6.")


if __name__ == "__main__":
    main()