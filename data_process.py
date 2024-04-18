#Task 1
import re

def run_report(filename):
    pos_count = 0
    neg_count = 0
    pos_words = r"\b(amazing|enjoy|wonderful|excellent|good|fantastic|memorable|great|enlightening|stunning)"
    neg_words = r"\b(poor|disappointing|lackluster|bad|awful|scarce)"
    p_list = []
    n_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if re.search(pos_words, line, re.IGNORECASE) or re.search(neg_words, line, re.IGNORECASE):
                    p_list = re.findall(pos_words, line, re.IGNORECASE)
                    n_list = re.findall(neg_words, line, re.IGNORECASE)
                    pos_count += len(p_list)
                    neg_count += len(n_list)
            print(pos_count, "positive words mentioned.")
            print(neg_count, "negative words mentioned.")
    except:
        print("An unexpected error occured, please try again!")

#run_report("travel_blogs.txt")



#Task 2
#show average temp for the year
#print the year with the highest average temp



def average_temp_year(*filename):
    first_average = 0
    second_average = 0
    for f_name in filename:
        try:
            with open(f_name, 'r', encoding="utf-8") as file:
                year = ""
                for line in file:
                    temps = re.findall(r",(.|..)°C", line)
                if re.search(r"(2020)", line):
                    for t in temps:
                        first_average += int(t)
                    year = "2020"
                elif re.search(r"2021", line):
                    for te in temps:
                        second_average += int(te)
                    year = "2021"
                if year == "2020":
                    first_average = round(first_average/len(temps), 1)
                elif year == "2021":
                    second_average = round(second_average/len(temps), 1)
                #print(first_average)
        except:
            print("An error has occured, please try again!")
    print(f"The average for the year 2020 is {first_average}°C\nThe average for the year 2021 is {second_average}°C")
    if first_average > second_average:
        print("2020 has the higher average temperature")
    elif second_average > first_average:
        print("2021 has the higher average temperature.")
    else:
        print("The given years have the same average temperature.")
    

average_temp_year("weather_2020.txt", "weather_2021.txt")