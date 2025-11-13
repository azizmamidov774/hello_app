from dotenv import load_dotenv
import os 

load_dotenv()
my_veriable = os.getenv('MY_KEY')

print(my_veriable)
# def main():
#     print("Hello from hello!")

# name = "Mamidov"

# if __name__ == "__main__":
#     main()
