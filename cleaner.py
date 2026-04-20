def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    clean_data = []
    lines = data.readlines()
    for line in lines:
        line.strip()
        if not line.strip() == 'minutes':
            clean_data.append(float(line))
    return clean_data