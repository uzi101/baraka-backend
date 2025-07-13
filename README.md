### ✅ Auth System

- Uses Firebase Authentication
- Verifies token via FastAPI dependency injection (`Depends(get_current_user)`)
- Returns user `uid`, `email`, and `provider`
- See `/api/auth/me` for example
