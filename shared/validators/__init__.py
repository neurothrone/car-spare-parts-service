def validate_primary_key(pk: int) -> None:
    if pk < 1:
        raise ValueError(f"Provided primary key with a value of {pk}. It can not be less than 1.")


def validate_length(provided: str, limit: int):
    if len(provided) > limit:
        error_msg = f"Provided string value '{provided}' exceeded the specified length limit of {limit}."
        raise ValueError(error_msg)
