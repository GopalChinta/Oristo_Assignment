CREATE TABLE tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  due_date DATETIME,
  status VARCHAR(50),
  remarks TEXT,
  created_on DATETIME,
  updated_on DATETIME,
  created_by VARCHAR(255),
  updated_by VARCHAR(255)
);