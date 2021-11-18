import dataclasses

from pycspr.types.cl_types import CL_Type_Bool
from pycspr.types.cl_values.base import CL_Value


@dataclasses.dataclass
class CL_Bool(CL_Value):
    """Represents a CL type value: boolean.
    
    """
    # Associated value.
    value: bool

    #region Equality & serialisation

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def as_bytes(self) -> bytes:
        return bytes([int(self.value)])

    def as_cl_type(self) -> CL_Type_Bool:
        return CL_Type_Bool()

    def as_parsed(self) -> str:
        return str(self.value)

    @staticmethod
    def from_bytes(as_bytes: bytes) -> "CL_Bool":
        return CL_Bool(bool(as_bytes[0]))
    
    #endregion
