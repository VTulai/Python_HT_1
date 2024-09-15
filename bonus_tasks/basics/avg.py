def get_average():
    with open('../files/avg_data.txt', 'r') as file_read:
        data = file_read.readlines()

    obj = data[0].strip('\n')
    values = data[1:]
    values = [float(i) for i in values]

    average = sum(values)/len(values)

    print(f"The average of specified {obj} is '{average}' and max is {max(values)}")


get_average()
