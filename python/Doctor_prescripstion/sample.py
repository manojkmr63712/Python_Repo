from mimesis.schema import Field, Schema
from mimesis.enums import Gender
_ = Field('en')
description = (
	nam = _('full_name')
	print(nam[2:-5])
     lambda: {
        'id': _('uuid'),
        'name': _('text.word'),
        'version': _('version', pre_release=True),
        'timestamp': _('timestamp', posix=False),
        'Doctor': {
            'name': _('full_name'),
            'doc_id': _('uuid')
        },
    }
)
schema = Schema(schema=description)
print(schema.create(iterations=5))