def publish_class(classes, class_id, title, instructor, schedule, capacity):
    if class_id in classes:
        return "Error: A class with this ID already exists."
    if capacity <= 0:
        return "Error: Capacity must be greater than zero."

    classes[class_id] = {
        "title": title,
        "instructor": instructor,
        "schedule": schedule,
        "capacity": capacity,
        "confirmed": [],
        "waitlist": [],
        "attended": []
    }
    return f"Success! Published '{title}' ({class_id}) with {capacity} seats."


def mark_attendance(classes, members, class_id, present_ids):
    if class_id not in classes:
        return "Error: Class ID not found."

    fitness_class = classes[class_id]
    marked = []
    skipped = []

    for m_id in present_ids:
        m_id = m_id.strip().upper()
        if m_id in fitness_class["confirmed"]:
            if m_id not in fitness_class["attended"]:
                fitness_class["attended"].append(m_id)
            marked.append(members[m_id])
        else:
            skipped.append(m_id)

    summary = f"Attendance recorded for {fitness_class['title']}: {len(fitness_class['attended'])}/{len(fitness_class['confirmed'])} present."
    if skipped:
        summary += f" (Ignored non-confirmed IDs: {', '.join(skipped)})"
    return summary
