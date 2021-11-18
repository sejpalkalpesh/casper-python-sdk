import dataclasses

from pycspr.types.cl_values.base import CL_Value


@dataclasses.dataclass
class U8Array(CL_Value):
    # Associated value.
    value: bytes

    @staticmethod
    def from_bytes(as_bytes: bytes) -> "U8Array":
        raise NotImplementedError()

    @staticmethod
    def from_json(as_json: str) -> "U8Array":
        raise NotImplementedError()

    def to_bytes(self) -> bytes:
        raise NotImplementedError()

    def to_json(self) -> str:
        raise NotImplementedError()
