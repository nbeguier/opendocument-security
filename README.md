# ODT Macro Lister

```

$ pip3 install -r requirements.txt


$ ./odt_macro_lister.py malware2.odt 
> Entering in content.xml
[CRITICAL] Found event listener: {'{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'dom:load', '{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple'}
[CRITICAL] Found event listener: {'{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'office:save', '{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple'}
  > Entering in Object 1/content.xml
  > Exiting Object 1/content.xml
  > Entering in Object 2/content.xml
[CRITICAL] Found event listener: {'{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'dom:load', '{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple'}
[CRITICAL] Found event listener: {'{urn:oasis:names:tc:opendocument:xmlns:script:1.0}language': 'ooo:script', '{urn:oasis:names:tc:opendocument:xmlns:script:1.0}event-name': 'office:save', '{http://www.w3.org/1999/xlink}href': 'vnd.sun.star.script:Standard.TEST.Flag?language=Basic&location=document', '{http://www.w3.org/1999/xlink}type': 'simple'}
  > Exiting Object 2/content.xml
> Exiting content.xml
```
