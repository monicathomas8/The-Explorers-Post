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
<img src="/static/images/mindmap.png">
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

## Features

### Design
The application features a clean and modern interface with intuitive navigation.
- **Landing Page**: An engaging home page with a responsive layout showcasing the purpose of the site.
- **Story List**: A grid display of travel stories with options to view, edit, or delete (edit and delete for logged-in users, of personal stories).
- **Create a Story**: A form to share travel experiences with a title, location, and rich text content.
- **My Collection**: A dashboard for logged-in users to manage their drafts and published stories.
- **Contact Form**: A simple form for visitors to reach out to the admin team.
- **Authentication**: Users can register, log in, and log out to access personalized features.
- **Responsive Design**: Fully responsive for an optimal experience across devices.

### Colour Scheme
The site uses  white and gray coloured text and backgrounds, to keep the focus on the background images.

### Imagery
High-quality travel-related images are used across the site to enhance the user experience.
The images were sourced from <a href="https://www.pexels.com/search/iconic%20wonders/">Pexels</a>
- <a href="https://www.pexels.com/photo/landscape-photo-of-a-snowy-top-mountain-near-body-of-water-2451035/ ">Japan</a>
- <a href="https://www.pexels.com/photo/sunrise-over-the-great-wall-of-china-29466142/">Great Wall of China</a>
- <a href="https://www.pexels.com/photo/great-sphinx-of-giza-under-blue-starry-sky-262780/">Sphinx</a>
- <a href="https://www.pexels.com/photo/colosseum-italy-1797161/">Colosseum</a>
- <a href="https://www.pexels.com/photo/desert-landscape-with-dunes-and-pyramid-of-cheops-3772630/">Pyramids</a>
- <a href="https://www.pexels.com/photo/parthenon-in-greece-14500447/">Parthenon</a>
- <a href="https://www.pexels.com/photo/exterior-of-sydney-opera-house-in-late-evening-5707610/">Sydney Opera House</a>
- <a href="https://www.pexels.com/photo/aurora-borealis-1933239/">Aurora Borealis</a>
- <a href="https://www.pexels.com/photo/eiffel-tower-paris-painting-1796716/">Eiffel Tower</a>
- <a href="https://www.pexels.com/photo/stonehenge-under-nimbostratus-clouds-161798/">Stonehenge</a>
- <a href="https://www.pexels.com/photo/photo-of-high-rise-building-755050/">Empire State Building</a>

## Information Architecture

### Project Structure
<pre>
The-Explorers-Post/
├── explores_posts   # Project
├── core/            # Core app (landing page, contact form) 
├── stories/         # Stories app (create and read stories)
├── users/           # Users app (read, edit and delete personal stories)
├── templates/       # HTML templates
├── static/          # CSS and images
├── manage.py        # Django management script
└── requirements.txt # Project dependencies 
</pre>

### Database
The database is structured to manage users, stories, and contact form submissions.

### Entity-Relationship Diagram
A detailed ERD maps the relationships between users, stories, and contact forms.
- Full details of the ERDs <a href="/ERD.md">ERD.md</a>

### Data Modelling
- Users: Manage own stories (CRUD).
- Stories: Store content, authorship, and status.
- Contact Form: Store user inquiries.

### User roles
#### Visitor
- View/Read published stories
- Contact admin via the form
#### Registered User
- Create, edit, and delete their stories
- Manage drafts and published stories

## Testing

### Manual Testing
Behavior Driven Development was used. You can find the user story and BDD detsils here
- Full details here <a href="/BDD.md">BDD.md</a>

### Validator Testing
- **HTML:** Validated using W3C Validator.
-	**CSS:** Validated using W3C CSS Validator.
-	**Python:** Checked for PEP8 compliance.

<img src="/static/images/Screenshot154354.png">
<img src="/static/images/Screenshot154502.png">
<img src="/static/images/Screenshot154927.png">

## Bugs 
### Resolved
1. Navigation Links Not Working: Clicking on navigation links did not navigate to the correct pages.
**Solution:** Updated href attributes in the navigation bar to point to the correct URLs.
2. Missing 's' in _posts in the Procfile Issue: Deployment to Heroku failed due to a typo in the Procfile (web: gunicorn explorer_post.wsgi:application was missing the s in _posts).
**Solution:** Corrected the typo in the Procfile.
3. Removed Unnecessary Test Code: Test code in views.py and urls.py was cluttering the project setup.
**Solution:** Removed the unused test code.
4. Navbar drop down menu: I added custom CSS to the bootstrap navbar, this caused the drop down menu to lose its background colour to make it visible. **Solution:** Removed my custom CSS. 
5. Excrement code line: I had a line of code in my story model that I didn't use. **Solution:** I ran a search to see where and if it was being used. it was only in the model and two migrations. so I removed the code. 

## Deployment



