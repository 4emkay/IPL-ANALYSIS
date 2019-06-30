import pandas as pd


def matches_(matches):
    print(matches.head())





if __name__ == '__main__':
    matches = pd.read_csv("/home/emkay/PycharmProjects/temp/matches.csv")
    matches_(matches)