class NullObject:
    def __getattr__(self, *args, **kwargs):
        # Provide default behavior for any attribute accessed on the NullObject
        return lambda *args, **kwargs: self

    def __call__(self, *args, **kwargs):
        # Provide default behavior for method calls on the NullObject
        return self

# Create an instance of the NullObject to represent null or missing objects
null_object = NullObject()

def get_user_name(user):
    # Assume user is a dictionary-like object with a 'name' attribute
    return user.get('name', null_object)

user1 = {'name': 'John Doe'}
user2 = {}

print(get_user_name(user1))  # Output: John Doe
print(get_user_name(user2))  # Output: <__main__.NullObject object at 0x...>
