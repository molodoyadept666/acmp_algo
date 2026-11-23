count_strings_one_page, string_index = map(int, input().split())
page_number = (string_index - 1) // count_strings_one_page + 1
string_number = (string_index - 1) % count_strings_one_page + 1
print(page_number, string_number)