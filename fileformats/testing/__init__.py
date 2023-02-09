from ._version import __version__
from fileformats.core import import_converters

from .headers import (
    Y,
    Xy,
    MyFormat,
    MyFormatGz,
    MyFormatGzX,
    MyFormatX,
    YourFormat,
    SeparateHeader,
    ImageWithHeader,
    EncodedText,
)
from .qualifers import A, B, C, D, E, F, G, H, J, K, L, M, N, AnyDataType, TestField

import_converters(__name__)
