import streamlit as st

def decrypt_message(encrypted_message, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in encrypted_message])

def main():
    st.set_page_config(page_title="RSA Decryption", layout="centered")

    st.title("RSA Decryption App")
    st.markdown("### Securely decrypt your text using RSA")

    e = st.text_input("Enter the public key (e)", "")
    n = st.text_input("Enter the product (n)", "")
    d = st.text_input("Enter the private key (d)", "")
    encrypted_message_str = st.text_area(
        "Enter the Cipher Text",
        placeholder="Enter the Cipher Text:",
        height=100
    )

    if st.button("Submit"):
        if e.strip() and n.strip() and d.strip() and encrypted_message_str.strip():
            try:
                e_val = int(e)
                n_val = int(n)
                d_val = int(d)
                encrypted_message = eval(encrypted_message_str)

                public_key = (e_val, n_val)
                private_key = (d_val, n_val)

                decrypted_message = decrypt_message(encrypted_message, private_key)

                st.markdown("---")
                st.markdown("**Decryption Results**")
                st.write(f"**Public Key:** {public_key}")
                st.write(f"**Private Key:** {private_key}")
                st.write(f"**Cipher Text:** {encrypted_message}")
                st.write("**Orignal Text:**", decrypted_message)

            except Exception as ex:
                st.error(f"An error occurred: {ex}")
        else:
            st.warning("Please fill in all fields before submitting.")

if __name__ == "__main__":
    main()