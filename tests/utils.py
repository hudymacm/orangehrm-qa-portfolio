import uuid


def generate_unique_name(prefix="Test"):
    return f"{prefix}{uuid.uuid4().hex[:8]}"