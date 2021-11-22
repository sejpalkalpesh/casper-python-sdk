import dataclasses
from pycspr.types.cl_types.base import CL_Type
from pycspr.types.cl_types.base import CL_TypeKey


@dataclasses.dataclass
class CL_Type_Unit(CL_Type):
    """Encapsulates CL type information associated with a result value.

    """
    # CSPR type key.
    type_key: CL_TypeKey = CL_TypeKey.UNIT

    def __eq__(self, other) -> bool:
        return self.type_key == other.type_key

    def as_bytes(self) -> bytes:
        return bytes([self.type_key.value])

    def as_json(self) -> str:
        return "Unit"

    @staticmethod
    def from_bytes(_: bytes) -> "CL_Type_Unit":
        return CL_Type_Unit()
