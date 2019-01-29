def main(*args, **kwargs):
    print(list(args))

    print(kwargs)

if __name__ == "__main__":
    main(1, 1, "testing", "testing", name="John", Age=50)
