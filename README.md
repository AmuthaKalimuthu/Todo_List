# Flask Todo App with React Frontend & MySQL Database

## Prerequisites
- Python 3.7+
- Node.js 14+
- MySQL Server

## MySQL Setup
1. Install MySQL Server
2. Create database:
   ```sql
   mysql -u root -p < setup_mysql.sql
   ```
3. Update database credentials in `config.py`

## Backend Setup (Flask)
1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Initialize database:
   ```
   python init_db.py
   ```

3. Run Flask server:
   ```
   python app.py
   ```
   Server runs on http://localhost:5000

## Frontend Setup (React)
1. Navigate to frontend directory:
   ```
   cd frontend
   ```

2. Install Node.js dependencies:
   ```
   npm install
   ```

3. Start React development server:
   ```
   npm start
   ```
   Frontend runs on http://localhost:3000

## Database Configuration
Update MySQL credentials in `config.py`:
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/todo_db'
```

## API Endpoints
- GET /api/tasks - Get all tasks
- POST /api/tasks - Create new task
- PUT /api/tasks/{id}/toggle - Toggle task completion
- DELETE /api/tasks/{id} - Delete task