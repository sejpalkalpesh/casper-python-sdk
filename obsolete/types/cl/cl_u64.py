import dataclasses

from pycspr.types.cl.cl_value import CL_Value
from pycspr.utils.conversion import int_to_le_bytes
from pycspr.utils.conversion import le_bytes_to_int


BYTE_LENGTH = 8


@dataclasses.dataclass
class CL_U64(CL_Value):
    # Associated value.
    value: int

    @staticmethod
    def from_bytes(as_bytes: bytes) -> "CL_U64":
        return CL_U64(le_bytes_to_int(as_bytes, False))


    @staticmethod
    def from_json(as_json: str) -> "CL_U64":
        return CL_U64(int(as_json))


    def to_bytes(self) -> bytes:
        return int_to_le_bytes(self.value, BYTE_LENGTH, False)


    def to_json(self) -> str:
        return str(self.value)
