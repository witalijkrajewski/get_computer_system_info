def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f"{round(bytes, 2)}{unit}{suffix}"
        bytes /= factor


