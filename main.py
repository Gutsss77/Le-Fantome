from le_fantome.agent.agent import LeFantome


def main():
    agent = LeFantome()

    print("👻 Le-Fantome")
    print("Local AI Computer Agent")
    print("Type 'exit' to quit.\n")

    while True:
        command = input("You > ").strip()

        if command.lower() in {"exit", "quit"}:
            print("Goodbye 👻")
            break

        if not command:
            continue

        response = agent.process(command)

        print(f"\nLe-Fantome > {response}\n")


if __name__ == "__main__":
    main()