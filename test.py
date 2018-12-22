def main(**kwargs):
        print("Number of arguments passed : {0}".format(len(kwargs)))
        print("Type of arguments : {0}".format(type(kwargs)))
        print("Contents of arguments:\n{0}".format(kwargs))

if __name__ == "__main__":
    main(first_name = "Venu", last_name = "Kottooru", employee_id = "106224098")
