def print_info(name, age, is_student):
    print("Nama:", name)
    print("Usia:", age)
    if is_student:
        print("Status: Pelajar")
    else:
        print("Status: Bukan Pelajar")

print_info("Dwi", 25, False)
print_info("Aini", 18, True)