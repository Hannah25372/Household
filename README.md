## Prerequisites

You will need to have installed:
- uv
- node.js

## To run

```
cd backend
uv sync
uv run uvicorn api.main:app --reload

cd frontend
npm install
npm run dev
```