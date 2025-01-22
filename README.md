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
Behavior Driven Development was used.
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

This project was deployed locally first and then hosted on Heroku. Follow these steps to set up and deploy the project:

### Local Deployment

1. **Fork or Clone the Repository**:
   You can view or clone the repository directly from the following link:  
   [The Explorer's Post GitHub Repository](https://github.com/monicathomas8/The-Explorers-Post.git)

2. **Install Dependencies**:
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root of your project and add the following variables:
     ```
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
     ```

4. **Run Migrations**:
   - Apply migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

5. **Collect Static Files**:
   - Collect static files locally to ensure they are ready for production:
     ```bash
     python manage.py collectstatic
     ```
   - This gathers all CSS, JavaScript, and image files into the `staticfiles` directory.

6. **Run the Project Locally**:
   - Start the development server:
     ```bash
     python manage.py runserver
     ```

---

### Heroku Deployment

1. **Push Code to GitHub**:
   - Ensure all changes are committed and pushed to GitHub:
     ```bash
     git add .
     git commit -m "Prepare for Heroku deployment"
     git push origin main
     ```

2. **Log In to Heroku**:
   - Log in to your Heroku account:
     ```bash
     heroku login
     ```

3. **Create a New Heroku App**:
   - Create a new app on Heroku:
     ```bash
     heroku create <your-app-name>
     ```

4. **Set Up Environment Variables**:
   - Go to the Heroku dashboard for your app.
   - Under the **Settings** tab, click **Config Vars** and add:
     - **Key:** `PORT` | **Value:** `8000`
     - **Key:** `SECRET_KEY` | **Value:** your_secret_key
     - Add your database URL if using a PostgreSQL database.

5. **Set Buildpacks**:
   - Add Python as the first buildpack.

6. **Connect to GitHub**:
   - In the Heroku dashboard, go to the **Deploy** tab.
   - Under **Deployment Method**, select **GitHub**.
   - Connect your GitHub repository.

7. **Deploy the Application**:
   - Choose a deployment method:
     - **Automatic Deployment**: Automatically deploy on new commits to the main branch.
     - **Manual Deployment**: Click **Deploy Branch** to deploy manually.

8. **Access the Application**:
   - Once deployment is complete, open the app using the URL:

## Summary

Throughout the development of *The Explorer's Post*, I have gained valuable insights into project structuring, feature planning, and future enhancements. Reflecting on my work, there are several areas I would approach differently and ideas I’d like to implement in the future:

1. **Renaming Apps for Clarity**:  
   With my growing understanding, I realize that naming the apps more intuitively would enhance the project’s readability and organization.  
   - The `core` app, which currently handles the homepage, could be renamed to **home**, as it better represents its functionality.  
   - The `stories` app could be renamed to **posts**, avoiding confusion with the concept of "user stories" and better reflecting its purpose of handling user-submitted posts.  
   - Additionally, the project name itself could replace `core`, ensuring that the app structure aligns more closely with best practices.

2. **Future Features and Enhancements**:  
   While this version of the project fulfills the primary objectives, I have identified several features for future development:  
   - **Liking Stories**: Enabling users to like stories to show appreciation.  
   - **Leaving Comments**: Allowing users to engage with stories by leaving comments.  
   - **Adding Photos to Stories**: Users could upload images to accompany their stories.  
   - **User Profiles**: Creating profiles for registered users to manage their submissions and preferences.  
   - **Searching Stories by Location**: Implementing a search feature to filter stories by destination.

3. **Visual Enhancements**:  
   To make the landing page more visually appealing, I would like to redesign it with a photo collage layout. Stacking photos in a creative, overlapping style would immediately capture users' attention and highlight the vibrant stories shared on the platform.

These future improvements reflect my commitment to enhancing both functionality and user experience as I continue to grow my skills and understanding of web development.

## Credits

### Content
- This project was designed and developed by **Monica Thomas** as part of the Code Institute Full-Stack Development Diploma.

### Tutorials and Resources
- **Tech With Tim**: [Django Beginner Tutorial](https://youtu.be/sm1mokevMWk?si=x647nUCIvSpyD2lU)  
- **Programming with Mosh**: [Django Full Course](https://youtu.be/rHux0gMZ3Eg?si=SBKdrSZ061fcF1YV)  
- **Bootstrap Documentation**: Used for styling components and understanding responsive design.
- **Resize Pixel**: [Resizing images](https://www.resizepixel.com/)
- **Audible books**: Clean Agile, Clean Code, The Clean Coder all by Robert C. Martin


### Acknowledgements
- Special thanks to the Code Institute community and my mentor Iuliia Konovalova for support and guidance throughout this project.

