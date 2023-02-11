import obj as o
import config as c

def main():
    print("In Main")
    b = c.get_test_board()




    print("testing notes")
    print(f"{'Index':5}\t{'chiefs':5}\t{'eagles':5}\t{'owner':20}\t{'note'}")
    # game start
    print(b.get_score(0,0,"Game Start : $25"))
    print(b.get_score(6,0,"Odell Beckham Jr. 17 Yd pass from Matthew Stafford : $25"))
    print(b.get_score(7,0,"Mat Gay PA : $25"))
    print(b.get_score(7,3,"Evan McPherson FG : $25"))
    print(b.get_score(7,3,"End of Q1 : $100"))

    # start of second qtr
    print(b.get_score(13,3,"Cooper Kupp 11 Yd pass from Matthew Stafford (Two-Point Pass Conversion Failed) : $25"))
    print(b.get_score(13,9,"Tee Higgins 6 Yd pass from Joe Mixon : $25"))
    print(b.get_score(13,10,"Evan McPherson Kick : $25"))
    print(b.get_score(13,10,"End of Q2 : $100"))

    # start of 3rd qtr
    print(b.get_score(13,16,"Tee Higgins 75 Yd pass from Joe Burrow : $25"))
    print(b.get_score(13,17,"Evan McPherson PAT : $25"))
    print(b.get_score(13,20,"Evan McPherson FG : $25"))
    print(b.get_score(16,20,"Matt Gay 41 Yd FG : $25"))
    print(b.get_score(16,20,"End of Q3 : $100"))

    # start of 4th Qtr
    print(b.get_score(22,20,"Cooper Kupp 1 Yd pass from Matthew Stafford : $25"))
    print(b.get_score(13,20,"Matt Gay PAT : $25"))
    print(b.get_score(13,20,"Final : $POT"))



if __name__ == "__main__":
    main()

