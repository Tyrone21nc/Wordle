# board = ["⬛ " * 4]
c_board = ["⬜" * 4]


def empty_board(num_of_responses):
    board_list = ["++++++++++++++++++++++++\n", "++++++++++++++++++++++++\n"]
    var = "+                      +\n|                      |\n+                      +\n"
    # The for loop adds the middle part by replacing the second index of the list every time it runs
    for i in range(1, num_of_responses):
        temp = board_list[i]
        board_list[i] = var
        board_list.append(temp)
    # This for loop just prints the board
    for i in range(len(board_list)):
        print(board_list[i], end="")

    return board_list


def change_value(value, board):
    board[1] = list(board[1])
    board[1][0] += value
    length = len(value)
    for i in range(length):
        board[1].remove(" ")
    print(board[0])
    print(), print()
    board[1] = "".join(board[1])
    for i in range(len(board)):
        print(board[i], end="")





if __name__ == "__main__":
    with open("famfued_Q&A.txt") as file:
        data = file.read()

    data = data.split("\n")
    print(len(data))
    new_data = []
    for i in range(len(data)):
        if i % 2 == 0:
            new_data.append(data[i])
    print(new_data)
    # print()
    # # print(data[0])
    # for k in range(len(data[1:])):
    #     ans_q = data[k].split(":")
    #     ans_q = data[k].split(",")
    #     for i in range(len(ans_q)):
    #         ans_q[i] = ans_q[i].strip()
    #     for i in range(len(ans_q)):
    #         ans_q[i] = ans_q[i].split(":")
    #         for j in range(len(ans_q[i])):
    #             ans_q[i][j] = ans_q[i][j].strip()
    # for i in range(len(ans_q)):
    #     print(ans_q[i])
    # print(ans_q)
    # empty_board()






















    """
    COOL STUFF TO THINK ABT
    c, d = [1, 2, 3], [1, 2, 8]
    print(c and d)
    # According to ChatGPT, reason for this is:
    # In Python, the and operator returns the first operand if it 
    # evaluates to False, otherwise, it returns the second operand.
    a = b = [8, 2, 6, 7, 9]
    print(a)
    print(b)
    print(a is b)
    print("changing first value of a")
    a[0] = 5
    print(a)
    print(">> it changes value of b as well")
    print(b)
    print(a is b)
    print("changing second value of b")
    b[1] = 0
    print(a)
    print(">> it changes value of a as well")
    print(b)
    print(a is b)"""

    """
    OTHER COOL STUFF
    string = {0: "some string", 1: "", 2: "third last string"}
    print(string)
    string[1] = "some other string"
    print(string)
    del string[1]
    print(string)


    def reciprocal(num):
        try:
            r = 1 / num
        except:
            print('Exception caught')
            return
        return r

    print(reciprocal(10))
    print(reciprocal(0))
    num = 5
    if num == 5:
        raise ZeroDivisionError('cannot divide')
        # an error actually pops up when num is set to 5
    else:
        print(num)"""







