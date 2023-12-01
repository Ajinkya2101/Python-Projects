alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
 
def caesar(plain_text,cipher_text, shift_amount):
  if direction == "encode":
    cipher_text = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift
      cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

  elif direction == "decode":
      plain_text = ""
      for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift
        plain_text += alphabet[new_position]
      print(f"The decoded text is {plain_text}")

caesar(plain_text= text, cipher_text= text, shift_amount=shift)
