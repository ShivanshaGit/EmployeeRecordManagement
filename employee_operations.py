# ============================================
# employee_operations.py
# All CRUD functions for Employee Records
# ============================================

from db_connection import get_connection


# ──────────────────────────────────────────
# CREATE — Add a new employee
# ──────────────────────────────────────────
def add_employee():
    print("\n========== ADD NEW EMPLOYEE ==========")
    name        = input("Enter Name           : ").strip()
    department  = input("Enter Department     : ").strip()
    designation = input("Enter Designation    : ").strip()
    salary      = input("Enter Salary         : ").strip()
    email       = input("Enter Email          : ").strip()
    phone       = input("Enter Phone          : ").strip()
    joining_date = input("Enter Joining Date (YYYY-MM-DD) : ").strip()

    # Basic validation
    if not all([name, department, designation, salary, email, joining_date]):
        print("\n[ERROR] All fields except phone are required.")
        return

    try:
        salary = float(salary)
    except ValueError:
        print("\n[ERROR] Salary must be a number.")
        return

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO employees (name, department, designation, salary, email, phone, joining_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, department, designation, salary, email, phone, joining_date)
        cursor.execute(query, values)
        conn.commit()
        print(f"\n[SUCCESS] Employee '{name}' added with ID: {cursor.lastrowid}")
    except Exception as e:
        print(f"\n[ERROR] Could not add employee: {e}")
    finally:
        cursor.close()
        conn.close()


# ──────────────────────────────────────────
# READ — View all employees
# ──────────────────────────────────────────
def view_all_employees():
    print("\n========== ALL EMPLOYEES ==========")
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees ORDER BY emp_id")
        rows = cursor.fetchall()

        if not rows:
            print("No employees found in the database.")
            return

        print(f"\n{'ID':<6} {'Name':<20} {'Department':<15} {'Designation':<22} {'Salary':>10}  {'Email':<25} {'Phone':<15} {'Joining Date'}")
        print("-" * 125)
        for row in rows:
            print(f"{row[0]:<6} {row[1]:<20} {row[2]:<15} {row[3]:<22} {row[4]:>10.2f}  {row[5]:<25} {str(row[6]):<15} {row[7]}")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    finally:
        cursor.close()
        conn.close()


# ──────────────────────────────────────────
# READ — Search employee by ID or Name
# ──────────────────────────────────────────
def search_employee():
    print("\n========== SEARCH EMPLOYEE ==========")
    print("1. Search by Employee ID")
    print("2. Search by Name")
    choice = input("Enter choice (1/2): ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()
            cursor.execute("SELECT * FROM employees WHERE emp_id = %s", (emp_id,))
        elif choice == "2":
            name = input("Enter Name (or part of it): ").strip()
            cursor.execute("SELECT * FROM employees WHERE name LIKE %s", (f"%{name}%",))
        else:
            print("[ERROR] Invalid choice.")
            return

        rows = cursor.fetchall()
        if not rows:
            print("\nNo matching employee found.")
            return

        print(f"\n{'ID':<6} {'Name':<20} {'Department':<15} {'Designation':<22} {'Salary':>10}  {'Email':<25} {'Phone':<15} {'Joining Date'}")
        print("-" * 125)
        for row in rows:
            print(f"{row[0]:<6} {row[1]:<20} {row[2]:<15} {row[3]:<22} {row[4]:>10.2f}  {row[5]:<25} {str(row[6]):<15} {row[7]}")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    finally:
        cursor.close()
        conn.close()


# ──────────────────────────────────────────
# UPDATE — Edit employee details
# ──────────────────────────────────────────
def update_employee():
    print("\n========== UPDATE EMPLOYEE ==========")
    emp_id = input("Enter Employee ID to update: ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        # First check if employee exists
        cursor.execute("SELECT * FROM employees WHERE emp_id = %s", (emp_id,))
        emp = cursor.fetchone()
        if not emp:
            print(f"\n[ERROR] No employee found with ID {emp_id}.")
            return

        print(f"\nCurrent details for '{emp[1]}':")
        print(f"  Name: {emp[1]}  |  Dept: {emp[2]}  |  Designation: {emp[3]}  |  Salary: {emp[4]}")
        print("\nEnter new values (press Enter to keep current value):")

        name        = input(f"  Name        [{emp[1]}]: ").strip() or emp[1]
        department  = input(f"  Department  [{emp[2]}]: ").strip() or emp[2]
        designation = input(f"  Designation [{emp[3]}]: ").strip() or emp[3]
        salary_inp  = input(f"  Salary      [{emp[4]}]: ").strip()
        salary      = float(salary_inp) if salary_inp else emp[4]
        email       = input(f"  Email       [{emp[5]}]: ").strip() or emp[5]
        phone       = input(f"  Phone       [{emp[6]}]: ").strip() or emp[6]

        query = """
            UPDATE employees
            SET name=%s, department=%s, designation=%s, salary=%s, email=%s, phone=%s
            WHERE emp_id=%s
        """
        cursor.execute(query, (name, department, designation, salary, email, phone, emp_id))
        conn.commit()
        print(f"\n[SUCCESS] Employee ID {emp_id} updated successfully.")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    finally:
        cursor.close()
        conn.close()


# ──────────────────────────────────────────
# DELETE — Remove an employee
# ──────────────────────────────────────────
def delete_employee():
    print("\n========== DELETE EMPLOYEE ==========")
    emp_id = input("Enter Employee ID to delete: ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        # Check if exists
        cursor.execute("SELECT name FROM employees WHERE emp_id = %s", (emp_id,))
        emp = cursor.fetchone()
        if not emp:
            print(f"\n[ERROR] No employee found with ID {emp_id}.")
            return

        confirm = input(f"Are you sure you want to delete '{emp[0]}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Deletion cancelled.")
            return

        cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
        conn.commit()
        print(f"\n[SUCCESS] Employee '{emp[0]}' (ID: {emp_id}) deleted.")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    finally:
        cursor.close()
        conn.close()


# ──────────────────────────────────────────
# BONUS — View employees by department
# ──────────────────────────────────────────
def view_by_department():
    print("\n========== EMPLOYEES BY DEPARTMENT ==========")
    dept = input("Enter Department name: ").strip()

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE department LIKE %s ORDER BY name", (f"%{dept}%",))
        rows = cursor.fetchall()

        if not rows:
            print(f"\nNo employees found in department '{dept}'.")
            return

        print(f"\nFound {len(rows)} employee(s) in '{dept}':\n")
        print(f"{'ID':<6} {'Name':<20} {'Designation':<22} {'Salary':>10}  {'Email'}")
        print("-" * 80)
        for row in rows:
            print(f"{row[0]:<6} {row[1]:<20} {row[3]:<22} {row[4]:>10.2f}  {row[5]}")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    finally:
        cursor.close()
        conn.close()