# Motel Meo

## Project Description

**Motel-Meo** is a comprehensive hotel management system designed for seamless management of hotel operations. This web-based application offers a robust suite of features to manage hotel accommodations, including room bookings, availability checks, and customer management.

## Features

### Hotel Management

Manage multiple hotels, each with details such as name, location, and available accommodations

### Room Management

Each hotel can list several types of rooms, specifying details like room type (e.g., Single, Double, Suite, Triple), availability, price, capacity, and size.

### Booking System

Customers can book rooms based on their preferences, with features such as selecting check-in and check-out dates, viewing room types, and confirming bookings instantly


## Strategy

The goal of the Motel Meo project is to develop a web-based application that allows users to book and manage motel rooms, facilitating smoother operations and enhanced user engagement for motel owners. The project is implemented using Django, Python, HTML/CSS, and JavaScript to ensure a smooth UI/UX design and functionality.

### Objectives

- **Project Setup**
  - Create the initial Django project and application.
  - Set up the directory structure following Django's common best practices.
  - Define and create database models relevant for motel operation.
  - Integrate custom CSS & JavaScript files.
  - Develop a `base.html` template for consistent layout throughout the app.
  - Use Google Fonts for better typography.

- **UX**
  - Include a custom favicon (e.g., a motel icon).
  - Implement Whitenoise to manage static files effectively.
  - Allow users to view various motel rooms and book as per their choice.
  - Style the login and registration pages using allauth.
  - Create an engaging Homepage.
  - Add a contact form on the contact page.
  - Implement 403, 404, and 500 error pages for better error management.
  - Enable both users and admins to view past and current bookings.
  - Implement notifications and alerts for improved interaction.

- **Navigation**
  - Implement a consistent Navbar across all pages.
  - Add a Footer with necessary links and copyright information in the same style across all pages.

- **CRUD Functionality**
  - Allow users to view upcoming and past bookings.
  - Provide functionality to book a room.
  - Enable cancellation of bookings.
  - Enhance admin capabilities for room and booking management.
  - Allow booking updates from both user and admin sides.

- **Authentication**
  - Setup Django allauth for user registration and authentication.
  - Enable account management for users, including email updates and password changes.
  - Implement email notifications for booking confirmations, cancellations, and updates.

- **Validation**
  - Implement validations in the booking form to ensure availability and correctness of data.

- **Administration**
  - Provide detailed admin features to manage bookings and room details.
  - Facilitate admin approval of bookings.

- **Deployment**
  - Used Heroku for deployment.
  - Set up a production-ready environment with proper settings.
  - Ensure that static and media files are managed through cloud services like Cloudinary.

- **Testing**
  - Develop unit tests for critical application components.
  - Conduct manual testing to ensure all user journeys work as intended.

- **Documentation**
  - Maintain a comprehensive README.md to guide future development and deployment.

## Installation & Usage

### Prerequisites

Ensure that you have Python (version 3.7 or newer) installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Installing

### Setup
1. Clone the project repository:
   ```bash
   git clone https://github.com/yourusername/motel-meo.git

2. Navigate into the project directory:
   ```bash
   cd motel-meo

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

### Running the Application

3. Install dependencies:
   ```bash
   pip install -r requirements.txt


## Tools Used

Motel Meo was built using a variety of technologies and services to ensure high-quality development, ease of deployment, and user experience. Below are the tools used in the development and maintenance of the project:

- [**GitHub**](https://github.com/) - Used for hosting the source code and version control.
- [**VS Code**](https://code.visualstudio.com/) - Primary code editor for developing the application.
- [**Heroku**](https://dashboard.heroku.com/) - Platform for deploying the live application.
- [**ElephantSQL**](https://www.elephantsql.com/) - PostgreSQL as a service used for the project's database.
- [**Balsamiq**](https://balsamiq.com/wireframes/) - For creating wireframes during the design phase.
- [**Favicon.io**](https://favicon.io/) - For generating the site's favicon.
- [**Font Awesome**](https://fontawesome.com/) - Provides icons used throughout the website.
- [**Bootstrap5**](https://getbootstrap.com/) - Utilized for initial site styling.
- [**Google Fonts**](https://fonts.google.com/) - For enhancing the typography of the site.
- [**Code Institute Pylint**](https://pep8ci.herokuapp.com/) - For Python code validation to adhere to PEP8 standards.
- [**HTML - W3C HTML Validator**](https://validator.w3.org/#validate_by_uri+with_options) - For validating HTML code.
- [**CSS - Jigsaw CSS Validator**](https://jigsaw.w3.org/css-validator/#validate_by_uri) - For validating CSS code.
- [**Chrome Dev Tools**](https://developer.chrome.com/docs/devtools/) - Used extensively for debugging and testing the project.
- [**W.A.V.E.**](https://wave.webaim.org/) - For accessibility testing.
- [**Cloudinary**](https://cloudinary.com/) - For managing static and media files, improving load times.
- [**Chrome LightHouse extension**](https://developer.chrome.com/docs/lighthouse/overview/) - For assessing the performance and SEO of the web pages.

These tools collectively help maintain the efficiency, reliability, and scalability of the Motel Meo project.
## Running the Tests

### Test 1

(Explanation of what the test does and how to interpret the results)

### Test 2

(Another explanation)

## Built With

(List of main libraries, frameworks used)

## Authors

## Acknowledgments

## Bugs Found and Fixed

### Bug Fixes

#### 1. Static Files Not Updating in Production
- **Issue**: Changes to `style.css` were not reflecting in the production environment.
- **Root Cause**: Misconfiguration in the handling of static files between development (`DEBUG = True`) and production (`DEBUG = False`).
- **Solution**: Implemented WhiteNoise to serve static files efficiently in production. Configured `STATICFILES_STORAGE` to use `whitenoise.storage.CompressedManifestStaticFilesStorage` and ensured correct settings in `STATIC_ROOT` and `STATICFILES_DIRS`.
- **Outcome**: Static files now update correctly in both development and production environments.

#### 2. Conflicting Static Files Storage Settings
- **Issue**: The project had conflicting settings for `STATICFILES_STORAGE` which caused confusion in static file handling.
- **Root Cause**: `STATICFILES_STORAGE` was set to both `cloudinary_storage.storage.StaticHashedCloudinaryStorage` and `whitenoise.storage.CompressedManifestStaticFilesStorage` in the settings.
- **Solution**: After evaluating both options, we decided to use WhiteNoise for its simplicity and efficiency in serving static files directly from the server. Removed the Cloudinary storage setting.
- **Outcome**: Simplified the static file handling and removed the dependency on external services for serving static files.

### Ongoing Issues

- **Current Bugs**: No critical bugs are currently impacting production. Minor UI adjustments are in progress.
- **Monitoring**: Continuously monitoring the application performance and user feedback to identify and fix any emerging issues promptly.

### Conclusion

The above fixes have significantly improved the stability and performance of our application. We are committed to maintaining a high standard of quality and responsiveness in addressing any future issues that may arise.