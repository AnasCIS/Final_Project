import tkinter as tk
from tkinter import messagebox
import pickle
import os


class Employee:
    """Simple Employee class for demonstration."""

    def __init__(self, name, employee_id, department, job_title, basic_salary):
        # Initialize employee attributes
        self.name = name  # Full name of the employee
        self.employee_id = employee_id  # Unique ID for each employee
        self.department = department  # Department where the employee works
        self.job_title = job_title  # Job title within the department
        self.basic_salary = basic_salary  # Monthly or yearly salary


class EmployeeForm:
    """GUI for managing Employee data."""

    def __init__(self, data_layers):
        self.data_layer = data_layers
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Employee Management")

        # Set up the GUI layout with labels and entry widgets for employee details
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        tk.Label(self.root, text="Employee ID:").grid(row=1, column=0)
        tk.Label(self.root, text="Department:").grid(row=2, column=0)
        tk.Label(self.root, text="Job Title:").grid(row=3, column=0)
        tk.Label(self.root, text="Basic Salary:").grid(row=4, column=0)

        # Entry widgets allow user input for each attribute of an employee
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)
        self.employee_id_entry = tk.Entry(self.root)
        self.employee_id_entry.grid(row=1, column=1)
        self.department_entry = tk.Entry(self.root)
        self.department_entry.grid(row=2, column=1)
        self.job_title_entry = tk.Entry(self.root)
        self.job_title_entry.grid(row=3, column=1)
        self.basic_salary_entry = tk.Entry(self.root)
        self.basic_salary_entry.grid(row=4, column=1)

        # Buttons for performing operations like save, delete, and show all employees
        tk.Button(self.root, text="Add/Modify Employee", command=self.save_employee).grid(row=5, column=1)
        tk.Button(self.root, text="Delete Employee", command=self.delete_employee).grid(row=6, column=1)
        tk.Button(self.root, text="Show All Employees", command=self.show_employees).grid(row=7, column=1)

        self.root.mainloop()

    def save_employee(self):
        """Save or modify an employee's details."""
        # Retrieve values from entry widgets
        name = self.name_entry.get()
        employee_id = self.employee_id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = self.basic_salary_entry.get()

        # Check if employee exists and confirm update or add new
        if employee_id in self.data_layer.employees:
            response = messagebox.askyesno("Update", "Employee exists. Update details?")
            if response:
                self.data_layer.employees[employee_id] = Employee(name, employee_id, department, job_title,
                                                                  basic_salary)
                messagebox.showinfo("Updated", "Employee updated successfully.")
        else:
            self.data_layer.employees[employee_id] = Employee(name, employee_id, department, job_title, basic_salary)
            messagebox.showinfo("Added", "Employee added successfully.")
        self.data_layer.write_employees_to_file()

    def delete_employee(self):
        """Delete an employee's details based on ID."""
        employee_id = self.employee_id_entry.get()
        if employee_id in self.data_layer.employees:
            del self.data_layer.employees[employee_id]
            messagebox.showinfo("Deleted", "Employee deleted successfully.")
            self.data_layer.write_employees_to_file()
        else:
            messagebox.showerror("Error", "Employee not found.")

    def show_employees(self):
        """Display all employees in a new window with a list."""
        new_window = tk.Toplevel(self.root)
        new_window.title("All Employees")
        listbox = tk.Listbox(new_window, width=50, height=20)
        listbox.pack(padx=20, pady=20)
        for emp_id, employee in self.data_layer.employees.items():
            listbox.insert(tk.END,
                           f"ID: {emp_id}, Name: {employee.name}, Dept: {employee.department}, Title: {employee.job_title}, Salary: ${employee.basic_salary}")


class DataLayer:
    """Handle read and write operations for employee data."""

    def __init__(self, filenames):
        self.filename = filenames
        self.employees = self.read_employees()

    def read_employees(self):
        """Load employee data from a file."""
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)

    def write_employees_to_file(self):
        """Save employee data to a file."""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.employees, f)


# Main execution
filename = "employees.pkl"
data_layer = DataLayer(filename)
employee_form = EmployeeForm(data_layer)
