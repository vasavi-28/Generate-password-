import random
print("\U0001F4B0 KAUN BANEGA CROREPATHI \U0001F4B0".center(100))
print("=================================================================================================")
name=input("Enter your name \U0001F600 : ")
print(f"\nWelcome \U0001F44B  to 'KAUN BANEGA CROREPATHI'  . Let's start the game!\n\nGOOD LUCK \U0001F44D {name}!!\n")
print("=================================================================================================")
prize_money=0
questions=[{
    "q": "What stands for AM?",
    "o":["1.Anthro Meridian" , "2.Anthro Median" , "3.Anti Meridian " , "4.Anti Median" , "5.quit"],
    "a":3
},{
    "q":"Which is the capital of TamilNadu?",
    "o":["1.Hyderabad" , "2.Chennai" , "3.Banglore" ,  "4.Pondicherry" , "5.quit"],
    "a":2
},{
    "q":"Which is our National game?",
    "o":["1.Cricket" , "2.Tennis", "3.Chess" , "4.Hockey" , "5.quit"],
    "a":4
},{
    "q":"Who is the captain of Chennai Super Kings in IPL 2024?",
    "o":["1.M S Dhoni" , "2.Rutraj Gaikwad" , "3.Virat Kohli" , "4.Sivam Dube" , "5.quit"],
    "a":2
},{
    "q":"Current Railway Minister of India?",
    "o":["1.Mamta Banarjee", "2.Ram Vilash", "3.Ashwini Vaishnaw", "4.Piyush Goyal" , "5.quit"],
    "a":3
},{
    "q":"Which God is also called as Gauri Nandan?",
    "o":["1.Agni" , "2.Indra" , "3.Hanuman" , "4.Ganesha" , "5.quit"],
    "a":4
},{
    "q":"What doesn't grow on a tree according to a popular hindi saying?",
    "o":["1.Money", "2.Flowers", "3.Leaves", "4.Fruits" , "5.quit"],
    "a":1
},{
    "q":"Which city is known as pink city in India?",
    "o":["1.Banglore", "2.Mysore", "3.Jaipur", "4.Kochi" , "5.quit"],
    "a":3
},{
    "q":"How many religions are there in India?",
    "o":["1.6", "2.7", "3.8", "4.9" , "5.quit"],
    "a":1
},{
    "q":"When is the National Hindi Diwas celebrated?",
    "o":["1.13th sept", "2.14th sept", "3.14th july", "4.15th aug" , "5.quit"],
    "a":2
},{
    "q":"How many states are there in India?",
    "o":["1.28", "2.29", "3.30", "4.31" , "5.quit"],
    "a":1
},{
    "q":"Where in India Gate is located?",
    "o":["1.Agra", "2.Punjab", "3.Jaipur", "4.New Delhi" , "5.quit"],
    "a":4
},{
    "q":"Who wrote Vandhe Matharam?",
    "o":["1.Sarath chandra", "2.Rabindranath Tagore", "3.Bakim Chandra chatterjee", "4.Ishwar Chandra Vidyasagar" , "5.quit"],
    "a":3
},{
    "q":"Which one of the following places is famous for the Great Vishnu Temple?",
    "o":["1.Bordubar,Indonesia", "2.Bamiyab,Afghanisthan", "3.Panja Sahib,Pakisthan", "4.Ankorvat,Combodia" , "5.quit"],
    "a":4
},{
    "q":"The largest Buddhist Monastery in INDIA is located at?",
    "o":["1.Sarnath", "2.Tawang", "3.Dharmashala", "4.Gangtok" , "5.quit"],
    "a":2
}]
a=input("Are you ready to play the game? \U0001F929 (yes/no): ")
random.shuffle(questions)
if a=="yes":
    for question in questions:
        print("\n",question["q"])
        for option in question["o"]:
            print("\n",option)
    
        user_ans=int(input("\nChoose one option: "))
    
        if user_ans==question["a"]:
            print("\nCongratulations! \U0001F44F, Your answer is right \U0001F600 \n")
            print("=================================================================================================")
            prize_money+=1000
        elif user_ans==5:
            ans=input("\nAre you sure to quit this game (yes/no)? \U0001F914 : ")
            if ans=="yes":
                break
        else:
            print("=================================================================================================")
            print("\nwrong answer!\U0001F44E You lose the game....\U0001F622")
            break
    print(f"\nFinally you've won {prize_money} \U0001F4B0")
    print("Thankyou for playing the game".center(100))
else:
    print("Thankyou".center(100))