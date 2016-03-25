

def get_from_config(config, property_name, default_value=None, transformation=None):
    _, value = config.get(property_name, (None, None))
    if value:
        return transformation(value) if transformation else value
    return default_value
