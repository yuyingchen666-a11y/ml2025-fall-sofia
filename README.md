# Book Library App – Final Project

## Overview
This project is a full-stack web application for managing a personal book library.  
Users can view, search, add, edit, and delete books. The application updates the interface without page reload.

The frontend is built with React and responsive CSS.  
The backend is built with Node.js and Express and provides REST API endpoints.  
Book data is stored temporarily in an array in the backend.

---

## Features

### User Features
- View a list of books with title, author, year, and genre
- Search books by title or author
- Add a new book through a form
- Edit book information
- Delete a book
- Dynamic UI without page refresh
- Responsive design that supports desktop, tablet, and mobile

### Technical Features
- Single-page application built with React components
- State management using useState and useEffect hooks
- Semantic HTML and responsive layout using Flexbox and media queries
- REST API built with Express for CRUD operations
- In-memory storage used for demonstration, can be replaced with a database later

---

## Project Structure


final-project/
 README.md
 backend/
 package.json
 server.js
 frontend/
 public/
 index.html
 src/
 index.js
 App.js
 styles.css
 components/
 Header.jsx
 Footer.jsx
 SearchBar.jsx
 BookList.jsx
 BookForm.jsx
 BookDetail.jsx

---

## How to Run the Project

### 1. Start the Backend API

Open a terminal and run:


cd backend
 npm install
 npm run dev # or: npm start

The API will run at:


http://localhost:5000

Available REST API endpoints:

| Method | Endpoint | Description |
|---|---|---|
| GET | /books | Retrieve all books |
| POST | /books | Add a new book |
| PUT | /books/:id | Edit a specific book |
| DELETE | /books/:id | Delete a specific book |

---

### 2. Start the Frontend (React App)

Open a separate terminal and run:


cd ../frontend
 npm install
 npm start

The React application will run at:


http://localhost:3000

Make sure the backend is running before testing the frontend.

---

## Technologies Used

### Frontend
- HTML5
- CSS3 with Flexbox and media queries
- JavaScript
- React (functional components, state hooks, fetch API)

### Backend
- Node.js
- Express
- CORS
- JSON request handling
- Temporary array storage

---

## Requirements Verification

| Requirement | Completed |
|---|---|
| HTML structure | Yes |
| Responsive CSS layout | Yes |
| DOM interactivity | Yes (implemented through React) |
| React SPA design | Yes |
| useState and useEffect | Yes |
| CRUD operations | Yes |
| Express REST API | Yes |
| Search feature | Yes |
| Temporary storage | Yes |

---

## Responsive Design
The layout uses Flexbox to organize the interface into a sidebar and a content area on larger screens.  
Media queries allow the layout to switch to a single-column format on smaller screens such as tablets and phones.  
The application is usable on different devices without layout issues.

---

## Learning Outcomes
While completing this project, I learned how to:

- Build a single-page application using React components
- Use useState and useEffect for application state and data loading
- Design responsive user interfaces using Flexbox and media queries
- Implement REST API endpoints in Express
- Connect frontend and backend systems using HTTP requests
- Manage create, read, update, and delete operations on data

---

## Future Improvements
Possible improvements for this application include:

- Replace temporary array with a real database such as SQLite or MongoDB
- Add user authentication and login
- Add book cover image uploads
- Add pagination, sorting, and category filters
- Deploy the application to a hosting platform

---

## Author
Final full-stack course project: Book Library App
