# Railway Deployment Guide

## Prerequisites
- Railway account
- GitHub repository with your code

## Deployment Steps

### 1. Create Railway Project
1. Go to [Railway.app](https://railway.app)
2. Sign in with your GitHub account
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Select your repository

### 2. Deploy Backend Service
1. Railway will automatically detect your main `Dockerfile`
2. Wait for the backend to deploy successfully
3. Note the backend service URL (e.g., `https://your-backend-name.railway.app`)

### 3. Deploy Frontend Service
1. In the same project, click **"New Service"** → **"GitHub Repo"**
2. Select the same repository
3. In the service settings, set **"Dockerfile Path"** to `Dockerfile.frontend`
4. Add environment variables:
   ```
   API_URL=https://your-backend-service-url.railway.app/chat/
   DEBUG=false
   ```
5. Deploy the frontend service

## Important Notes

### Port Configuration
- Railway automatically provides a `PORT` environment variable
- The `Dockerfile.frontend` is configured to use this port
- No manual port configuration needed

### Backend Service Options

#### Option 1: Deploy Both Services on Railway (Recommended)
1. **Deploy Backend First**:
   - Create a new Railway service using your main `Dockerfile`
   - Railway will assign a URL like `https://your-backend-name.railway.app`
   
2. **Deploy Frontend**:
   - Create another Railway service using `Dockerfile.frontend`
   - Set `API_URL=https://your-backend-name.railway.app/chat/`

#### Option 2: External Backend
- Point to an existing backend API (must be HTTPS)
- Set `API_URL=https://your-external-api.com/chat/`

**Note**: Railway serves all applications over HTTPS, so your backend must also be accessible via HTTPS.

### Environment Variables
- `API_URL`: URL of your backend API service
- `DEBUG`: Set to "true" for development debugging
- `PORT`: Automatically set by Railway

## Troubleshooting

### Common Issues
1. **Port binding errors**: The startup script handles Railway's PORT variable
2. **API connection errors**: Ensure `API_URL` is correctly set
3. **Build failures**: Check that all dependencies are in `requirements.txt`

### Logs
- Check Railway logs for any startup errors
- The startup script will show which port is being used
- Streamlit logs will show any application errors

## Local Testing
To test locally with Railway-like configuration:

```bash
# Set Railway-like environment
export PORT=8501
export API_URL=http://localhost:8000/chat/
export DEBUG=true

# Run with Docker
docker build -f Dockerfile.frontend -t frontend .
docker run -p 8501:8501 -e PORT=8501 -e API_URL=http://localhost:8000/chat/ frontend
```
