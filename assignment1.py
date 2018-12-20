def open_file():
    #open the choosen file
    
    file_name = input('Enter filename >')
    file = open(file_name,'r')
    data = file.read()
    data_string = data.splitlines()
    
    return data_string


def clean_and_sorted_the_data(data):
    # clean the useless data in data list 
    
    number_of_message_need_to_clean = 0
    
    # find how many messages need to be clean
    for elements in data:
        position = data.index(elements)
        if elements == '':
            number_of_message_need_to_clean += 1
        elif not elements[0] == 'i': 
            number_of_message_need_to_clean += 1
    
    # sotred the data
    data = sorted(data)
    
    # remove useless messages in the list
    for element in range(number_of_message_need_to_clean):   
        data.remove(data[0])
    
    return data

def get_the_factors_in_data(data):
    # get the necessary factors from the data
    # - monthly_visists: define a dictionary to count how many times of animals visited to both station
    # - station1: a dictionart that save how many times of each animal visited to station1
    # - station2: a dictionart that save how many times of each animal visited to station2
    # - month_list: a list which keep all the data of months of visited
    # - animal_list: a list to save all the animal_id in data list
    # - animal_list_without_repeat: a list only count each animal one time
    
    monthly_visits = {}
    station1 = {}
    station2 = {}
    month_list = []
    animal_list=[]
    animal_list_without_repeat=[]
    
    # split the message in data
    for elements in data: 
        animal_id,coming_date,station = elements.split('#')
        animal_list.append(animal_id)                              # get all animal_id
        month,day,year = coming_date.split('/')
        month_list.append(month)                                   # get all months           
        
    # find how many times for each aniaml visited station1 and station2
        if station == 's1':
            if animal_id in station1:
                station1[animal_id] = station1[animal_id] + 1
            else:
                station1[animal_id] =  1
        else:
            if animal_id in station2:
                station2[animal_id] = station2[animal_id] + 1
            else:
                station2[animal_id] =  1
    
    # keep animal_list only conut each animal one time
    for animal_id in animal_list:
        if not animal_id in animal_list_without_repeat:
            animal_list_without_repeat.append(animal_id)
    animal_list = animal_list_without_repeat

    # add a key and value in particular dictionary if an animal did not visit one of the station
    for animal in animal_list:
        if animal not in station1:
            station1[animal] = 0
        elif animal not in station2:
            station2[animal] = 0 
   
    # find the total number of visits for each month and save it in the dictionary      
    for month in month_list:
        if month in  monthly_visits:
            monthly_visits[month] =   monthly_visits[month] + 1
        else:
            monthly_visits[month] = 1
        
    return animal_list,station1,station2,month_list,monthly_visits


def print_section1(animal_list,station1,station2):
    # print number of each animal visited each station
    # - animal_list : a list keep all the animal's id
    # - station1: a dictionary keep how many times for each animal visited to station1
    # - station2: a dictionary keep how many times for each animal visited to station2
                      
    print('Number of times each animal visited each station',
        '{0:^20}{1:^20}{2:^20}'.format('Animal Id','Station1','Station2'),
        '='*60,sep= '\n')
    # print each animal's id and the times they visited each station
    for animal in animal_list:
        print('{0:^20}{1:^20}{2:^15}'.format('a'+animal[len(animal)-2 : len(animal)],station1[animal],station2[animal]))
     
     

def print_section2(animal_list,station1,station2):
    # print animals that visited both stations at least 4 times
    # - animal_list : a list keep all the animal's id
    # - station1: a dictionary keep how many times for each animal visited to station1
    # - station2: a dictionary keep how many times for each animal visited to station2
    
    print('-'*60,
          'Animals that visited both stations at least 4 times',sep='\n')
    
    # find and print animals that visited both stations at least 4 times
    for animal in animal_list:
        if station1[animal] >= 4 and station2[animal]>= 4:
            print('{0}'.format('a'+animal[len(animal)-2 : len(animal)]))
            

def print_section3(animal_list,station1,station2):
    # print total number of cisits for each animal
    # - animal_list : a list keep all the animal's id
    # - station1: a dictionary keep how many times for each animal visited to station1
    # - station2: a dictionary keep how many times for each animal visited to station2    
    
    print('-'*60,
          'Total Number of visits for each animal',sep='\n')    
    
    # add and print the total number of visits for each animal and their id
    for animal in animal_list:
        print('{0} {1}'.format('a'+animal[len(animal)-2 : len(animal)],station1[animal] + station2[animal]))

def print_section4(month_list,monthly_visits):
    # print the month with the highest number of visits to the station
    # - month_list: a list keep all the data of months of visited
    # - monthly_visits: a dictionary keep the totol number of visits for each month
    
    highest_visits = 0                                             # inital the highest visits number
    highest_visits_month = ''                                       # inital the highest visits month 
    
    # find the month which is highest visited, and the total number of visited 
    for month in  monthly_visits:
        if int( monthly_visits[month]) >= int(highest_visits):
            highest_visits = monthly_visits[month]
            highest_visits_month = month
    
    print('-'*60,
          'The month with the highest number of visits to the stations',sep='\n')
    if not len(month_list) == 0:      
        print('Month',highest_visits_month,'has', highest_visits,'visits')
             

def main():
    data = open_file()
    data = clean_and_sorted_the_data(data)
    animal_list,station1,station2,month_list,monthly_visits = get_the_factors_in_data(data)
    print_section1(animal_list,station1,station2)
    print_section2(animal_list,station1,station2)
    print_section3(animal_list,station1,station2)
    print_section4(month_list,monthly_visits)

main()
