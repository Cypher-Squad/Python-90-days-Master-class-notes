#Build a student report card dictionary with name, marks (as a nested dict with 3 subjects), and calculate the average marks.
student_report_card = {
    "name": "John Doe",
    "marks": {
        "Math": 85,
        "Science": 90,
        "English": 78
    }
}
# Calculate average marks
total_marks = sum(student_report_card["marks"].values())
average_marks = total_marks / len(student_report_card["marks"])
print(f"Student Name: {student_report_card['name']}")
print(f"Average Marks: {average_marks:.2f}")  # Output: Average Marks: 84.33
