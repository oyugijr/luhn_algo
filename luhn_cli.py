import random

def luhn_check(card_number):
    """Validate a number using the Luhn Algorithm."""
    digits = [int(d) for d in str(card_number)][::-1]
    checksum = sum(d if i % 2 == 0 else (d * 2 - 9 if d * 2 > 9 else d * 2)
                   for i, d in enumerate(digits))
    return checksum % 10 == 0

def luhn_generate(base_number):
    """Generate a valid Luhn number by computing the correct check digit."""
    digits = [int(d) for d in str(base_number)]
    digits.append(0)  # Placeholder for checksum
    checksum = sum(d if i % 2 == len(digits) % 2 else (d * 2 - 9 if d * 2 > 9 else d * 2)
                   for i, d in enumerate(digits[:-1]))
    check_digit = (10 - (checksum % 10)) % 10
    return int(str(base_number) + str(check_digit))

def generate_random_luhn(length=16):
    """Generate a random valid Luhn-compliant number of given length."""
    if length < 2:
        raise ValueError("Length must be at least 2")
    base_number = random.randint(10**(length-2), 10**(length-1) - 1)
    return luhn_generate(base_number)

def get_valid_number(prompt):
    """Prompt the user until they enter a valid number or return to the menu."""
    while True:
        number = input(prompt).strip()
        if number.isdigit():
            return number
        print("\n⚠️ Invalid input. Please enter digits only.")
        print("1. Try again")
        print("2. Return to main menu")
        choice = input("Choose an option (1 or 2): ").strip()
        if choice == "2":
            return None  # Return to menu

def validate_batch():
    """Allows batch validation of multiple numbers."""
    numbers = input("Enter numbers separated by spaces: ").strip().split()
    for number in numbers:
        if number.isdigit():
            is_valid = luhn_check(number)
            print(f"{number} -> {'✅ VALID' if is_valid else '❌ NOT VALID'}")
        else:
            print(f"⚠️ Skipping invalid input: {number}")

def main():
    while True:
        print("\n" + "="*40)
        print("          Luhn Algorithm CLI          ")
        print("="*40)
        print("1. Validate a Luhn number")
        print("2. Generate a Luhn-compliant number from a base number")
        print("3. Generate a random Luhn number")
        print("4. Batch Validate multiple numbers")
        print("5. Exit")
        print("="*40)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            number = get_valid_number("Enter the number to validate: ")
            if number:
                is_valid = luhn_check(number)
                print(f"✅ {number} is a VALID Luhn number" if is_valid else f"❌ {number} is NOT a valid Luhn number")
                # if invalid, lets use the provided number as the base number and help generate a valid number and print it below the invalid
                if not is_valid:
                    # print(f"✅ Generated Luhn number: {luhn_generate(number)}")
                    print("\n")
                    # prompt to move to the main menu
                
                    print("1. Try again")
                    print("2. Use the number as base number")

                    retry = input("Choose an option (1 or 2): ").strip()
                    if retry == "2":
                        print(f"✅ Generated Luhn number: {luhn_generate(number)}")

                        print("1. Exit")
                        print("2. Return to main menu")
                        retry = input("Choose an option (1 or 2): ").strip()
                        if retry == "1":
                            break



                # # if invalid provide options to either try again or return to menu
                # if not is_valid:
                #     print("1. Try again")
                #     print("2. Return to main menu")
                #     retry = input("Choose an option (1 or 2): ").strip()
                #     if retry == "2":
                #         break
                    
        elif choice == "2":
            base_number = get_valid_number("Enter the base number: ")
            if base_number:
                print(f"✅ Generated Luhn number: {luhn_generate(base_number)}")

        elif choice == "3":
            while True:
                length = input("Enter the length of the Luhn number (min 2): ").strip()
                if length.isdigit() and int(length) >= 2:
                    print(f"✅ Generated random Luhn number: {generate_random_luhn(int(length))}")
                    break
                print("\n⚠️ Invalid input. Length must be at least 2.")
                print("1. Try again")
                print("2. Return to main menu")
                retry = input("Choose an option (1 or 2): ").strip()
                if retry == "2":
                    break

        elif choice == "4":
            validate_batch()

        elif choice == "5":
            print("\n🚀 Exiting... Goodbye!\n")
            break

        else:
            print("\n⚠️ Invalid option. Please select 1, 2, 3, 4, or 5.\n")

if __name__ == "__main__":
    main()
