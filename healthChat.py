import pandas as pandas

# load your data ino a dataframe
df = pandas.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, I am your Health assistance bot. Ask me about your symptoms.")

while True:
    #1. get the user input and store the same intio a variable
    user_text = input("\n You: ").lower()

    # 2. to check if the user whats to exit
    if user_text == "quit":
        print("Healthbot: Goodbye! Nice to have been of service to you. Stay Heakthy")
        break

    # create a variable that will store the details structered in the csv file
    found_answer = False

    # come upwith a loop thatloops through the entire data frame created before.
    for index, row in df.iterrows():
        # clean up the keywords from the csv
        keywords_list = str(row['Keywords']).split(',')

        # below we check every keyword in that given row
        for word in keywords_list:
            clean_word = word.strip().lower()

            # if the keyword is inside of the users sentence
            if clean_word in user_text:
                print("Healthbot:", row["Response"])
                found_answer = True
                break

        if found_answer:
            break # stop looking at other answers
    
    #4. if we went through the entire csv fileand never found any match of the keywords,
    # we need to display a massage to the user
        
    if not found_answer:
        print("Healthbot: Sorry, i don't know that one, Try asking for something else")
