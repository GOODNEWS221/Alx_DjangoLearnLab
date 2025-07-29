# Managing Permissions and Groups in Django

This application uses Django's built-in group and permission system to enforce access control.

## Custom Permissions Defined
In `Book` model (bookshelf/models.py):
- can_view
- can_create
- can_edit
- can_delete

## Groups Created
- **Viewers**: can view books
- **Editors**: can view, create, and edit books
- **Admins**: all permissions including delete

## Permission Enforcement
In `bookshelf/views.py`:
- Views are protected using `@permission_required` decorators.

## Testing
- Use Django admin to create test users and assign them to groups.
- Each user is restricted to actions defined by their group's permissions.

## How to Use
- Run migrations: `python manage.py makemigrations && python manage.py migrate`
- Access admin site: `http://127.0.0.1:8000/admin`
- Create users/groups and assign permissions

