from _ctypes import POINTER, Structure
from contextlib import contextmanager
from ctypes import c_char_p, c_int32, cdll
from pathlib import Path

PACKAGE_PATH = Path(__file__).parent

dylib_dir = PACKAGE_PATH / "dylib"
dylib_path = list(dylib_dir.glob("libsnips_nlu_ontology_rs*"))[0]
lib = cdll.LoadLibrary(str(dylib_path))


@contextmanager
def string_array_pointer(ptr):
    try:
        yield ptr
    finally:
        lib.snips_nlu_ontology_destroy_string_array(ptr)


@contextmanager
def string_pointer(ptr):
    try:
        yield ptr
    finally:
        lib.snips_nlu_ontology_destroy_string(ptr)


class CStringArray(Structure):
    _fields_ = [
        ("data", POINTER(c_char_p)),
        ("size", c_int32)
    ]
