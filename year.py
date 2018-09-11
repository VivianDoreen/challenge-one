#importing the date to get the current date
import datetime
#class that is going to handle the different years of users
class ClassYear():
#function to get the age of the user
    def get_year(self):
        now = datetime.datetime.now().year
        while True:
            try:
                year_born = int(input("Enter your Birth Year"))
                if len(str(year_born)) < 4 or len(str(year_born)) > 4:
                    print("please enter strictly four digits") 
                elif year_born > now:
                    print("Your born year must be less than the current year")
                else:
                    user_age = now - year_born

                    if user_age < 18:
                        return "You are a minor"
                    elif user_age >= 18 and user_age <= 36:
                        return "You are a youth"
                    else:
                        return "You are an elder"
                    break
            except:
                print("Please enter intergers only")
get_method = ClassYear()
print(get_method.get_year())
