""" constants for bulk import of projects
"""

BULK_IMPORT_VERSIONS = ["1.0"]
BULK_IMPORT_COLS = {
    "1.0" : {
        "PROJECT TITLE":"<type 'str'>",
        "PROJECT STREAM":"<type 'str'>",
        "PROJECT FRAMEWORK":"<type 'str'>",
        "IEE PAPER":"<type 'str'>",
        "PROJECT ABSTRACT":"<type 'str'>"
    },
}

BULK_IMPORT_MANDATORY_FIELDS = ["PROJECT TITLE", "PROJECT STREAM", "PROJECT FRAMEWORK", "PROJECT ABSTRACT", "PROJECT PROVIDER ID"]

BULK_IMPORT_ERROR_SCHEMA = {
    "HEADER MISMATCH":"4201",
    "DATA MISSING":"4281"
}

BULK_IMPORT_ERROR_CODES = {
    "4201": "Header values Doesn't match. please check with the sample template and try again. Thank you",
    "4281": "The data for {0} is missing. we cannot allow as it is a mandatory field. please try again. Thank you"
}