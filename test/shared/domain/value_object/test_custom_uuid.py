import pytest
from uuid import uuid4

from src.shared.domain.value_object.custom_uuid import Uuid


class TestUuid:
    def test_valid_uuid_initialization(self):
        valid_uuid = str(uuid4())
        uuid_obj = Uuid(valid_uuid)
        
        assert uuid_obj.value == valid_uuid
        assert str(uuid_obj) == valid_uuid
    
    def test_invalid_uuid_raises_error(self):
        invalid_uuids = [
            "not-a-uuid",
            "123",
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "",
            "12345678-1234-1234-1234-1234567890ab-extra"
        ]
        
        for invalid_uuid in invalid_uuids:
            with pytest.raises(ValueError, match=f"Invalid UUID: {invalid_uuid}"):
                Uuid(invalid_uuid)
