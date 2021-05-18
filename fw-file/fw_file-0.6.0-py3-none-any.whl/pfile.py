"""GE MR RAW / PFile format (Pnnnnn.7 files)."""
import datetime
import struct
import typing as t

from fw_meta import MetaExtractor
from fw_utils import AnyFile, BinFile

from .common import FieldsMixin
from .dicom.utils import parse_patient_name
from .file import File

HEADER_SIZE = 256 << 10  # 256 KB


class PFile(FieldsMixin, File):  # pylint: disable=too-many-ancestors
    """GE MR RAW data / PFile class."""

    def __init__(
        self,
        file: t.Union[AnyFile, BinFile],
        extractor: t.Optional[MetaExtractor] = None,
        encoding: str = "ascii",
    ) -> None:
        """Read and parse a PFile, supporting only a subset of the fields.

        Args:
            file (str|Path|file): Filepath (str|Path) or open file to read from.
            extractor (MetaExtractor, optional): MetaExtractor instance to
                customize metadata extraction with if given. Default: None.
            encoding (str, optional): String field encoding. Default: "ascii".
        """
        super().__init__(file, extractor=extractor)
        with self.file as rfile:
            # read the first 256K that covers all parsed fields
            header = rfile.read(HEADER_SIZE)
            # parse pfile version number (float) from the first 4 bytes
            version: float = round(unpack(header, 0, "f"), 3)
            if version not in VERSION_OFFSETS:
                raise ValueError(f"Invalid PFile or unsupported version: {version}")
            # parse known fields with the offsets for the version
            offsets = VERSION_OFFSETS[version]
            fields = {}
            for name, (offset, fmt) in offsets.items():
                value = unpack(header, offset, fmt, encoding=encoding)
                fields[name] = value
            # validate logo (~magic bytes for pfile type)
            if fields["logo"] not in ("GE_MED_NMR", "INVALIDNMR"):
                raise ValueError(f"Invalid PFile logo: {fields['logo']!r}")
        object.__setattr__(self, "header", header)
        object.__setattr__(self, "encoding", encoding)
        object.__setattr__(self, "version", version)
        object.__setattr__(self, "fields", fields)

    @property
    def default_meta(self) -> t.Dict[str, t.Any]:
        """Return the default Flywheel metadata of the PFile."""
        if self.im_datetime > 0:
            timestamp = datetime.datetime.utcfromtimestamp(self.im_datetime)
        else:
            month, day, year = [int(i) for i in self.scan_date.split("/")]
            hour, minute = [int(i) for i in self.scan_time.split(":")]
            year += 1900  # GE epoch begins in 1900
            timestamp = datetime.datetime(year, month, day, hour, minute)
        firstname, lastname = parse_patient_name(self.patient_name or "")
        defaults: t.Dict[str, t.Any] = {
            "subject.label": self.patient_id,
            "subject.firstname": firstname,
            "subject.lastname": lastname,
            "session.uid": self.exam_uid,
            "acquisition.uid": f"{self.series_uid}_{self.acq_no}",
            "acquisition.label": self.series_desc,
            "acquisition.timestamp": timestamp,
            "file.type": "pfile",
        }
        return {k: v for k, v in defaults.items() if v is not None and v != ""}

    def save(self, file: t.Optional[AnyFile] = None) -> None:
        """Save PFile."""
        with self.file as rfile:
            rfile.seek(HEADER_SIZE)
            after_header = rfile.read()
        with self.open_dst(file) as wfile:
            tell = wfile.write(pack(self.version, "f"))
            for name, (offset, fmt) in VERSION_OFFSETS[self.version].items():
                if offset > tell:
                    tell += wfile.write(self.header[tell:offset])
                if not self.get(name):
                    size = struct.calcsize("32s" if fmt == "uid" else fmt)
                    tell += wfile.write(bytes(size))
                    continue
                tell += wfile.write(pack(self[name], fmt, encoding=self.encoding))
            wfile.write(after_header)


def unpack(raw: bytes, offset: int, fmt: str, encoding: str = "ascii"):
    """Return field parsed from the raw bytes using the offset and format."""
    uid = fmt == "uid"
    fmt = "32s" if uid else fmt
    start, end = offset, offset + struct.calcsize(fmt)
    value = struct.unpack(fmt, raw[start:end])[0]
    if uid:
        # see: https://en.wikipedia.org/wiki/Binary-coded_decimal
        components = [
            str(byte - 1) if byte < 11 else "."
            for pair in [(b >> 4, b & 15) for b in value]
            for byte in pair
            if byte > 0
        ]
        value = "".join(components)
    if isinstance(value, bytes):
        value = value.split(b"\x00", 1)[0].decode(encoding)
    return value


def pack(value: t.Any, fmt: str, encoding: str = "ascii") -> bytes:
    """Return field value packed in raw bytes format."""
    uid = fmt == "uid"
    fmt = "32s" if uid else fmt
    if uid:
        bs = bytes(11 if c == "." else int(c) + 1 for c in value)
        bi = iter(bs.ljust(32, b"\x00"))
        value = bytes(b1 << 4 | b2 for b1, b2 in zip(bi, bi))
    if isinstance(value, str):
        value = value.encode(encoding)
    return struct.pack(fmt, value)


# PFile {version: field_offsets} map
# Adding support for a new version:
#   1. Duplicate the closest version within the dict
#   2. Set the key to the version number being added
#   3. Update field offsets (ask Michael Perry / Gunnar Shaefer for more)
VERSION_OFFSETS: t.Dict[float, t.Dict[str, t.Tuple[int, str]]] = {
    28.002: {
        "scan_date": (92, "10s"),
        "scan_time": (102, "8s"),
        "logo": (110, "10s"),
        "exam_no": (202548, "H"),
        "exam_uid": (203280, "uid"),
        "patient_name": (203376, "65s"),
        "patient_id": (203441, "65s"),
        "accession_no": (203506, "17s"),
        "patient_dob": (203523, "9s"),
        "series_no": (204548, "h"),
        "series_desc": (204794, "65s"),
        "series_uid": (204957, "uid"),
        "prescribed_duration": (206684, "f"),
        "im_datetime": (207420, "i"),
        "acq_no": (207866, "h"),
        "psd_name": (208004, "33s"),
    },
    27.001: {
        "scan_date": (92, "10s"),
        "scan_time": (102, "8s"),
        "logo": (110, "10s"),
        "exam_no": (202548, "H"),
        "exam_uid": (203280, "uid"),
        "patient_name": (203376, "65s"),
        "patient_id": (203441, "65s"),
        "accession_no": (203506, "17s"),
        "patient_dob": (203523, "9s"),
        "series_no": (204548, "h"),
        "series_desc": (204794, "65s"),
        "series_uid": (204957, "uid"),
        "prescribed_duration": (206684, "f"),
        "im_datetime": (207420, "i"),
        "acq_no": (207866, "h"),
        "psd_name": (208004, "33s"),
    },
    27.0: {
        "scan_date": (92, "10s"),
        "scan_time": (102, "8s"),
        "logo": (110, "10s"),
        "exam_no": (194356, "H"),
        "exam_uid": (195088, "uid"),
        "patient_name": (195184, "65s"),
        "patient_id": (195249, "65s"),
        "accession_no": (195314, "17s"),
        "patient_dob": (195331, "9s"),
        "series_no": (196356, "h"),
        "series_desc": (196602, "65s"),
        "series_uid": (196765, "uid"),
        "prescribed_duration": (198492, "f"),
        "im_datetime": (199228, "i"),
        "acq_no": (199674, "h"),
        "psd_name": (199812, "33s"),
    },
    26.002: {
        "scan_date": (92, "10s"),
        "scan_time": (102, "8s"),
        "logo": (110, "10s"),
        "exam_no": (194356, "H"),
        "exam_uid": (195088, "uid"),
        "patient_name": (195184, "65s"),
        "patient_id": (195249, "65s"),
        "accession_no": (195314, "17s"),
        "patient_dob": (195331, "9s"),
        "series_no": (196356, "h"),
        "series_desc": (196602, "65s"),
        "series_uid": (196765, "uid"),
        "prescribed_duration": (198492, "f"),
        "im_datetime": (199228, "i"),
        "acq_no": (199674, "h"),
        "psd_name": (199812, "33s"),
    },
    24.0: {
        "scan_date": (16, "10s"),
        "scan_time": (26, "8s"),
        "logo": (34, "10s"),
        "exam_no": (143516, "H"),
        "exam_uid": (144248, "uid"),
        "patient_name": (144344, "65s"),
        "patient_id": (144409, "65s"),
        "accession_no": (144474, "17s"),
        "patient_dob": (144491, "9s"),
        "series_no": (145622, "h"),
        "series_desc": (145762, "65s"),
        "series_uid": (145875, "uid"),
        "prescribed_duration": (147652, "f"),
        "im_datetime": (148388, "i"),
        "acq_no": (148834, "h"),
        "psd_name": (148972, "33s"),
    },
    21.001: {
        "scan_date": (16, "10s"),
        "scan_time": (26, "8s"),
        "logo": (34, "10s"),
        "exam_no": (144064, "H"),
        "exam_uid": (144788, "uid"),
        "patient_name": (144884, "65s"),
        "patient_id": (144949, "65s"),
        "accession_no": (145014, "17s"),
        "patient_dob": (145031, "9s"),
        "series_no": (146170, "h"),
        "series_desc": (146310, "65s"),
        "series_uid": (146423, "uid"),
        "prescribed_duration": (148200, "f"),
        "im_datetime": (148936, "i"),
        "acq_no": (149382, "h"),
        "psd_name": (149520, "33s"),
    },
    20.007: {
        "scan_date": (16, "10s"),
        "scan_time": (26, "8s"),
        "logo": (34, "10s"),
        "exam_no": (143516, "H"),
        "exam_uid": (144248, "uid"),
        "patient_name": (144344, "65s"),
        "patient_id": (144409, "65s"),
        "accession_no": (144474, "17s"),
        "patient_dob": (144491, "9s"),
        "series_no": (145622, "h"),
        "series_desc": (145762, "65s"),
        "series_uid": (145875, "uid"),
        "prescribed_duration": (147652, "f"),
        "im_datetime": (148388, "i"),
        "acq_no": (148834, "h"),
        "psd_name": (148972, "33s"),
    },
    20.006: {
        "scan_date": (16, "10s"),
        "scan_time": (26, "8s"),
        "logo": (34, "10s"),
        "exam_no": (143516, "H"),
        "exam_uid": (144240, "uid"),
        "patient_name": (144336, "65s"),
        "patient_id": (144401, "65s"),
        "accession_no": (144466, "17s"),
        "patient_dob": (144483, "9s"),
        "series_no": (145622, "h"),
        "series_desc": (145762, "65s"),
        "series_uid": (145875, "uid"),
        "prescribed_duration": (147652, "f"),
        "im_datetime": (148388, "i"),
        "acq_no": (148834, "h"),
        "psd_name": (148972, "33s"),
    },
    11.0: {
        "scan_date": (16, "10s"),
        "scan_time": (26, "8s"),
        "logo": (34, "10s"),
        "exam_no": (61576, "H"),
        "exam_uid": (61966, "uid"),
        "patient_name": (62062, "65s"),
        "patient_id": (62127, "65s"),
        "accession_no": (62192, "17s"),
        "patient_dob": (62209, "9s"),
        "series_no": (62710, "h"),
        "series_desc": (62786, "65s"),
        "series_uid": (62899, "uid"),
        "prescribed_duration": (64544, "f"),
        "im_datetime": (65016, "i"),
        "acq_no": (65328, "h"),
        "psd_name": (65374, "33s"),
    },
}
