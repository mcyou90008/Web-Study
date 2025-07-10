import os
import time

frames = [
    "   *   ",
    "   *   \n  * *  ",
    "   *   \n  * *  \n *   * ",
    "   *   \n  * *  \n *   * \n*******",
    "   *   \n  * *  \n *   * \n*******\n *   * ",
    "   *   \n  * *  \n *   * \n*******\n *   * \n  * *  ",
    "   *   \n  * *  \n *   * \n*******\n *   * \n  * *  \n   *   ",
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.5)


if __name__ == "__main__":
    main()

