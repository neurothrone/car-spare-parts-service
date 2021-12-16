from shared.exc import BaseError


class InvalidRequiredArgsError(BaseError):
    pass


class InvalidStoreTypeError(BaseError):
    pass


class OnlineStoreInvalidArgsError(BaseError):
    pass


class PhysicalStoreInvalidArgsError(BaseError):
    pass


class OnlineStoreExistsError(BaseError):
    pass
