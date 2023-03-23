import En_Cipher as en_Cipher
import De_Cipher as de_Cipher

Text = "Hello There"
Key = list("qwertyuiopasdfghjklzxcvbnm")
re_Fact = 2

print(f"Original Plain Text:\n{Text}")
#print("<---------------------------------------------Encryption------------------------------------------------------>")
Cipher = en_Cipher.encrypt(Text, re_Fact, Key)
print(f"\nThe Cipher text is:\n{Cipher}")
print("<---------------------------------------------Decryption------------------------------------------------------>")
Plain = de_Cipher.decrypt(Cipher, Key)
print(f"\nThe Original Plain text is:\n{Plain}")
