import sqlite3

connection = sqlite3.connect('registration.db')
cursor = connection.cursor()

cursor.execute('PRAGMA foreign_keys = ON')

while True:
    choice = input(
        """
Enter choice:
1. Manage faculty
2. Manage course
3. Manage section
4. Manage student
5. Manage enrollment
6. Show student transcript
Q. Quit
> """
    ).strip().upper()

    if choice == 'Q':
        break

    if choice == '1':
        action = input(
            """
Enter action:
1. List faculty
2. Add faculty
3. Update faculty
> """
        ).strip()

        if action == '1':
            print("ID | Name | Email")
            cursor.execute('SELECT * FROM faculty')
            for row in cursor:
                print(row)

        elif action == '2':
            name = input('Enter name: ')
            email = input('Enter email: ')
            cursor.execute(
                'INSERT INTO faculty (name, email) VALUES (?, ?)',
                (name, email)
            )
            connection.commit()
            print('Faculty added.')

        elif action == '3':
            id = int(input('Enter faculty ID to update: '))
            name = input('Enter updated name: ')
            email = input('Enter updated email: ')
            cursor.execute(
                'UPDATE faculty SET name = ?, email = ? WHERE id = ?',
                (name, email, id)
            )
            connection.commit()
            print('Faculty updated.')

    elif choice == '2':
        action = input(
            """
Enter action:
1. List courses
2. Add course
3. Update course
> """
        ).strip()

        if action == '1':
            print("ID | Department | Number | Credits | Description")
            cursor.execute('SELECT * FROM course')
            for row in cursor:
                print(row)

        elif action == '2':
            department = input('Enter department: ')
            number = input('Enter course number: ')
            credits = int(input('Enter credits: '))
            description = input('Enter description: ')
            cursor.execute(
                'INSERT INTO course (department, number, credits, description) VALUES (?, ?, ?, ?)',
                (department, number, credits, description)
            )
            connection.commit()
            print('Course added.')

        elif action == '3':
            id = int(input('Enter course ID to update: '))
            department = input('Enter updated department: ')
            number = input('Enter updated course number: ')
            credits = int(input('Enter updated credits: '))
            description = input('Enter updated description: ')
            cursor.execute(
                'UPDATE course SET department = ?, number = ?, credits = ?, description = ? WHERE id = ?',
                (department, number, credits, description, id)
            )
            connection.commit()
            print('Course updated.')

    elif choice == '3':
        action = input(
            """
Enter action:
1. List sections
2. Add section
3. Update section
> """
        ).strip()

        if action == '1':
            print("SectionID | CourseID | FacultyID | Semester | Day | Time")
            cursor.execute('SELECT * FROM section')
            for row in cursor:
                print(row)

        elif action == '2':
            course_id = int(input('Enter course ID: '))
            faculty_id = int(input('Enter faculty ID: '))
            semester = input('Enter semester: ')
            day = input('Enter day(s): ')
            time = input('Enter time: ')
            cursor.execute(
                'INSERT INTO section (course_id, faculty_id, semester, day, time) VALUES (?, ?, ?, ?, ?)',
                (course_id, faculty_id, semester, day, time)
            )
            connection.commit()
            print('Section added.')

        elif action == '3':
            id = int(input('Enter section ID to update: '))
            course_id = int(input('Enter updated course ID: '))
            faculty_id = int(input('Enter updated faculty ID: '))
            semester = input('Enter updated semester: ')
            day = input('Enter updated day(s): ')
            time = input('Enter updated time: ')
            cursor.execute(
                'UPDATE section SET course_id = ?, faculty_id = ?, semester = ?, day = ?, time = ? WHERE id = ?',
                (course_id, faculty_id, semester, day, time, id)
            )
            connection.commit()
            print('Section updated.')

    elif choice == '4':
        action = input(
            """
Enter action:
1. List students
2. Add student
3. Update student
> """
        ).strip()

        if action == '1':
            print("ID | Name | Major")
            cursor.execute('SELECT * FROM student')
            for row in cursor:
                print(row)

        elif action == '2':
            name = input('Enter student name: ')
            major = input('Enter major: ')
            cursor.execute(
                'INSERT INTO student (name, major) VALUES (?, ?)',
                (name, major)
            )
            connection.commit()
            print('Student added.')

        elif action == '3':
            id = int(input('Enter student ID to update: '))
            name = input('Enter updated student name: ')
            major = input('Enter updated major: ')
            cursor.execute(
                'UPDATE student SET name = ?, major = ? WHERE id = ?',
                (name, major, id)
            )
            connection.commit()
            print('Student updated.')

    elif choice == '5':
        action = input(
            """
Enter action:
1. List enrollments
2. Add enrollment
3. Update enrollment
4. Delete enrollment
> """
        ).strip()

        if action == '1':
            print("ID | StudentID | SectionID | Grade")
            cursor.execute('SELECT * FROM enrollment')
            for row in cursor:
                print(row)

        elif action == '2':
            student_id = int(input('Enter student ID: '))
            section_id = int(input('Enter section ID: '))
            grade = input('Enter grade (leave blank if none yet): ')
            cursor.execute(
                'INSERT INTO enrollment (student_id, section_id, grade) VALUES (?, ?, ?)',
                (student_id, section_id, grade)
            )
            connection.commit()
            print('Enrollment added.')

        elif action == '3':
            id = int(input('Enter enrollment ID to update: '))
            student_id = int(input('Enter updated student ID: '))
            section_id = int(input('Enter updated section ID: '))
            grade = input('Enter updated grade: ')
            cursor.execute(
                'UPDATE enrollment SET student_id = ?, section_id = ?, grade = ? WHERE id = ?',
                (student_id, section_id, grade, id)
            )
            connection.commit()
            print('Enrollment updated.')

        elif action == '4':
            id = int(input('Enter enrollment ID to delete: '))
            cursor.execute('DELETE FROM enrollment WHERE id = ?', (id,))
            connection.commit()
            print('Enrollment deleted.')

    elif choice == '6':
        student_id = int(input('Enter student ID for transcript: '))
        cursor.execute(
            '''
            SELECT student.name,
                   student.major,
                   course.department,
                   course.number,
                   course.credits,
                   section.semester,
                   enrollment.grade
            FROM enrollment
            INNER JOIN student ON student.id = enrollment.student_id
            INNER JOIN section ON section.id = enrollment.section_id
            INNER JOIN course ON course.id = section.course_id
            WHERE student.id = ?
            ''',
            (student_id,)
        )
        rows = cursor.fetchall()

        if len(rows) == 0:
            print('No transcript records found for that student ID.')
        else:
            print('\nTranscript')
            print('Student:', rows[0][0])
            print('Major:', rows[0][1])
            print('Courses:')
            for row in rows:
                print(f'{row[2]} {row[3]} | {row[4]} credits | {row[5]} | Grade: {row[6]}')

    else:
        print('Invalid choice.')

connection.close()
print('Done.')
