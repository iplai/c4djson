def _closure(name, value):
    from c4djson.bl import BL
    return property(lambda cls: BL(cls(name, value)))


class _TypeMeta(type):
    def __new__(metacls, clsname, bases, attrs: dict):
        pairs = {
            k: v for k, v in attrs.items() if type(v) == int
        }
        for name, value in pairs.items():
            attrs[name] = classmethod(_closure(name, value))
        cls = super().__new__(metacls, clsname, bases, attrs)
        for name, value in pairs.items():
            Type.__members__[value] = cls(name, value)
        return cls


class Type(metaclass=_TypeMeta):
    __members__: dict[int, "Type"] = {}

    def __init__(self, name: str, value: int) -> None:
        self.name, self.value = name, value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"

    @classmethod
    def find(cls, value: int):
        try:
            return Type.__members__[value]
        except KeyError:
            ...
