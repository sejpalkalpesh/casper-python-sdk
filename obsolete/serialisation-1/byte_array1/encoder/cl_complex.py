import typing

import pycspr.serialisation.byte_array.encoder.cl_primitive as primitives_encoder
from pycspr.types import PublicKey
from pycspr.types import StateKey
from pycspr.types import StateKeyType
from pycspr.types import UnforgeableReference


def encode_any(value: object) -> bytes:
    """Encodes a value of an unassigned type.

    """
    raise NotImplementedError()


def encode_list(value: list, inner_encoder: typing.Callable) -> bytes:
    """Encodes a list of values.

    """
    return encode_vector_of_t(list(map(inner_encoder, value)))


def encode_map(value: list) -> bytes:
    """Encodes a map of keys to associated values.

    """
    raise NotImplementedError()


def encode_option(value: object, inner_encoder: typing.Callable) -> bytes:
    """Encodes an optional CL value.

    """
    return bytes([0] if value is None else [1]) + inner_encoder(value)


def encode_public_key(value: PublicKey) -> bytes:
    """Encodes a public key.

    """
    return bytes([value.algo.value]) + value.pbk


def encode_result(value: object) -> bytes:
    """Encodes a smart contract execution result.

    """
    raise NotImplementedError()


def encode_key(value: StateKey) -> bytes:
    """Encodes a key mapped to data within global state.

    """
    if value.key_type == StateKeyType.ACCOUNT:
        return bytes([0]) + value.identifier
    elif value.key_type == StateKeyType.HASH:
        return bytes([1]) + value.identifier
    elif value.key_type == StateKeyType.UREF:
        return bytes([2]) + value.identifier
    else:
        raise ValueError(f"Unencodeable key type: {value}")


def encode_tuple1(value: tuple) -> bytes:
    """Encodes a 1-ary tuple of CL values.

    """
    raise NotImplementedError()


def encode_tuple2(value: tuple) -> bytes:
    """Encodes a 2-ary tuple of CL values.

    """
    raise NotImplementedError()


def encode_tuple3(value: tuple) -> bytes:
    """Encodes a 3-ary tuple of CL values.

    """
    raise NotImplementedError()


def encode_uref(value: UnforgeableReference):
    """Encodes an unforgeable reference.

    """
    return primitives_encoder.encode_byte_array(
        value.address + bytes([value.access_rights.value])
        )


def encode_vector_of_t(value: list):
    """Encodes an unbound vector.

    """
    return \
        primitives_encoder.encode_u32(len(value)) + \
        bytes([i for j in value for i in j])