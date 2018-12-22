def main():
        employee = {
                "name": "Venu",
                "employee_id": "10624098",
                "feedback": "none"
        }

        try:
                last_name = employee["last_name"]
        except KeyError:
                print("Error finding last_name")
        
        print("This code executes!")

if __name__ == "__main__":
    main()
