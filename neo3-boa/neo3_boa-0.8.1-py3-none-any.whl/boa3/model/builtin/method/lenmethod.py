from typing import Any, Dict, List, Optional, Sized, Tuple

from boa3.model.builtin.method.builtinmethod import IBuiltinMethod
from boa3.model.expression import IExpression
from boa3.model.type.collection.icollection import ICollectionType
from boa3.model.type.collection.sequence.sequencetype import SequenceType
from boa3.model.type.itype import IType
from boa3.model.variable import Variable
from boa3.neo.vm.opcode.Opcode import Opcode


class LenMethod(IBuiltinMethod):

    def __init__(self, collection_type: IType = None):
        from boa3.model.type.type import Type
        if not isinstance(collection_type, ICollectionType):
            collection_type = Type.sequence

        identifier = 'len'
        args: Dict[str, Variable] = {'__o': Variable(collection_type)}
        super().__init__(identifier, args, return_type=Type.int)

    def validate_parameters(self, *params: IExpression) -> bool:
        if len(params) != 1:
            return False
        if not isinstance(params[0], IExpression):
            return False
        return isinstance(params[0].type, SequenceType)

    @property
    def opcode(self) -> List[Tuple[Opcode, bytes]]:
        return [(Opcode.SIZE, b'')]

    @property
    def _args_on_stack(self) -> int:
        return len(self.args)

    @property
    def _body(self) -> Optional[str]:
        return None

    def build(self, value: Any) -> IBuiltinMethod:
        if type(value) == type(self.args['__o'].type):
            return self

        if isinstance(value, Sized) and len(value) == 1:
            value = value[0]
        if isinstance(value, ICollectionType):
            return LenMethod(value)
        return super().build(value)
