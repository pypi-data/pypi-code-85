from . import (backbones, convertors, decoders, encoders, heads, losses, necks,
               preprocessor, recognizer)

from .backbones import *  # NOQA
from .convertors import *  # NOQA
from .decoders import *  # NOQA
from .encoders import *  # NOQA
from .heads import *  # NOQA
from .losses import *  # NOQA
from .necks import *  # NOQA
from .preprocessor import *  # NOQA
from .recognizer import *  # NOQA

__all__ = (
    backbones.__all__ + convertors.__all__ + decoders.__all__ +
    encoders.__all__ + heads.__all__ + losses.__all__ + necks.__all__ +
    preprocessor.__all__ + recognizer.__all__)
