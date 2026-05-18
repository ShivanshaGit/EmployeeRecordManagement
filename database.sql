CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;
CREATE TABLE IF NOT EXISTS employees (
    emp_id        INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    department    VARCHAR(100) NOT NULL,
    designation   VARCHAR(100) NOT NULL,
    salary        DECIMAL(10, 2) NOT NULL,
    email         VARCHAR(150) UNIQUE NOT NULL,
    phone         VARCHAR(15),
    joining_date  DATE NOT NULL
);
INSERT INTO employees (name, department, designation, salary, email, phone, joining_date) VALUES
('Rahul Sharma',   'Engineering',  'Software Developer',  55000.00, 'rahul@example.com',  '9876543210', '2023-01-15'),
('Priya Singh',    'HR',           'HR Manager',          48000.00, 'priya@example.com',  '9876543211', '2022-06-01'),
('Amit Kumar',     'Finance',      'Accountant',          42000.00, 'amit@example.com',   '9876543212', '2023-03-20'),
('Neha Gupta',     'Engineering',  'QA Engineer',         50000.00, 'neha@example.com',   '9876543213', '2021-11-10'),
('Vikram Patel',   'Marketing',    'Marketing Executive', 38000.00, 'vikram@example.com', '9876543214', '2024-01-05');

SELECT 'Database and table created successfully!' AS Status;
SELECT * FROM employees;