#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" OpenDocument Security """

# Standard library imports
import logging
import sys
import zipfile

# Third party library imports
import xml.etree.ElementTree as ET

# Debug
# from pdb import set_trace as st

VERSION = '1.0.0'

LOGGER = logging.getLogger('opendocument-security')

def find_rec(node, element, result):
    for item in node:
        for match_item in item.findall(element):
            result.append(match_item)
        find_rec(item, element, result)
    return result

def get_event_listeners(content, script_prefix):
    result = list()
    find_rec(content, '{'+script_prefix+'}'+'event-listener', result)
    for script in result:
        LOGGER.critical('[CRITICAL] Found event listener: %s', script.attrib)

def get_ole_objects(content, draw_prefix):
    result = list()
    return find_rec(content, '{'+draw_prefix+'}'+'object', result)

def get_tag(content, tag):
    for i in content.decode().split(' '):
        if i.startswith(tag+'='):
            return i.split('"')[-2]

def main(odt_zipfile, content_path, indent=''):
    LOGGER.warning('%s> Entering in %s', indent, content_path)
    with odt_zipfile.open(content_path) as manifest:
        raw_content = manifest.read()
        root = ET.fromstring(raw_content)
        office_prefix = get_tag(raw_content, 'xmlns:office')
        script_prefix = get_tag(raw_content, 'xmlns:script')
        draw_prefix = get_tag(raw_content, 'xmlns:draw')
        xlink_prefix = get_tag(raw_content, 'xmlns:xlink')
        if office_prefix is None:
            LOGGER.warning('%s> Exiting %s', indent, content_path)
            return False
        if script_prefix is not None:
            get_event_listeners(root, script_prefix)
        if draw_prefix and xlink_prefix is not None:
            for ole_object in get_ole_objects(root, draw_prefix):
                draw_href = ole_object.attrib['{'+xlink_prefix+'}'+'href'].replace('./', '')
                main(odt_zipfile, '{}/{}'.format(draw_href, 'content.xml'), indent=indent+'  ')
    LOGGER.warning('%s> Exiting %s', indent, content_path)

if __name__ == '__main__':
    ODT_PATH = sys.argv[1]
    with zipfile.ZipFile(ODT_PATH, 'r') as ODT_ZIP_FILE:
        main(ODT_ZIP_FILE, 'content.xml')
