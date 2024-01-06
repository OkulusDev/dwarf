import lief


def parse_elf(filepath: str) -> dict:
    binary = lief.parse(filepath);

    return {
        'binary': binary,
        'header': binary.header,
        'sections': binary.sections,
    }



