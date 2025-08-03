"""
Authentication & Permissions:
- Uses TokenAuthentication from DRF
- Token retrieval endpoint: /api/api-token-auth/
- All CRUD operations on books require the user to be authenticated
- Token must be included in the Authorization header as:
  Authorization: Token <your_token>
"""

