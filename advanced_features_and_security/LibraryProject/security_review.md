# Security Review for HTTPS Implementation

## Settings Configured

- `SECURE_SSL_REDIRECT = True`: Forces all requests to use HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Tells browsers to only use HTTPS for the domain.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows domain to be submitted to browser preload lists.
- `SESSION_COOKIE_SECURE = True`: Ensures cookies are not sent over HTTP.
- `CSRF_COOKIE_SECURE = True`: Same as above, for CSRF cookies.
- `X_FRAME_OPTIONS = 'DENY'`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-sniffing attacks.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables basic browser-side XSS protection.

## Deployment Steps

See `deployment_https_notes.md` for full server configuration details.

## Potential Improvements

- Use Content Security Policy (CSP) headers.
- Set `Referrer-Policy`, `Permissions-Policy`, and `Strict-Transport-Security` headers at the server level.
- Monitor HTTPS certificate renewal automation (e.g., Certbot auto-renewal logs).
