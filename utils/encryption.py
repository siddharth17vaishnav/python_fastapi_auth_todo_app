from passlib.hash import pbkdf2_sha256

def encypt_password(password):
   return str(pbkdf2_sha256.hash(password))

def verify_password(password,hash_password):
   return pbkdf2_sha256.verify(password, hash_password)

from passlib.hash import pbkdf2_sha256

