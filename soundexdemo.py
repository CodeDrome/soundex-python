import soundex

def main():

    """
    Demonstration of the Soundex module, creating lists of name pairs
    and running them through the soundex method before printing results.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Soundex       |")
    print("-----------------\n")

    names1 = ["Johnson", "Adams", "Davis", "Simons", "Richards", "Taylor", "Carter", "Stevenson", "Taylor", "Smith", "McDonald", "Harris", "Sim", "Williams", "Baker", "Wells", "Fraser", "Jones", "Wilks", "Hunt", "Sanders", "Parsons", "Robson", "Harker"]

    names2 = ["Jonson", "Addams", "Davies", "Simmons", "Richardson", "Tailor", "Chater", "Stephenson", "Naylor", "Smythe", "MacDonald", "Harrys", "Sym", "Wilson", "Barker", "Wills", "Frazer", "Johns", "Wilkinson", "Hunter", "Saunders", "Pearson", "Robertson", "Parker"]

    # namecount = len(names1)

    for i in range(0, len(names1)):

        s1 = soundex.soundex(names1[i])
        s2 = soundex.soundex(names2[i])

        print(f"{names1[i]:20s}{s1:4s}  {names2[i]:20s}{s2:4s}")


if __name__ == "__main__":

    main()
