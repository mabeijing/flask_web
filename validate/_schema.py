schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "TestInfo",
    "description": "some information about test",
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the test",
            "type": "string"
        },
        "age": {
            "description": "age of test",
            "type": "integer"
        }
    },
    "required": [
        "name", "age"
    ]
}