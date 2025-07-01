#حالات دیگر:
# contacts=[{"name":name, "num"=num}]
# or contact={"name"=name, "num"=num}
# contacs={contact}
contacts=[] 
def add-contact():
name= input("Enter name:")
num= int(input("Enter name:"))
contact={"name":name, "num":num}
contact.append(contact)
print("مخاطب با موفقیت افزوده شد!")
print(contacts)

def empty_contacts():
if len(contacts)==0:              #  بررسی خالی بودن لیست.
    print("لیست مخاطبین خالی است.")
else:
    print("لیست مخاطبین:")
for i, contact in enumerate(contacts, start=1)  #برای شماره‌گذاری مخاطبین
    print(f"{i}. {contact['name']} - {contact['phone']}") #دسترسی به مقدارهای دیکشنری



def search_contact():
search_name = input("نام یا بخشی از نام مخاطب را وارد کنید: ")
found = False
for contact in contacts:
    if search_name.lower() in contact['name'].lower():    #یعنی بخشی از اسم هم قابل جستجوه
        print(f"{contact['name']} - {contact['phone']}")
        found = True
        break  # چون پیدا کردیم، دیگه نیازی به ادامه نیست
if not found:
    print("مخاطبی با این نام پیدا نشد.")


def delete_contact():
del_name = input("نام مخاطبی که می‌خواهید حذف کنید را وارد کنید: ")

found = False
for contact in contacts:
    if contact["name"] == search_name:
        contacts.remove(contact)
        print(f"مخاطب '{search_name}' با موفقیت حذف شد.")
        found = True
        break

if not found:
    print("مخاطب مورد نظر پیدا نشد.")


# #editsearch_name = input("نام مخاطبی که می‌خواهید ویرایش کنید را وارد کنید: ")

# found = False  # پرچم برای اینکه بفهمیم پیدا شده یا نه
# for contact in contacts:
#     if contact["name"] == search_name:
#         # اینجا در مرحله بعد مقدار جدید رو می‌گیریم و جایگزین می‌کنیم
#         found = True
#         break

# if not found:
#     print("مخاطب مورد نظر پیدا نشد.")

def update_contact():
    upd_name = input("نام مخاطبی که می‌خواهید ویرایش کنید را وارد کنید: ")
    for contact in contacts:
        if contact['name'] == upd_name:
            new_phone = input("شماره تلفن جدید را وارد کنید: ")
            contact['phone'] = new_phone
            print("شماره تلفن به‌روزرسانی شد.")
            return
    print("مخاطبی با این نام پیدا نشد.")
while True:
    print("\n--- منوی دفترچه تلفن ---")
    print("1. افزودن مخاطب")
    print("2. نمایش مخاطبین")
    print("3. جستجوی مخاطب")
    print("4. حذف مخاطب")
    print("5. ویرایش مخاطب")
    print("6. خروج")
    choice=input("گزینه مورد نظر را وارد کنید (1-6): ")
      if choice == "1":
        name= input("enter ur name:")
        phone= int(input("enter phone:"))
        contact={"name":name,"phone":phone}
        contacts.append(contact)
        print("✅ مخاطب با موفقیت افزوده شد.")
      
    elif choice == "2":
        if len(contacts)==0:
            print("⚠️ هیچ مخاطبی وجود ندارد.")
    else:
        print("📒 لیست مخاطبین:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. نام: {contact['name']} - شماره: {contact['phone']}")
        ...
    
    elif choice == "3":
        search_name = input("نام مخاطب مورد نظر را وارد کنید: ")
    found = False
    for contact in contacts:
        if contact["name"] == search_name:
            print(f"📞 شماره {search_name}: {contact['phone']}")
            found = True
            break
    if not found:
        print("❌ مخاطب پیدا نشد.")

    elif choice == "4":
        delete_name = input("نام مخاطبی که می‌خواهید حذف کنید را وارد کنید: ")
    for contact in contacts:
        if contact["name"] == delete_name:
            contacts.remove(contact)
            print(f"🗑 مخاطب {delete_name} با موفقیت حذف شد.")
            break
    else:
        print("❌ مخاطب پیدا نشد.")
        ...
    elif choice == "5":
        update_name=input("enter new name:")
        for contact in contacts:
            if contact[name]==update_name:
                new_name = input("نام جدید: ")
            new_phone = input("شماره جدید: ")
            contact["name"] = new_name
            contact["phone"] = new_phone
            print(f"✅ مخاطب '{update_name}' با موفقیت به‌روزرسانی شد.")
            break
    else:
        print("❌ مخاطب پیدا نشد.")
        ...
    elif choice == "6":
         if contacts:
        print("📒 لیست مخاطبین:")
        for contact in contacts:
            print(f"👤 {contact['name']} - 📞 {contact['phone']}")
        else:
            print("⚠️ دفترچه تلفن خالی است.")
            break
    else:
        print("گزینه نامعتبر است. لطفاً عددی بین 1 تا 6 وارد کنید.")
    elif choice == "7":
            print("خدانگهدار!")
            break
        else:
            print("گزینه نامعتبر است. دوباره تلاش کنید.")

if __name__ == "__main__":
    main()

