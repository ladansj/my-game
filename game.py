import random

# لیست انتخاب‌ها
choices = ["سنگ", "کاغذ", "قیچی"]

# انتخاب تصادفی توسط کامپیوتر
computer_choice = random.choice(choices)

# گرفتن انتخاب بازیکن
player_choice = input("یکی از گزینه‌های 'سنگ'، 'کاغذ' یا 'قیچی' را انتخاب کن: ")

# چاپ انتخاب بازیکن و کامپیوتر
print(f"انتخاب شما: {player_choice}")
print(f"انتخاب کامپیوتر: {computer_choice}")
# بررسی نتیجه بازی
if player_choice == computer_choice:
    print("بازی مساوی شد!")
elif (player_choice == "سنگ" and computer_choice == "قیچی") or \
     (player_choice == "قیچی" and computer_choice == "کاغذ") or \
     (player_choice == "کاغذ" and computer_choice == "سنگ"):
    print("شما برنده شدید!")
else:
    print("کامپیوتر برنده شد!")
