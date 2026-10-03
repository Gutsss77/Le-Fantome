from src.agent.agent import LeFantome


def main():

    agent = LeFantome()

    print("Le-Fantome")
    print("Local AI Computer Agent")
    print("Type 'exit' to quit.\n")

    while True:

        command = input("You > ").strip()

        if command.lower() in {"exit", "quit"}:
            print("Closing Le-Fantome")
            break

        if not command:
            continue

        response = agent.process(command)

        print(f"\nLF > {response}\n")


if __name__ == "__main__":
    main()