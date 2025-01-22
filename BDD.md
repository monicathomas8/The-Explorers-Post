## BDD Tests for User Story: Easy to use website

**User Story:**  
As a user, I want the site to be easy to view and read, so I can use and view the website with ease.

### Acceptance Criteria:
- Navigation bar with workable links.
- Uniform format across all pages.
- Easy-to-read fonts.
- Vibrant photos.

### BDD Scenarios:

#### Scenario 1: Navigation Bar with Workable Links
- **Given** I am on any page of the website  
- **When** I click a link in the navigation bar  
- **Then** I am taken to the correct page  

#### Scenario 2: Uniform Format Across All Pages
- **Given** I visit any page on the website  
- **When** I compare the layout and styling  
- **Then** I see a consistent format across all pages  

#### Scenario 3: Easy-to-Read Fonts
- **Given** I am on any page of the website  
- **When** I read the text  
- **Then** The fonts are clear and easy to read  

#### Scenario 4: Vibrant Photos
- **Given** I am browsing the website  
- **When** I view the photos  
- **Then** The photos are vibrant and visually appealing  

## BDD Tests for User Story: Browse Travel Stories

**User Story:**  
As a user, I want to browse travel stories about ancient wonders and iconic destinations so that I can find inspiration for my next adventure.

### Acceptance Criteria:
- Users can view all submitted travel stories on the homepage (Read).
- Each story includes the title, author’s name, and a brief preview (Read).

### BDD Scenarios:

#### Scenario 1: View All Travel Stories via the Homepage
- **Given** I am on the homepage  
- **When** I click a button  
- **Then** I see all submitted travel stories listed on a story list page.

#### Scenario 2: Story Details
- **Given** I am on the story list page 
- **When** I look at a travel story preview  
- **Then** I can see the title, destination type, author’s name, and a brief preview of the content  

## BDD Tests for User Story: Review and Approve User-Submitted Stories

**User Story:**  
As an admin, I want to review and approve user-submitted stories so I can maintain content quality.

### Acceptance Criteria:
- Admins can view all submitted stories in a pending review section (Read).
- Admins can approve or reject stories, and only approved stories appear publicly (Update/Delete).

### BDD Scenarios:

#### Scenario 1: View Pending Stories
- **Given** I am logged in as an admin  
- **When** I navigate to the pending review section  
- **Then** I see a list of all user-submitted stories awaiting approval  

#### Scenario 2: Approve a Story
- **Given** I am logged in as an admin  
- **When** I approve a user-submitted story  
- **Then** The story is moved from the pending review section to the story list page 

#### Scenario 3: Reject a Story
- **Given** I am logged in as an admin  
- **When** I reject a user-submitted story  
- **Then** The story is removed from the pending review section and does not appear publicly  

## BDD Tests for User Story: Sign Up

**User Story:**  
As a user, I want to sign up so I can share travel stories.

### Acceptance Criteria:
- Users can sign up to create an account.

### BDD Scenarios:

#### Scenario 1: Successful Sign-Up
- **Given** I am on the sign-up page  
- **When** I enter valid information (username, email, password) and submit the form  
- **Then** My account is created, and I am redirected to the homepage or create a story page

#### Scenario 2: Sign-Up with Missing Information
- **Given** I am on the sign-up page  
- **When** I submit the form with missing or invalid fields  
- **Then** I see error messages indicating which fields need to be corrected  

#### Scenario 3: Sign-Up with Existing Email or Username
- **Given** I am on the sign-up page  
- **When** I attempt to sign up using an email or username that is already taken  
- **Then** I see an error message indicating the conflict and prompting me to choose a different email or username  

## BDD Tests for User Story: Share My Experience

**User Story:**  
As a registered user, I want to share my experience so that others can learn from my journey.

### Acceptance Criteria:
- Registered users can submit a travel story.
- The story is saved in the database and appears under the appropriate category after admin approval (Read).

### BDD Scenarios:

#### Scenario 1: Submit a Travel Story
- **Given** I am logged in as a registered user  
- **When** I navigate to the create a story page and fill in all required fields  
- **Then** My story is submitted for review and saved in the database  

#### Scenario 2: Story Saved Under the Appropriate Category
- **Given** My story has been submitted and is awaiting admin approval  
- **When** The admin approves my story  
- **Then** The story is displayed publicly on the story list page 

#### Scenario 3: Story Not Visible Without Approval
- **Given** I have submitted a travel story  
- **When** The admin has not yet approved the story  
- **Then** The story does not appear on the story list page, but is visible on the my collection page under draft stories

## BDD Tests for User Story: View My Stories

**User Story:**  
As a registered user, I want to view my stories so that I can review my stories and see them all in one place.

### Acceptance Criteria:
- Users can view all their own stories in one place.

### BDD Scenarios:

#### Scenario 1: View Personal Stories
- **Given** I am logged in as a registered user  
- **When** I navigate to the my collection page  
- **Then** I see a list of all the stories I have submitted  

#### Scenario 2: Display Story Details
- **Given** I am on the "My Stories" page  
- **When** I view the list of stories  
- **Then** Each story displays its title, status (e.g., pending or approved), and a brief preview  

#### Scenario 3: No Stories Submitted
- **Given** I am logged in as a registered user  
- **When** I navigate to the "My Stories" page and I have not submitted any stories  
- **Then** I see a message indicating that I have not submitted any stories yet  

## BDD Tests for User Story: Update a Story

**User Story:**  
As a registered user, I want to update my story so that I can correct or add new details.

### Acceptance Criteria:
- Users can edit their previously submitted stories through their dashboard (Update).
- The updated content reflects immediately in the appropriate category (Read).
- A confirmation message is displayed.

### BDD Scenarios:

#### Scenario 1: Edit a Submitted Story
- **Given** I am logged in as a registered user  
- **When** I navigate to my collection and select a story to edit  
- **Then** I am taken to a story editing form where I can update the details  

#### Scenario 2: Save Updated Story
- **Given** I have updated a story using the editing form  
- **When** I submit the form with valid changes  
- **Then** The story is updated in the database and reflects immediately under the appropriate category  

#### Scenario 3: Confirmation Message
- **Given** I have successfully updated a story  
- **When** The changes are saved  
- **Then** I see a confirmation message indicating that the story has been updated successfully  

## BDD Tests for User Story: Delete a Story

**User Story:**  
As a registered user, I want to delete my story so that I can remove it if I no longer want it displayed.

### Acceptance Criteria:
- Users can delete their stories via a "Delete" button in their dashboard (Delete).
- Deleted stories are removed from the database and are no longer visible on the site (Read).
- A confirmation message is displayed with a warning.

### BDD Scenarios:

#### Scenario 1: Delete a Story
- **Given** I am logged in as a registered user  
- **When** I navigate to my collection and click the "Delete" button for a story  
- **Then** I see a confirmation prompt asking if I want to proceed  

#### Scenario 2: Confirm Deletion
- **Given** I am in the confirmation prompt after clicking the "Delete" button  
- **When** I confirm the deletion  
- **Then** The story is removed from the database and no longer visible on the site  

#### Scenario 3: Cancel Deletion
- **Given** I am in the confirmation prompt after clicking the "Delete" button  
- **When** I cancel the deletion  
- **Then** The story remains in the database and visible on the site  

#### Scenario 4: Display Confirmation Message
- **Given** I have successfully deleted a story  
- **When** The deletion is processed  
- **Then** I see a confirmation message stating that the story was deleted successfully  
## BDD Tests for User Story: Contact Form

**User Story:**  
As a visitor, I can get in touch so I can ask questions and share feedback.

### Acceptance Criteria:
- Create a form for all users to be able to see and fill out.
- Have a confirmation message after the form has been submitted.

### BDD Scenarios:

#### Scenario 1: Display the Contact Form
- **Given** I am on the contact page  
- **When** I visit the page  
- **Then** I see a form with fields for name, email, and message  

#### Scenario 2: Submit the Contact Form with Valid Inputs
- **Given** I have filled out the contact form with valid inputs  
- **When** I submit the form  
- **Then** The form is successfully submitted, and I see a confirmation message  

#### Scenario 3: Submit the Contact Form with Invalid Inputs
- **Given** I am filling out the contact form  
- **When** I leave any required field empty or enter invalid data  
- **Then** I see an error message prompting me to correct the invalid fields  

#### Scenario 4: Confirmation After Submission
- **Given** I have successfully submitted the contact form  
- **When** The form submission is processed  
- **Then** I see a confirmation message thanking me for my message  
