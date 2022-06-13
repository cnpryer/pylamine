from pylamine.pylamine import CalamineError


class UnimplmentedError(Exception):
    pass


class InvalidParameterError(Exception):
    pass


__all__ = ["CalamineError"]
