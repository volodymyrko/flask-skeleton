import hashids
from flask import current_app


def generate_hash_code(number):
    """Generate hash code."""
    return hashids.Hashids(
        salt=current_app.config['HASH_SALT'],
        min_length=7
    ).encode(number)
