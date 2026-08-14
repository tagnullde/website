from crypto import *

### initial values ###
db_sec_key = "R_EFY1hb236guS3jNq1aHyPcruXbjk7Ff-QwL6PMqJM="
db_salt = "qIhAhRt3xq_dzIEqyJQFmWnymFbO1cZVhbQaTWA-v9Q="
dba_hash = "utUU0jkamCZDmqFLOrAuPjFxL0zp8zWzISe5MF0GY/l8Silrmu3caqrtjaVjLQlvFFEgESGz"

### what we know ###
print "Current known dba hash: " + dba_hash

### run pwd through pqencryptpassword ###
user = "dba"
password = "supersecret"
pq_pwd = pqencryptpassword(password, user)
print ""
print "pq thingy: " + pq_pwd

### test encrypt function ###
print ""
print "Testing encrypt process...."
plaintext = pq_pwd
key = "R_EFY1hb236guS3jNq1aHyPcruXbjk7Ff-QwL6PMqJM="
new = encrypt(plaintext, key)
print "before: " + plaintext + " :After: " + new

### test decrypt function ###
print ""
print "Testing decrypt...."
ciphertext = new
print "Encrypted: " + ciphertext + " :decrypted: " + decrypt(ciphertext, key)

### decrypt ###
ciphertext = "utUU0jkamCZDmqFLOrAuPjFxL0zp8zWzISe5MF0GY/l8Silrmu3caqrtjaVjLQlvFFEgESGz"
#ciphertext = "l8Silrmu3caqrtjaVjLQlvFFEgESGz"
#ciphertext = "utUU0jkamCZDmqFLOrAuPjFxL0zp8zWzISe5MF0GY"
print ""
print "Actual...."
print decrypt(ciphertext, "$pbkdf2-sha512$25000$z9nbm1Oq9Z5TytkbQ8h5Dw$Vtx9YWQsgwdXpBnsa8BtO5kLOdQGflIZOQysAy7JdTVcRbv/6csQHAJCAIJT9rLFBawClFyMKnqKNL5t3Le9vg")
