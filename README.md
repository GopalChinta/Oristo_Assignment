## Overview

This project is a **To-Do List Management Web Application** developed using **Flask (Python)** and **MySQL**. It allows users to:

- Create, update, and delete tasks.
- View a dashboard of existing tasks.
- Track task status, due dates, remarks, and timestamps.

## DB Design

### ER Diagram (Text Description)

```
+-------------+
|  tasks      |
+-------------+
| id (PK)     |
| title       |
| description |
| due_date    |
| status      |
| remarks     |
| created_on  |
| updated_on  |
| created_by  |
| updated_by  |
+-------------+
```

- A single table `tasks` stores all task-related information.
- The `id` field serves as the primary key.
- No foreign keys are used since there are no related tables in this version.

### Data Dictionary

```
| Field Name   | Data Type     | Description                                |
|--------------|---------------|--------------------------------------------|
| `id`         | INT (PK, AI)  | Unique task identifier                     |
| `title`      | VARCHAR(255)  | Title of the task                          |
| `description`| TEXT          | Detailed description                       |
| `due_date`   | DATE          | Due date for the task                      |
| `status`     | VARCHAR(50)   | Task status: Pending/In Progress/Completed |
| `remarks`    | TEXT          | Optional remarks                           |
| `created_on` | DATETIME      | Timestamp when task was created            |
| `updated_on` | DATETIME      | Timestamp when task was last updated       |
| `created_by` | VARCHAR(100)  | Who created the task                       |
| `updated_by` | VARCHAR(100)  | Who updated the task                       |

```

### Documentation of Indexes Used

- The `PRIMARY KEY` index is defined on the `id` column.
- No additional indexes are used, though indexing `due_date` or `status` could optimize performance for larger datasets.

### Code First or DB First Approach?

- **Approach Used:** Code First
- **Reason:** The database schema was designed based on the application's logic and requirements in Python code. This approach is suitable for smaller projects and rapid development.

## Structure of the Application

### Standard MVC Server-Side Page Rendering

- The application follows a basic MVC structure:
  - **Model:** MySQL database using SQL queries.
  - **View:** HTML templates with Jinja2 templating engine.
  - **Controller:** Flask route functions in `app.py`.
- All HTML is rendered on the server, and pages are refreshed on each action (non-SPA approach).

---

## Frontend Structure

### Frontend Used and Why

- **Frontend Used:** Web pages built using HTML and styled with Bootstrap 5.
- **Why:**
  - Quick development.
  - Compatible with Flask’s Jinja2 templates.
  - Provides a responsive and clean UI without JavaScript frameworks.

### Web Page or Mobile Application?

- A **Web Page Frontend** is used.
- Mobile responsiveness is handled via Bootstrap, but it is not a native mobile app.

---

## Build and Install

### Environment Details and List of Dependencies

- **Programming Language:** Python 3.9+
- **Framework:** Flask
- **Database:** MySQL 8.0+
- **Python Dependencies:**
  - Flask
  - mysql-connector-python

### Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/Devil-lucifer0402/oritso-assignment
   ```
2. Configure database credentials in `config.py`

3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create database named as `oritso`
6. Create `tasks` table by executing sql query from `migration.sql` file
7. Start the Flask development server:
   ```bash
   python run.py
   ```
   Then open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

Thanks!!
