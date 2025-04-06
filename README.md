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

### Usage
1. user registration

	url ``` http://127.0.0.1:8000/users/register/ ```

	token ``` 127c8ad3f486fddd7c21e818b8dd63414a98eb18 ```

	http request ``` POST ```

	json data
```
	{
		"username" : "test",
		"email" : "test@example.com",
		"password" : "userpasstest"
	}

	{
		"username" : "test2",
		"email" : "test2@example.com",
		"password": "user2passtest"
	}

```

2. user login

	url ``` http://127.0.0.1:8000/users/login/ ```

	http request ``` POST ```

	json data
```
	{
		"username" : "test",
		"password" : "userpasstest"
	}
	{
		"username" : "test2",
		"password": "user2passtest"
	}
``` 

3. Create student and/or staff profile

	url ``` http://127.0.0.1:8000/users/teachers/ ```

	http request ``` POST ```

	json data
```
	{
		"name" : "John Doe",
		"email" : "test@example.com",
		"profile": null,
		"user": 1
	}

	{
		"name" : "Jane Doe",
		"email" : "test2@example.com",
		"profile": null,
		"user": 2
	}
```

4. Create course

	url ``` http://127.0.0.1:8000/program/course/ ```

	http request ``` POST ```

	json data
```
	{
		"name": "mathematics",
		"coursecontent": "This is the course content"
	}
```

5. Enroll

	url ``` http://127.0.0.1:8000/courses/enroll/ ```

	http request ``` POST ```

	json data
```
	{
		"student": 1,
		"course": 3
	}
```

6. List enrolled courses

	url ``` http://127.0.0.1:8000/courses/enrolled ```

	http request ``` GET ```

### Contact

For any questions or suggestions, please open an issue or contact the project maintainer at aremzy2018@gmail.com.
