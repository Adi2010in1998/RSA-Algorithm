import streamlit as st
import random
from sympy import isprime

def generate_prime(start, end):
    while True:
        num = random.randint(start, end)
        if isprime(num):
            return num

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys(bits=8):
    p = generate_prime(2**(bits-1), 2**bits)
    q = generate_prime(2**(bits-1), 2**bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 3
    while gcd(e, phi_n) != 1:
        e += 2

    d = mod_inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def encrypt_message(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def main():
    st.set_page_config(page_title="RSA Encryption", layout="centered")

    st.title("RSA Encryption App")
    st.markdown("### Securely encrypt your text using RSA")

    user_text = st.text_input("Enter Text To Encrypt", "")

    if st.button("Submit"):
        if user_text.strip():
            public_key, private_key = generate_keys(bits=8)

            encrypted_message = encrypt_message(user_text, public_key)

            st.markdown("---")
            st.markdown("**Encryption Results**")
            st.write(f"**Public Key (e):** {public_key[0]}")
            st.write(f"**Product (n):** {public_key[1]}")
            st.write(f"**Private Key (d):** {private_key[0]}")
            st.write("**Cipher Text:**", encrypted_message)
        else:
            st.warning("Please enter some text before submitting.")

if __name__ == "__main__":
    main()
