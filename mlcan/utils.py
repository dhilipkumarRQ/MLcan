def keep_selected_fields(dictionary, keep_fields):
    keys_to_remove = [key for key in dictionary if key not in keep_fields]
    for key in keys_to_remove:
        dictionary.pop(key)
