# Ask a user their weight(in pounds), convert it to kilograms and print on the terminal
# 1 Pound = 0.45kg


# Ask the user to enter their weight in pounds
weight_lbs= input('Whats your weight in pounds? ')


# Convert the input (string) into a number (float)
# Convert pounds to kilograms (1 pound = 0.453592 kg)
weight_kg= float(weight_lbs) * 0.45


# Print the converted weight
print(weight_kg)
