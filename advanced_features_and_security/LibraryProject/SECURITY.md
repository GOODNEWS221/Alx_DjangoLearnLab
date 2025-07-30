# Security Measures Implemented

- Set `DEBUG = False` to avoid exposing sensitive errors.
- Enabled browser protections using:
  - `SECURE_BROWSER_XSS_FILTER`
  - `X_FRAME_OPTIONS = 'DENY'`
  - `SECURE_CONTENT_TYPE_NOSNIFF`
- Enforced secure cookies:
  - `CSRF_COOKIE_SECURE`
  - `SESSION_COOKIE_SECURE`
- All templates now include `{% csrf_token %}` in forms.
- All views use Django ORM or parameterized queries to prevent SQL injection.
- Implemented Content Security Policy using `django-csp`.

## Testing Done
- Tested all forms for CSRF token inclusion.
- Attempted XSS inputs to ensure they are escaped.
- Verified that cookies are sent over HTTPS.