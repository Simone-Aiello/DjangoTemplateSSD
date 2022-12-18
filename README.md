# Admin
    username: simone
    password: admin
# Model
    After creating a model register it in admin.py so it's accessible in the admin page
# Study list
    How to create models
    Models validators
    Serializers
    Permission, groups
    Testing Django models and urls
# Useful things
## How to query all the groups name associated with a user
    user_groups = list(request.user.groups.values_list('name', flat=True))
## Check read only methods
    if request.method in permissions.SAFE_METHODS: