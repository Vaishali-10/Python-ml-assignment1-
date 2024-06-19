def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# Example usage:
main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to check: ")

if check_substring(main_str, sub_str):
    print(f"The substring '{sub_str}' is present in the main string '{main_str}'.")
else:
    print(f"The substring '{sub_str}' is not present in the main string '{main_str}'.")
