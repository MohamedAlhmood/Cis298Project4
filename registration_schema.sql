PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department TEXT,
    number TEXT,
    credits INTEGER,
    description TEXT
);

CREATE TABLE IF NOT EXISTS faculty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS section (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    faculty_id INTEGER,
    semester TEXT,
    day TEXT,
    time TEXT,
    FOREIGN KEY (course_id) REFERENCES course(id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
);

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    major TEXT
);

CREATE TABLE IF NOT EXISTS enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    section_id INTEGER,
    grade TEXT,
    FOREIGN KEY (student_id) REFERENCES student(id),
    FOREIGN KEY (section_id) REFERENCES section(id)
);
