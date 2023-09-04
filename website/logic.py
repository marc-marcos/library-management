import isbnlib

def extract_metadata_from_isbn(isbn):
    metadata = isbnlib.meta(isbn)
    return metadata