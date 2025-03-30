"""
Author: Romain Dzeinse
Date: 3/16/24
Time: 5:47pm
Objective: Try your best to replicate Family Feud - Steve Harvey's version
Inspiration: I used to watch some Family Feud with my mom, wasn't something that I would tune in for every day,
it was just cool to guess the questions with my mom. I also enjoyed the celebrity edition with the Warriors Team
"""

score = 0
question_type1 = ["Name a place where people tend to lose their keys.", "Name a popular excuse for not exercising.",
                  "Name a food that is commonly deep-fried.",
                  "Name something people often forget to pack when going on vacation."]
t1_q1_correct_answers = {
    "couch": 49,
    "bag": 30,
    "kitchen counter": 15,
    "car": 6
}

board = "⬛ " * (len(t1_q1_correct_answers))





def team_score(team_name, current_score):
    if current_score:
        if current_score == 1:
            return f"🎉{team_name.upper()} have {current_score} point!🎉"
        else:
            return f"🎉{team_name.upper()} have {current_score} points!🎉"
    else:
        return f"😡{team_name.upper()} have {current_score} points!😡"


def type1_first_question():
    print("Question Number 1:", end=" ")
    print(question_type1[0])


def type1_second_question():
    print("Question Number 2:", end=" ")
    print(question_type1[1])


def type1_third_question():
    print("Question Number 3:", end=" ")
    print(question_type1[2])


def type1_fourth_question():
    print("Question Number 4:", end=" ")
    print(question_type1[3])


def the_response(fam1, fam1_members, fam2, fam2_members):
    print(f"Good morning {fam1} team and {fam2} team. \nWelcome to Family Feud")
    type1_first_question()  # This prints the first question
    print("To respond: FX response -> F2 bread")
    response = input(">>> ")
    response = response.split(" ")
    while "1" in response[0] or "2" in response[0]:
        if len(response) == 2:
            if response[1] in t1_q1_correct_answers:
                new_board = board.split(" ")
                place = 0
                num = 0
                for i in t1_q1_correct_answers:
                    if t1_q1_correct_answers[response[1]] == t1_q1_correct_answers[i]:
                        place = num
                    num += 1
                new_board[place] = t1_q1_correct_answers[response[1]]
                new_board.remove("")
                print()
                for i in range(len(new_board)):
                    if new_board[i] == "⬛":
                        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                        print(f"⬜⬜⬜⬜ {new_board[i]} ⬜⬜⬜⬜")
                        print("______________________")
                    else:
                        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                        print(f" \033[32m{response[1]}             {t1_q1_correct_answers[response[1]]}\033[0m")
                        print("______________________")
                print(f"The new board is {new_board}")
        response = input(">>> ")
        response = response.split(" ")
    # elif "2" in response[0]:
    #     pass


if __name__ == "__main__":
    print("\t\t\tWelcome to Family Feud")
    print("Family number 1:", end=" \033[1;33m")
    family1 = "Golden State Warriors"
    family1_members = ["\033[1;33mCurry\033[0m", "\033[1;33mGreen\033[0m", "\033[1;33mWiggins\033[0m",
                       "\033[1;33mThompson\033[0m", "\033[1;33mMcGee\033[0m"]
    score1 = 0
    print(family1, "\033[0m")
    print("Family number 2:", end=" \033[38;2;255;165;")
    family2 = "Cleveland Cavaliers"
    family2_members = ["\033[1;31mJames\033[0m", "\033[1;31mIrving\033[0m", "\033[1;31mSmith\033[0m",
                       "\033[1;31mLove\033[0m", "\033[1;31mShumpert\033[0m"]
    score2 = 0
    print(family2, "\033[0m")
    print()
    print()
    print(f"{family1_members[0]} and {family2_members[0]} please step up to the podium")
    the_response(family1, family1_members, family2, family2_members)








