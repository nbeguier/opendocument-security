# OpenDocument Security

## Prerequisites

```
pip3 install -r requirements.txt
```

### Usage

$ ./opendocument-security.py examples/vba-nested-ole.odt 
> Parsing ./examples/vba-nested-ole.odt
> This OpenDocument contains macro !
  > Object 2/Basic/Standard/TEST.xml
  > Object 2/Basic/Standard/script-lb.xml
  > Basic/Standard/TEST.xml
  > Basic/Standard/script-lb.xml
> Entering in content.xml
  > Found event listener: {'{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'dom:load'}
  > Found event listener: {'{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'office:save'}
  > Entering in Object 1/content.xml
  > Exiting Object 1/content.xml
  > Entering in Object 2/content.xml
    > Found event listener: {'{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'dom:load'}
    > Found event listener: {'{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'office:save'}
  > Exiting Object 2/content.xml
> Exiting content.xml
```
