def get_value_from_nested_object(obj, key):
    keys = key.split('/')  # Split the key into individual levels
    value = obj  # Start with the entire object

    try:
        for k in keys:
           # print(k)
            # print("before: " + str(value))
            value = value[k]  # Access the nested object based on the current key
            # print("after: " + str(value))
        return value
    except (KeyError, TypeError):
        return None  # Return None if the key is not found or if there's a type mismatch

# Example usage
object = {"a": {"b": {"c": "d"}}}
key = "a/b/c"
result = get_value_from_nested_object(object, key)
print(result)  # Output: example