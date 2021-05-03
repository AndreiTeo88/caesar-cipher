from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  caesar_text = ""
  for n in text:
    if n in alphabet:
      postion_letter = alphabet.index(n)
      if direction == "encode":
        new_position_letter = postion_letter + shift
      elif direction == "decode":
        new_position_letter = postion_letter - shift
      caesar_text += alphabet[new_position_letter]
    else:
      caesar_text += n
  print(f"Here's the {direction}d result: {caesar_text}")

should_not_end = True
while should_not_end:

  which_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  plain_text = input("Type your message:\n").lower()
  numb_shift = int(input("Type the shift number:\n"))

  numb_shift = numb_shift % 26

  caesar(plain_text, numb_shift, which_direction)

  go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if go_again == "no":
    should_not_end = False
    print("Good bye.")
