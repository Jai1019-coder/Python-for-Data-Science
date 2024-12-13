import multiprocessing,sys,time,math

sys.set_int_max_str_digits(1000000)

def computer_factorial(number):
    print(f"Computing factoral of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result
if __name__ == '__main__':
    numbers = [5000,6000,7000,8000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,numbers)
    end_time = time.time()
    print(f"Results = {results}")
    print(f"Time taken : {end_time-start_time}")