def gather_credits(credit, *courses):
    total_credit = 0
    courses_dict = dict()

    for course_name, score in courses:
        if total_credit >= credit:
            break
        if course_name not in courses_dict:
            courses_dict[course_name] = score
            total_credit += score

    if total_credit >= credit:
        result = f"Enrollment finished! Maximum credits: {total_credit}.\nCourses: "
        course_list = ", ".join(sorted(courses_dict.keys()))  # Join course names
        result += course_list

    else:
        result = f"You need to enroll in more courses! You have to gather {credit - total_credit} credits more."

    return result


def gather_credits2(needed_credits, *courses_info):
    gathered_credits = 0
    enrolled_courses = []

    for course_name, course_credits in courses_info:
        if gathered_credits >= needed_credits:
            break
        if course_name in enrolled_courses:
            continue
        enrolled_courses.append(course_name)
        gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        return f"""Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {', '.join(sorted(enrolled_courses))}"""
    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."



print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))