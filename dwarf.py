#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Dwarf - Software for parsing and manipulating ELF files
Author: OkulusDev
License: GNU GPL v3"""
from modules.parser import parse_elf


def main():
    data = parse_elf(input('File: '))
    
    print(data['binary'])
    print(data['header'])
    
    for section in data['sections']:
        size, name = section.size, section.name
        contentlen = len(section.content)
        print(f'=== SECTION {name} ===')
        print(f' SIZE: {size}')
        print(f' CONTENT LENGTH: {contentlen}')


if __name__ == "__main__":
    main()

