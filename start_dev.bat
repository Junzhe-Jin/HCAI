@echo off
echo Starting SmartPrompt Development Server...
echo ------------------------------------------

REM 激活虚拟环境
call backend\venv\Scripts\activate

REM 启动 FastAPI 后端
start cmd /k "cd backend && uvicorn app.main:app --reload"

REM 启动前端 Vite 服务
start cmd /k "cd frontend && npm run dev"

echo Services are starting. Do not close this window.
pause
