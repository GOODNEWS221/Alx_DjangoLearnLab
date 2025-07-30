# HTTPS Deployment Configuration

To deploy the Django app securely over HTTPS:

1. **Obtain an SSL/TLS certificate:**
   - Use Let's Encrypt (free) or a commercial provider.

2. **Configure the web server (e.g., Nginx or Apache):**
   - For Nginx:
     ```
     server {
         listen 443 ssl;
         server_name yourdomain.com;

         ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
         ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

         location / {
             proxy_pass http://127.0.0.1:8000;
             include proxy_params;
         }
     }
     ```

3. **Redirect HTTP to HTTPS:**
server {
listen 80;
server_name yourdomain.com;
return 301 https://$host$request_uri;
}


4. **Confirm Django is set to enforce HTTPS via `settings.py`.**
