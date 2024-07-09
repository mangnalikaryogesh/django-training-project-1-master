# Django school website.

## Overview
Django School Website is a comprehensive web application designed to cater for the needs of students, parents, and educators. It serves as a platform for showcasing the courses offered, providing information about the school, and offering engaging blog content for readers.



## Features
1. **Blog Features:**
   - **View Blog Posts:** Users can access a list of blog posts.
   - **View Post Detail:** Users can click on a specific post to view its details, including title, image, content, categories, and tags.
   - **Comment on Posts:** Users can comment on blog posts.
   - **Filter by Category:** Users can filter blog posts by category.
   - **Search Blog:** Users can search for specific blog posts using keywords.
   - **Filter by Tag:** Users can filter blog posts by tags.

2. **Courses Features:**
   - **View Courses:** Users can access a list of available courses and view its details, including name, image, duration, price, and related subject..
   - **View Subjects:** Users can access a list of subjects.
   - **Registration:** Users can register for courses.
   - **Authentication:** Users can log in and log out of their accounts.
   - **About Page:** Provides information about the website or organization.
   - **Teachers Page:** Provides information about the teachers.
   - **Contact Page:** Allows users to get in touch with the organization with a contact form designed to send emails to the admin.
   - **User Registration:** New users can register for an account.
   - **User Authentication:** Registered users can log in and log out of their accounts.

## Technologies Used
- Django
- Django CKEditor
- HTML/CSS/JavaScript
- Bootstrap
- AJAX
- JQuery
- SQLite (can easily be integrated with other database. eg MYSQL, postgreSQL)
- Template used has been included in the root folder in a directory named 'Templates used'

## Installation
1. Clone the repository: `git clone https://github.com/danielnjama/django-training-project-1.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Migrate database: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`
5. Create a superuser `python manage.py createsuperuser`
6. Access the admin dashboard and explore. view the different tables. Carry out the CRUD operations on this dashboard: `http://127.0.0.1:8000/admin`

## Usage
1. Navigate to the project directory.
2. Start the Django development server.
3. Access the web application in your preferred web browser.
4. Explore the different features such as viewing blog posts, registering for courses, etc.

OR
To practice along, download the templates under 'Templates used' and do your thing!

## Contributing
Contributions are welcome! Please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes with descriptive commit messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.

