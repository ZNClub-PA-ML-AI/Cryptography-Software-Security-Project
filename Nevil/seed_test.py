# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 00:49:12 2016

@author: Nevil Dsouza
"""


import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
key = os.urandom(16)
iv = os.urandom(16)
cipher = Cipher(algorithms.SEED(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"45") + encryptor.finalize()
print(str(ct.decode("utf-16")))

decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()

print(pt)

