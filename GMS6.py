class Superuser:
    regimens = {}
    members_gym = {}

    @classmethod
    def add_member(cls, member):
        Superuser.members_gym[member.get_phn_no()] = member


class Member:
    def __init__(self, name, age, gender, phn_no, email, bmi, membership_duration):
        self.name = name
        self.age = age
        self.gender = gender
        self.phn_no = phn_no
        self.email = email
        self.bmi = bmi
        self.membership = membership_duration

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_phn_no(self):
        return self.phn_no

    def set_phn_no(self, phn_no):
        self.phn_no = phn_no

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_bmi(self):
        return self.bmi

    def set_bmi(self, bmi):
        self.bmi = bmi

    def get_membership_duration(self):
        return self.membership_duration

    def set_membership_duration(self, membership_duration):
        self.membership_duration = membership_duration

print("(-:(-:(-: Edyoda Gym :-):-):-)")

while True:
    print("1 for User and 2 for Superuser:")
    print("Exit - 0")
    Memb = int(input())

    if Memb == 1:
        print('User')
        while True:
            print('''1=> User Regimen \n\n2=> User Profile \n\n0=> Exit''')

            select = int(input())

            if select == 1:
                num = int(input("Enter Phone No:"))
                print("Regimen Based on your BMI")
                for s in Superuser.regimens:
                    if s == num:
                        for l, m in Superuser.regimens[s].items():
                            print(l, ":", m)

            elif select == 2:
                num = int(input("Enter Contact No:"))
                try:
                    for s in Superuser.members_gym:
                        if s == num:
                            t = Superuser.members_gym[s]
                            print("Your Profile")
                            print(f"Name: {t.get_name()}"
                                  f"\nAge: {t.get_age()}"
                                  f"\nGender: {t.get_gender()}"
                                  f"\nEmail: {t.get_email()}"
                                  f"\nBMI: {t.get_bmi()}"
                                  f"\nMembership Duration: {t.get_membership_duration()}")
                except:
                    print("User Doesn't Exist")

            elif select == 0:
                break

            else:
                print("Invalid Input")

    elif Memb == 2:
        print("Super User")
        while True:
            print('''
            1=> Create User
            2=> View User
            3=> Delete User
            4=> Update User
            5=> Create Regimen
            6=> View Regimen
            7=> Delete Regimen
            8=> Update Regimen
            0=> Exit
            ''')

            select = int(input())

            if select == 1:
                print("Enter User Details\n")
                name = input("Enter Name:")
                age = int(input("Enter Age:"))
                gender = input("Enter Gender:")
                no = int(input("Enter Mobile No.:"))
                email = input("Enter Email:")
                bmi = int(input("Enter BMI:"))
                membership = int(input("Enter Membership Duration In Months:"))

                if bmi < 18.5:
                    regimen = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Rest',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Rest',
                         'Sun': 'Rest'
                         }

                elif bmi < 25:
                    regimen = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Cardio/Abs',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Legs',
                         'Sun': 'Rest'
                         }

                elif bmi < 30:
                    regimen = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Abs/Cardio',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Legs',
                         'Sun': 'Cardio'
                         }

                elif bmi > 30:
                    regimen = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Cardio',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Cardio',
                         'Sun': 'Cardio'
                         }

                member = Member(name, age, gender, no, email, bmi, membership)
                Superuser.regimens[no] = regimen
                Superuser.add_member(member)


            elif select  == 2:
                num = int(input("Enter Phone No of User:"))
                for s in Superuser.members_gym:
                    if s == num:
                        y = Superuser.members_gym[s]
                        print(f"Name: {y.get_name()}"
                              f"\nAge: {y.get_age()}"
                              f"\nGender: {y.get_gender()}"
                              f"\nEmail: {y.get_email()}"
                              f"\nBMI: {y.get_bmi()}"
                              f"\nMembership Duration: {y.get_membership_duration()}")
                    else:
                        print("User Doesn't Exist")


            elif select  == 3:
                num = int(input("Enter Phone No of User:"))
                try:
                    for s in Superuser.members_gym:
                        if s == num:
                            Superuser.members_gym.pop(num)
                            print("Deleted User")
                except:
                    print("User doesn't Exist")

            elif select  == 4:
                num = int(input("Enter Phone No of User:"))
                ask = input("Enter if you want to add or remove:")
                if ask == 'add':
                    extend = int(input("Enter for how many do you want to extebd:"))
                    for s in Superuser.members_gym:
                        if s == num:
                            x = member.get_membership_duration()
                            z = x + extend
                            member.set_membership_duration(z)
                            print("Membership Extended")

                elif ask == 'remove':
                    for s in Superuser.members_gym:
                        if s == num:
                            member.set_membership_duration(0)
                            print("Membership Revoked")

            elif select  == 5:
                num = int(input("Enter Phone No of User:"))
                for s in Superuser.regimens:
                    if s == num:
                        for l in Superuser.regimens[s]:
                            Superuser.regimens[s][l] = input(l + ':')

            elif select  == 6:
                num = int(input("Enter Phone No of User:"))
                for s in Superuser.regimens:
                    if s == num:
                        for l, m in Superuser.regimens[s].items():
                            print(l, ':', m)

            elif select  == 7:
                num = int(input("Enter Phone No of User:"))
                for s in Superuser.regimens:
                    if s == num:
                        Superuser.regimens.pop(num)
                        print("Regimen Deleted Sucessfully")

            elif select  == 8:
                num = int(input("Enter Contact No of User:"))
                for s in Superuser.regimens:
                    if s == num:
                        day = input("Enter the day on which you want to update:")
                        for l in Superuser.regimens[s]:
                            if l == day:
                                Superuser.regimens[s][l] = input("Enter the Workout:")
                                print("Updated Sucessfully")

            elif select  == 0:
                break

            else:
                print("Invalid Input")

    elif Memb == 0:
        break

    else:
        print("Invalid Input")
