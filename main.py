# AIM: WAP to find students appearing for entrance exams
# Coder:shaikh aliya
# Date:2-4-26 

print("--- Entrance Exam Students ---")
cet_students = {"Alice", "Bob", "Charlie", "David"}
jee_students = {"Eve", "Frank", "Grace", "Heidi"}
neet_students = {"Ivan", "Judy", "Karl", "Liam"}

print(f"List of Students:")
print(f"CET Students: {cet_students}")
print(f"JEE Students: {jee_students}")
print(f"NEET Students: {neet_students}")

# Write your code here
# TODO: Find and Print All the Students appearing for any Entrance Exam

# TODO: Find and Print Students appearing for All Entrance Exams

# TODO: Find and Print Students appearing for JEE but not for NEET

# TODO: Find and Print Students appearing for CET and NEET but not for JEE
print("List of Students:")

all_students = cet | jee | neet
print(f"All Students: {all_students}")

all_exams = cet & jee & neet
print(f"All Exams: {all_exams}")

jee_not_neet = jee - neet
print(f"JEE but not for NEET: {jee_not_neet}")

cet_and_neet_not_jee = (cet & neet) - jee
print(f"CET and NEET but not for JEE: {cet_and_neet_not_jee}")
