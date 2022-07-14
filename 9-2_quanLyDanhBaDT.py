def menu():
    entry = input('\n\n1. Display \n2. Add \n3. Check \n4. Delete \n5. Exit \nEnter your choice: ')
    return entry

def phonebook():
    contacts = []
    while True:
        entry = int(menu())
        if entry == 1:
            f = open('D:\FULL_Material_Semester12345\Semester5\Learn_Python\code_project\contact.txt','r')
            contacts = f.readlines()
            f.close()
            if not contacts:
                print('Empty phonebook !')
            else:
                for i in contacts:
                    print(i,end='')
        elif entry == 2:
            flag = False
            phoneNumber = input('Enter phone number : ')
            contactName = input('Enter contact name : ')
            f = open('D:\FULL_Material_Semester12345\Semester5\Learn_Python\code_project\contact.txt','r')
            contacts = f.readlines()
            f.close()
            for i in contacts:
                if i.find(contactName) != -1:
                    print('Contact already exist !')
                    flag = True
                    break
            if flag == False:
                f = open('D:\FULL_Material_Semester12345\Semester5\Learn_Python\code_project\contact.txt','a')
                contacts.append(contactName+': '+phoneNumber+'\n')
                contacts = f.write(contacts[-1])
                f.close()
                print('Contact saved successfully !')
        elif entry == 3:
            flag = False
            f = open('D:\FULL_Material_Semester12345\Semester5\Learn_Python\code_project\contact.txt','r')
            contacts = f.readlines()
            f.close()
            contactName = input('Enter contact name: ')
            for i in contacts:
                if i.find(contactName) != -1:
                    print(i)
                    flag = True
                    break
            if flag == False:
                print('Contact does not exist !')
        elif entry == 4:
            flag = False
            delete = 0
            f = open('D:\FULL_Material_Semester12345\Semester5\Learn_Python\code_project\contact.txt','r')
            contacts = f.readlines()
            f.close()
            contactName = input('Enter contact name: ')
            for i in contacts:
                if i.find(contactName) != -1:
                    print(i)
                    delete = contacts.index(i)
                    flag = True
                    confirm = input('Are you sure to delete?(y/n): ')
                    if confirm.lower() == 'y':
                        contacts.pop(delete)
                        f = open('D:\FULL_Material_Semester12345\Semester5\Learn_Python\code_project\contact.txt','w')
                        for i in contacts:
                            f.write(i)
                        f.close()
                    else:
                        print('Back to menu !')
                    break
            if flag == False:
                print('Contact does not exist !')
        elif entry == 5:
            print('Thank you so much !')
            break
        else:
            print('Please enter the integer in the range [1-5]')

phonebook()
