# Flask Todo App with React Frontend

## Setup Instructions

### Backend (Flask)
1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run Flask server:
   ```
   python app.py
   ```
   Server runs on http://localhost:5000

### Frontend (React)
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

## API Endpoints
- GET /api/tasks - Get all tasks
- POST /api/tasks - Create new task
- PUT /api/tasks/{id}/toggle - Toggle task completion
- DELETE /api/tasks/{id} - Delete task