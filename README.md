# The Explore's Post 

## About
**The Explorer's Post** is a dynamic web application designed to share and explore captivating travel stories.
Users can browse, share, manage personal travel experiences. Keeping cherished memories alive, while inspiring others to embark on their own adventures.

<img>
<img>

## User Experience Design
### Strategy
The Explorer's Post aims to:
-	Provide a platform for users to share travel stories.
- Allow visitors to explore stories written by other users.
- Foster a community of travel enthusiasts by enabling story sharing and feedback.
### Target Audience
- **Travel enthusiasts:** Those who wish to share their adventures.
- **Aspiring travellers:** People looking for inspiration for their next journey.
- **General audience:** Visitors interested in reading engaging travel stories.

## Technologies Used
- **Languages**: Python, HTML, CSS, JavaScript
- **Frameworks and Libraries**: Django, Bootstrap
- **Other Libraries**:
  - `django-crispy-forms`: Simplified form styling.
  - `django-summernote`: Rich text editor for story content.
  - `whitenoise`: Static file management in production.
- **Database**: SQLite, PostgreSQL
- **Hosting**: Heroku and GitHub

## Other Tools
- Heroku (Deployment)
- GitPod (Development environment)
- GitHub (Version control)
- W3C Validator (HTML validation)
- Jigsaw Validator (CSS validation)
- PEP8 (Python code validation)

<img src="/static/images/Screenshot154354.png">
<img src="/static/images/Screenshot154502.png">
<img src="/static/images/Screenshot154927.png">

## Features
- **Landing Page**: An engaging home page with a responsive layout showcasing the purpose of the site.
- **Story List**: A grid display of travel stories with options to view, edit, or delete (edit and delete for logged-in users, of personal stories).
- **Create a Story**: A form to share travel experiences with a title, location, and rich text content.
- **My Collection**: A dashboard for logged-in users to manage their drafts and published stories.
- **Contact Form**: A simple form for visitors to reach out to the admin team.
- **Authentication**: Users can register, log in, and log out to access personalized features.
- **Responsive Design**: Fully responsive for an optimal experience across devices.




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