# Deploying to Render

How to host this web app on the render platform.

Reference: https://render.com/docs/deploy-flask

## Render Setup

1. Log in to [Render](https://dashboard.render.com) and go to the dashboard.
2. Create a new **Web Service**.
3. Choose this repository using its public URL (Public Git Repository).
4. Set the start command:

```sh
gunicorn "web_app:create_app()"
```

5. Choose the **Free** instance type.
6. Add environment variables (without quotes):
   - `ALPHAVANTAGE_API_KEY` - your AlphaVantage API key
   - `SECRET_KEY` - a long random string
7. Click **Deploy Web Service**.

## Redeploys

Every push to the `main` branch triggers a new deployment automatically. You can also trigger a deploy manually from the Render dashboard.

When the build finishes, the app is live at the URL shown in Render (like `https://YOUR-APP.onrender.com/`).

