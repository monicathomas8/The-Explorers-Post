# The Explore's Post 

## Overview
**The Explorer's Post** is a dynamic web application designed to share and explore captivating travel stories.
Users can browse, share, manage personal travel experiences. Keeping cherished memories alive, while inspiring others to embark on their own adventures.

## Features
- **Landing Page**: An engaging home page with a responsive layout showcasing the purpose of the site.
- **Story List**: A grid display of travel stories with options to view, edit, or delete (edit and delete for logged-in users, of personal stories).
- **Create a Story**: A form to share travel experiences with a title, location, and rich text content.
- **My Collection**: A dashboard for logged-in users to manage their drafts and published stories.
- **Contact Form**: A simple form for visitors to reach out to the admin team.
- **Authentication**: Users can register, log in, and log out to access personalized features.
- **Responsive Design**: Fully responsive for an optimal experience across devices.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS, Bootstrap
- **Database**: PostgreSQL
- **Hosting**: Deployed on Heroku and GitHub
- **Other Libraries**:
  - `django-crispy-forms`: Simplified form styling.
  - `django-summernote`: Rich text editor for story content.
  - `whitenoise`: Static file management in production.

## Project Structure

<pre>
The-Explorers-Post/
├── core/            # Core app (landing page, contact form) 
├── stories/         # Stories app (create and read stories)
├── users/           # Users app (read, edit and delete personal stories)
├── templates/       # HTML templates
├── static/          # CSS and images
├── manage.py        # Django management script
└── requirements.txt # Project dependencies 
</pre>

## User roles
### Visitor
- View/Read published stories
- Contact admin via the form
### Registered User
- Create, edit, and delete their stories
- Manage drafts and published stories






## Resources

https://www.pexels.com/photo/landscape-photo-of-a-snowy-top-mountain-near-body-of-water-2451035/ - japan