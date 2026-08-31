@echo off
echo Starting both frontend and backend development servers...
start cmd /k "cd frontend && npm run dev"
start cmd /k "cd backend && uv run uvicorn api.main:app --reload"