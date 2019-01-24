import hashlib
import uuid
def generate_hash(content):
    return hashlib.sha256(str(content).encode('utf-8')).hexdigest()

hash_something = generate_hash('hello world')
print(hash_something)
print(uuid.uuid4())