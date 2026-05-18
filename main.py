# ============================================
# main.py
# Employee Record Management System
# Entry point — run this file to start the app
# ============================================

from employee_operations import (
    add_employee,
    view_all_employees,
    search_employee,
    update_employee,
    delete_employee,
    view_by_department
)


def print_menu():
    print("\n" + "=" * 45)
    print("   EMPLOYEE RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add New Employee")
    print("  2. View All Employees")
    print("  3. Search Employee")
    print("  4. Update Employee Details")
    print("  5. Delete Employee")
    print("  6. View Employees by Department")
    print("  0. Exit")
    print("=" * 45)


def main():
    print("\nWelcome to Employee Record Management System")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            view_by_department()
        elif choice == "0":
            print("\nThank you! Exiting the system. Goodbye!\n")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()