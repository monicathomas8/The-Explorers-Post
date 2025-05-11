# The Explorer's Post 
Live link here: [The Explorer's Post](https://the-ep-9aae432261ad.herokuapp.com/)

**The Explorer's Post** is a dynamic web application designed to share and explore captivating travel stories.
Users can browse, share and manage personal travel experiences. Keeping cherished memories alive, while inspiring others to embark on their own adventures.
The Explorer's Post aims to:
-	Provide a platform for users to share travel stories.
- Allow visitors to explore stories written by other users.
- Foster a community of travel enthusiasts by enabling story sharing and feedback.
### Target Audience
- **Travel enthusiasts:** Those who wish to share their adventures.
- **Aspiring travellers:** People looking for inspiration for their next journey.
- **General audience:** Visitors interested in reading engaging travel stories.

![Snap Shot ](/static/images/pp4snapshot.jpg)

## Features
### Design
The application features a clean and modern interface with intuitive navigation. 
- **Landing Page**: An engaging home page with a responsive layout showcasing the purpose of the site.
![Landing Page](/static/images/landingpage.png)

- **Story List**: A grid display of travel stories with options to view.
![story list page](/static/images/storylist.png)

- **Story Detail**: A page that loads the full story with author and the date it was created on.
![Story detail page](/static/images/storydetail.png)
- **Create a Story**: A form for logged-in users to share travel experiences with a title, location, and rich text content.
![create a story page](/static/images/createstory.png)

- **My Collection**: A dashboard for logged-in users to manage their drafts and published stories.
![my collection page](/static/images/mycollection.png)

- **Contact Form**: A simple form for visitors to reach out to the admin team.
![contact us page](/static/images/contactform.png)

- **Authentication**: Users can register, log in, and log out to access personalized features.
![sign up page](/static/images/signup.png)
![sign in page](/static/images/signin.png)

- **Responsive Design**: Fully responsive for an optimal experience across devices. These include:

   1. Navbav - adaptive for different screen sizes, with a toogle button and dropdown menu.
    ![Navbar dropdown menu](/static/images/tooglenavmenu.png)
   2. Footer with social links and a message to state if the user is logged in or not. 
   ![footer ](/static/images/footer.png)
   3. Pop up messages
   ![pop up message](/static/images/signinmessage.png)
   4. Buttons 
   ![buttons](/static/images/signout.png)
   

### Colour Scheme and Imagery
The site uses white and gray coloured text and backgrounds for text containers. This is to keep the focus on the background images.
High-quality travel-related images are used across the site to enhance the user experience.
The images were sourced from [Pexels](https://www.pexels.com/search/iconic%20wonders/)
- [Japan](https://www.pexels.com/photo/landscape-photo-of-a-snowy-top-mountain-near-body-of-water-2451035/)
- [Great Wall of China](https://www.pexels.com/photo/sunrise-over-the-great-wall-of-china-29466142/)
- [Sphinx](https://www.pexels.com/photo/great-sphinx-of-giza-under-blue-starry-sky-262780/)
- [Colosseum](https://www.pexels.com/photo/colosseum-italy-1797161/)
- [Pyramids](https://www.pexels.com/photo/desert-landscape-with-dunes-and-pyramid-of-cheops-3772630)
- [Parthenon](https://www.pexels.com/photo/parthenon-in-greece-14500447/)
- [Sydney Opera House](https://www.pexels.com/photo/exterior-of-sydney-opera-house-in-late-evening-5707610/)
- [Aurora Borealis](https://www.pexels.com/photo/aurora-borealis-1933239/)
- [Eiffel Tower](https://www.pexels.com/photo/eiffel-tower-paris-painting-1796716/)
- [Stonehenge](https://www.pexels.com/photo/stonehenge-under-nimbostratus-clouds-161798/)
- [Empire State Building](https://www.pexels.com/photo/photo-of-high-rise-building-755050/)

## Planning 
During the planning and early design stages, I use a mind map to help create the foundations of the project. **UPDATE** 
I also drew out a simple plan on paper and used Balasmiq wireframes.
![mind map](/static/images/mindmap.png)
![First Draft](/static/images/pp4firstdraft.png)
![Wireframe](/static/images/wireframePP4.png)

Reasoning behind the layout:  
- Navbar - for quick easy links. 
- Title - to explain the site to a user, with a fun descriptive paragraph. 
- Buttons -  for easy links to the main content. 
- Footer - for easy links and a neat looking site.


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
- W3C Validator (HTML and CSS validation)
- PEP8 (Python code validation)
- Favicon.io  [Favicon Generator](https://favicon.io/)

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
- Full details of the [ERDs file](ERD.md)

### Data Modelling
- Users: Manage own stories (CRUD).
- Stories: Store content, authorship, and status.
- Contact Form: Store user inquiries.

### User roles
#### Visitor
- View/Read published stories
- Contact admin via the form
#### Registered User
- Create, read, edit, and delete their stories
- Manage their drafts and published stories

## Testing

### Manual Testing
Behavior Driven Development was used.
- Full details are here [BDD file](BDD.md)

### Validator Testing
- **HTML:** Validated using W3C Validator.
![html](/static/images/Screenshot154502.png)
-	**CSS:** Validated using W3C CSS Validator.
![CSS](/static/images/Screenshot154354.png)
-	**Python:** Checked for PEP8 compliance.
![python](/static/images/Screenshot154927.png)
- **Lighthouse** 
![Lighthouse results](/static/images/lighthouse.png)

## Bugs 
### Resolved
1. Navigation Links Not Working: Clicking on navigation links did not navigate to the correct pages.
**Solution:** Updated href attributes in the navigation bar to point to the correct URLs.
2. Deployment to Heroku failed:  Deployment to Heroku failed due to a typo in the Procfile (web: gunicorn explorer_post.wsgi:application was missing the s in _posts).
**Solution:** Corrected the typo in the Procfile.
3. Removed Unnecessary Test Code: Test code in views.py and urls.py was cluttering the project setup.
**Solution:** Removed the unused test code.
4. Navbar drop down menu: I added custom CSS to the bootstrap navbar, this caused the drop down menu to lose its background colour to make it visible. **Solution:** Removed my custom CSS. 
5. Excrement code line: I had a line of code in my story model that I didn't use. **Solution:** I ran a search to see where and if it was being used. it was only in the model and two migrations. so I removed the code. 
6. **NEW BUG FOUND AFTER DEPLOYMENT** Within the story detail page, the html tags were displaying within the posts. **Solution:** when fetching the story detail, I added "content|truncatewords:20|safe" to stop the html tags from displaying. 

## Deployment
This project was deployed locally first and then hosted on Heroku. Follow these steps to set up and deploy the project: [Deployment file](/DEPLOYMENT.md)

## Summary and Future Features

Throughout the development of *The Explorer's Post*, I have gained valuable insights into project structuring, feature planning, and future enhancements. Reflecting on my work, there are several areas I would approach differently and ideas I’d like to implement in the future:

1. **Renaming Apps for Clarity**:  
   With my growing understanding, I realize that naming the apps more intuitively would enhance the project’s readability and organization.  
   - The `core` app, which currently handles the homepage, could be renamed to **home**, as it better represents its functionality.  
   - The `stories` app could be renamed to **posts**, avoiding confusion with the concept of "user stories" and better reflecting its purpose of handling user-submitted posts.  
   - Additionally, the project name itself could of been called `core`, ensuring that the app structure aligns more closely with best practices.

2. **Future Features and Enhancements**:  
   While this version of the project fulfills the primary objectives, I have identified several features for future development (each item has a user story in the project board):  
   - **Liking Stories**: Enabling users to like stories to show appreciation.  
   - **Leaving Comments**: Allowing users to engage with stories by leaving comments.  
   - **Adding Photos to Stories**: Users could upload images to accompany their stories.  
   - **User Profiles**: Creating profiles for registered users to manage their submissions and preferences.  
   - **Searching Stories by Location**: Implementing a search feature to filter stories by location.

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

Live link here: [The Explorer's Post](https://the-ep-9aae432261ad.herokuapp.com/)