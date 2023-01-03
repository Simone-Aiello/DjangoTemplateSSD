# Admin
    username: simone
    password: admin
# Model
    After creating a model register it in admin.py so it's accessible in the admin page
    class Song(models.Model):
        ALLOWED_GENRES = (
            ("ROCK", "ROCK"),
            ("TRAP", "TRAP"),
            ("RAP", "RAP"),
            ("COUNTRY", "COUNTRY"),
            ("PUNK", "PUNK"),
            ("HOUSE", "HOUSE"),
            ("DANCE", "DANCE"),
        )
    
        author = models.CharField(max_length=100, validators=[MinLengthValidator(1), RegexValidator(r'^[a-zA-Z0-9\s]+$')])
        title = models.CharField(max_length=100, validators=[MinLengthValidator(1), RegexValidator(r'^[a-zA-Z0-9\s]+$')])
        genre = models.CharField(max_length=10, choices=ALLOWED_GENRES)
        duration_in_seconds = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(1000000)])
# Study list
    How to create models
    Models validators
    Serializers
    Permission, groups
    Testing Django models and urls
# Validators
## Create class Validator
    @deconstructible
    class EnumValidator:

    def __init__(self, allowed_values: List[str]):
        self.allowed_values = allowed_values

    def __call__(self, value):
        if value not in self.allowed_values:
            raise ValidationError(f"Values must be one of {self.allowed_values}")

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (
            self.allowed_values == other.allowed_values
        )
## RegexValidator
    MAKE SURE YOU PUT ^$

## Function Validator
    def validate_in_allowed_values(value: str):
        allowed_values = ["ROCK", "TRAP", "RAP", "COUNTRY", "PUNK", "HOUSE", "DANCE"]
        if value not in allowed_values:
            raise ValidationError(f"Genre must be one of {allowed_values}")

# Permissions
## Group and read only permission
    class IsInGroup(permissions.BasePermission):
        __full_access_groups = ["Avengers", "AmericanGods", "Xmen"]
        __read_only_groups = ["DoomPatrol", "TheTick", "FutureMan"]
    
        def has_permission(self, request, view):
            user_groups = list(request.user.groups.values_list('name', flat=True))
            for group in user_groups:
                if group in self.__full_access_groups:
                    return True
            if request.method in permissions.SAFE_METHODS:
                for group in user_groups:
                    if group in self.__read_only_groups:
                        return True
            return False

# Serializer
## Validate in serializers
    def validate(self, attrs):
        instance = UmbrellaReservation(**attrs)
        instance.clean()
        return attrs
# Views
## get_serializer_class
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return CreateSongSerializer
        else:
            return ListSongSerializer
## get_queryset
    def get_queryset(self):
        return Post.object.filter(field=self.request.user)

# Testing
## useful functions
    def get_client(user=None):
        res = APIClient()
        if user is not None:
            res.force_login(user)
        return res
    
    
    def parse(response):
        response.render()
        content = response.content.decode()
        return json.loads(content)
## Model test example
    def test_invalid_values_for_duration(db):
        invalid_values = [-1, -4, 1000001, 9]
        for value in invalid_values:
            song = mixer.blend(Song, duration_in_seconds=value)
            with pytest.raises(ValidationError):
                song.full_clean()
## Adding a user to a group for testing
        user = mixer.blend(get_user_model())    
        group = mixer.blend(Group, name='beach-managers')
        user.groups.add(group)
## View test/url example
    def test_customer_user_can_make_post_requests(self, reservations):
        path = reverse('reservations-list')
        user = mixer.blend(get_user_model())
        client = get_client(user)
        reservation = {'number_of_seats': 2, 'reservation_start_date': datetime.date.today(),
                       'reservation_end_date': datetime.date.today(), 'reserved_umbrella_id': 10}
        response = client.post(path, reservation)
        assert response.status_code == HTTP_201_CREATED
## Reverse options
    path = reverse("basename-detail", kwargs={'pk': reservations[0].pk}) DELETE,PUT,PATCH,GET singola
    path = reverse('basename-list') POST, GET multiple 
# Other useful things
## How to query all the groups name associated with a user
    user_groups = list(request.user.groups.values_list('name', flat=True))
## Check read only methods
    if request.method in permissions.SAFE_METHODS:
## Check if a user has a specific group
    if request.user.groups.filter(name='NOME_GRUPPO').exists():
        pass