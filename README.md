# OpenDocument Security

## Prerequisites

```
pip3 install -r requirements.txt
```

### Usage

```
# Example with classic OpenDocument
$ ./opendocument-security.py examples/vba-nested-ole.odt 
> Parsing OpenDocument examples/vba-nested-ole.odt
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


# Example with Flat OpenDocument
$ ./opendocument-security.py examples/only-ole-object.fodt 
> Parsing Flat OpenDocument examples/only-ole-object.fodt
> This Flat OpenDocument contains macro !
  > [<Element '{http://openoffice.org/2004/office}library-embedded' at 0x7f416deec950>]
> Entering in examples/only-ole-object.fodt
  > Found event listener: {'{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'dom:load', '{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.Module1.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple'}
  > Found event listener: {'{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'office:save', '{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.Module1.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple'}
> Exiting examples/only-ole-object.fodt

```
