from passlib.hash import pbkdf2_sha256
class PasswordManager:
    def set_password(self, password):
        _hash = pbkdf2_sha256.using(rounds=35719).hash(password).split('$')
        self.password = _hash[4]
        self.salt = _hash[3]
    
    def verify_password(self, password):
        _hash = '$pbkdf2-sha256$35719${}${}'.format(self.salt, self.password)
        return pbkdf2_sha256.verify(password, _hash)