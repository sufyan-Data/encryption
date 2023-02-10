import streamlit as st

def rc4(key, data):
    S = list(range(256))
    j = 0
    out = []

    # Key-scheduling algorithm
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)

def main():
    st.title("RC4 Encryption and Decryption")

    # Get key and data from user
    key = st.text_input("Enter a secret key:")
    data = st.text_area("Enter the data to be encrypted/decrypted:")

    # Encrypt and decrypt data
    if st.button("Encrypt"):
        result = rc4(key, data)
        st.success("Encrypted data: `{}`".format(result))
    if st.button("Decrypt"):
        result = rc4(key, data)
        st.success("Decrypted data: `{}`".format(result))

if __name__ == '__main__':
    main()
