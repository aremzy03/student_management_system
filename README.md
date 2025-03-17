# Student Management System

This project is a simple Student Management System that allows you to manage student records, including adding, updating, and deleting student information. Courses including adding, updating, enrolling and deleting. And finally managing the students attendance data.

## Setup Instructions

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the repository:**

	```bash
	git clone https://github.com/yourusername/student_management_system.git
	cd student_management_system
	```

2. **Create a virtual environment:**

	```bash
	python3 -m venv venv
	```

3. **Activate the virtual environment:**


	- On macOS/Linux:

	  ```bash
	  source venv/bin/activate
	  ```
4. **Create new project**
	- On Linux:
		```
		django-admin startproject student_management_system
		```
5. **Creating applications**
	- On Linux:
		```
		./manage.py startapp <Appname>
		```
6. **Creating migrations and migrating**
		
		```
		./manage.py makemigratons
		./manage.py migrate
		```

7. **Running the Server**
		
		```
		./manage.py runserver
		```		
### Contact

For any questions or suggestions, please open an issue or contact the project maintainer at aremzy2018@gmail.com.
