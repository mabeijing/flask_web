schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "TestInfo",
    "description": "some information about test",
    "type": "object",
    "properties": {
        "username": {
            "description": "Name of the test",
            "type": "string"
        },
        "password": {
            "description": "age of test",
            "type": "string"
        }
    },
    "required": [
        "username", "password"
    ]
}
