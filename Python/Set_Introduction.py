def average(array):
    all_values =  set(array)
    average_plants =sum(all_values) / len(all_values)
    
    return average_plants

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
