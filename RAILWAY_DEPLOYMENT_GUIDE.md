### **Guide to Deploying the "AI Chatbot Kit"**

This guide will walk you through the process of deploying the AI Chatbot Kit, which includes a FastAPI backend and a Streamlit frontend, using Railway.app.

---

#### **Step 1: Fork the GitHub Repository**

1.  Navigate to the `gparadel0/ai-chatbot-kit` repository on GitHub.
2.  Click the **"Fork"** button in the top-right corner.
3.  This will create a copy of the repository under your own GitHub account. This is the repository you will connect to Railway.

---

#### **Step 2: Deploy the Backend Service on Railway**

1.  Go to **Railway.app** and log in to your account.
2.  From your dashboard, click **"Deploy a New Project"** or **"New Project"**.
3.  Select **"Deploy from GitHub repo"**.
4.  If you haven't already, connect your GitHub account and authorize Railway to access your repositories.
5.  Select the forked repository, `ai-chatbot-kit`, from the list.
6.  Railway will automatically create a new service. You'll see a deployment for the entire project.
7.  Click on the newly created service and rename it to **`backend`**.
8.  Go to the **"Settings"** tab for the `backend` service.
9.  Under the **"Source"** section, find **"Root Directory"** and enter `backend` to specify that this service should run the backend code.
10. In the **"Variables"** tab, add the following environment variables:
    * **`HOST`**: Set this to `::`
    * **`OPENAI_API_KEY`**: Paste your OpenAI API key here.
11. Add a volume to persist data:
    * Click on **"Create"** and select **"Volume"**.
    * Link the volume to the `backend` service.
    * Set the **"Mount path of the volume"** to `/data`.
---

#### **Step 3: Deploy the Frontend Service on Railway**

1.  Back on the Railway dashboard, click **"Create"** again and select **"Deploy from GitHub repo"**.
2.  Choose the same forked `ai-chatbot-kit` repository.
3.  Rename this new service to **`frontend`**.
4.  Go to the **"Settings"** tab for the `frontend` service.
5.  Under the **"Source"** section, set the **"Root Directory"** to `frontend`.
6.  The frontend needs to communicate with the backend. Go to the **"Variables"** tab for the `frontend` service.
7.  Add a new variable:
    * **`APL_URL`**: For the value, put `http://${{backend.RAILWAY_PRIVATE_DOMAIN}}:8080`, which will automatically use the private domain of the service called "backend".
8.  Click **"Deploy"** to deploy both services.
9.  Once it finished deploying, enable public networking for the frontend:
    * Go to the **"Settings"** tab.
    * Under **"Networking"**, click **"Generate Domain"** to create a public URL for your application.

---

#### **Step 4: Test the Application**

1.  Once both the `backend` and `frontend` services are successfully deployed, click on the public domain link generated for your `frontend` service.
2.  This will open your new AI chatbot application in a browser.
3.  You can now start a new chat, and the frontend will communicate with your deployed backend and OpenAI API to provide responses.

---

#### If you want to use your own frontend:

1. You need to add a domain name to your `backend` service (either your own custom domain or a Railway domain).
2. Add the variable `CORS_ORIGINS_STR` with the value of your frontend domain to the `backend` service.
