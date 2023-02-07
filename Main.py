
def save_to_file(file_name: str, file_contents: str )-> bool:
    try:
        with open(f'text_files/{file_name}.txt', 'w') as file:
            file.write(file_contents)
        return True
    except Exception as e:
        print(f'Error: {e}')
        return False


my_file_name = input('What is the file name ')
my_file_contents = input('What is the file content ')
print(save_to_file(my_file_name, my_file_contents))
