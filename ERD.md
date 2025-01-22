
<h4>User Table</h4>
<table>
  <tr>
    <th>Field Type</th>
    <th>Field Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>AutoField</td>
    <td>id</td>
    <td>Primary Key</td>
  </tr>
  <tr>
    <td>CharField</td>
    <td>username</td>
    <td>Unique, User's name</td>
  </tr>
  <tr>
    <td>EmailField</td>
    <td>email</td>
    <td>User's email address</td>
  </tr>
  <tr>
    <td>CharField</td>
    <td>password</td>
    <td>User's password</td>
  </tr>
</table>

<h4>Story Table</h4>
<table>
  <tr>
    <th>Field Type</th>
    <th>Field Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>AutoField</td>
    <td>id</td>
    <td>Primary Key</td>
  </tr>
  <tr>
    <td>CharField</td>
    <td>title</td>
    <td>Title of the story</td>
  </tr>
  <tr>
    <td>SlugField</td>
    <td>slug</td>
    <td>Unique URL-friendly identifier</td>
  </tr>
  <tr>
    <td>TextField</td>
    <td>content</td>
    <td>Content of the story</td>
  </tr>
  <tr>
    <td>ForeignKey</td>
    <td>author</td>
    <td>Linked to User model</td>
  </tr>
  <tr>
    <td>IntegerField</td>
    <td>status</td>
    <td>Story status (e.g., Draft)</td>
  </tr>
  <tr>
    <td>DateTimeField</td>
    <td>created_on</td>
    <td>Timestamp of creation</td>
  </tr>
</table>

<h4>ContactForm Table</h4>
<table>
  <tr>
    <th>Field Type</th>
    <th>Field Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>AutoField</td>
    <td>id</td>
    <td>Primary Key</td>
  </tr>
  <tr>
    <td>CharField</td>
    <td>name</td>
    <td>Name of the sender</td>
  </tr>
  <tr>
    <td>EmailField</td>
    <td>email</td>
    <td>Sender's email address</td>
  </tr>
  <tr>
    <td>TextField</td>
    <td>message</td>
    <td>Message content</td>
  </tr>
  <tr>
    <td>DateTimeField</td>
    <td>submitted_on</td>
    <td>Timestamp of submission</td>
  </tr>
</table>