#Basic Permissions Layout
## Superuser
- All permissions
- ** is the only one that can create new aquarium_controller objects **

## Aquarium_controller
- permission to post

## Users
- read only
- as of right now users are some what unnecessary for mvp because anyone will have read only permissions. Once the basic once the basic functionality is complete I want to tie users to particular controllers so they can send authenticated requests to the controllers
