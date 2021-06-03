from ..lists.suspicious_words import *

def run_verification(words, string):
    for word in words:
        if word in string.lower():
            return True
    return False

def includes_pass(string):
    words = ["pass", "senha"]
    return run_verification(words, string)
        
def includes_user(string):
    words = ["user", "usuario"]
    return run_verification(words, string)

def includes_key(string):
    words = ["key", "chave"]
    return run_verification(words, string)

def includes_no_pass(string):
    words = ["nopasswd", "all=nopasswd", "nopasswd:all"]
    return run_verification(words, string)

def includes_add_user_command(string):
    words = ["adduser", "useradd"]
    return run_verification(words, string)

def includes_disabled_password(string):
    words = ["disabled-password", "no-password"]
    return run_verification(words, string)

def includes_host(string):
    words = ["host", "url", "uri", "domain", "dominio"]
    return run_verification(words, string)

def includes_suspicious_ip(string):
    words = ["0.0.0.0", "--ip='*'", "--ip=*", "--host=*", "--host='*'"]
    return run_verification(words, string)

def includes_permission(string):
    words = ["777", "a+rwx"]
    return run_verification(words, string)

def includes_weak_encryption(string):
    words = ["md5", "md4", "sha1", "sha-1"]
    return run_verification(words, string)

def includes_suspicious_word(string):
    for word in suspicious_words:
        if(word in string.lower()):
            return True