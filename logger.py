def log(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            '{} ran with args: {} and kwargs: {}'.format(original_function.__name__ ,args, kwargs))
        return original_function(*args, **kwargs)
    
    return wrapper
