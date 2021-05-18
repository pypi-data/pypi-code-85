from typing import Any, Optional

from boa3.model.type.itype import IType
from boa3.neo.vm.type.AbiType import AbiType


class MetaType(IType):
    """
    A class used to represent internal Boa and Python types
    """

    def __init__(self, type_of: IType = None):
        identifier = 'type'
        super().__init__(identifier)
        self._internal_type: Optional[IType] = type_of

    @property
    def abi_type(self) -> AbiType:
        return AbiType.Any

    @classmethod
    def build(cls, value: Any) -> IType:
        if isinstance(value, IType):
            return cls(value)
        else:
            return metaType

    @classmethod
    def _is_type_of(cls, value: Any) -> bool:
        return isinstance(value, MetaType)

    def is_type_of(self, value: Any) -> bool:
        return isinstance(value, MetaType) and self._internal_type.is_type_of(value._internal_type)

    @property
    def has_meta_type(self) -> bool:
        return self._internal_type is not None

    @property
    def meta_type(self) -> Optional[IType]:
        return self._internal_type

    @property
    def meta_id(self) -> Optional[None]:
        return self._internal_type.identifier if self._internal_type is not None else None


metaType: IType = MetaType()
