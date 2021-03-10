import random as rd
import fonctions as fc
import os

participants=[]


if __name__ == "__main__":

    print("Who are the participants?")
    participant1= input()

    fc.add_participants(participant1)

    print(participants)

    fc.add_more_participants()

    print(participants)

    print("Do you want to add a skill?")

    print(fc.add_competence())

main()