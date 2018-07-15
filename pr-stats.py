import argparse
import calendar
import datetime
import getpass
import requests


def get_opt():
    parser = argparse.ArgumentParser(
        description="Script for getting a pull request statistics from"
                    "GitHub")
    parser.add_argument("-v", "--version", dest="version", action="version",
                        version="%(prog)s 1.0")
    parser.add_argument("-n", "--number", dest="number", action="store_true",
                        default=False, help="Number of days opened")
    parser.add_argument("-d", "--opend", dest="opend", action="store_true",
                        default=False, help="Day of the week opened")
    parser.add_argument("-o", "--openu", dest="openu", action="store_true",
                        default=False, help="User who opened")
    parser.add_argument("-la", "--lineadd", dest="lineadd",
                        action="store_true", default=False,
                        help="Number of lines added")
    parser.add_argument("-ld", "--linedel", dest="linedel",
                        action="store_true",
                        default=False, help="Number of lines deleted")
    parser.add_argument("-u", "--user", dest="user", type=str, required=True,
                        help="GitHub login")
    parser.add_argument("-r", "--repo", dest="repo", type=str, required=True,
                        help="GitHub repo")
    args = parser.parse_args().__dict__
    args["login"] = input("Username: ")
    args["password"] = getpass.getpass()

    res = requests.get("https://api.github.com/repos/%s/%s/pulls?page="
                       "1&per_page=100" % (args["user"], args["repo"]),
                       auth=(args["login"], args["password"])).json()
    return args, res


def number(res):
    now = datetime.datetime.now().date()
    for i in res:
        title = i["title"]
        date_str = i["created_at"]
        date = datetime.datetime.strptime(date_str,
                                          "%Y-%m-%dT%H:%M:%SZ").date()
        dif = now - date
        print("Pull request with title {0} is opened {1} days".format
              (title, dif.days))


def opened_day(res):
    for i in res:
        title = i["title"]
        date = datetime.datetime.strptime(i["created_at"],
                                          "%Y-%m-%dT%H:%M:%SZ")
        day = calendar.day_name[date.weekday()]
        print("Pull request with title {0} was opened on {1}".format
              (title, day))


def user_open(res):
    for i in res:
        name = i["user"]["login"]
        title = i["title"]
        print("Pull Request with title {0} was opened by "
              "user {1}".format(title, name))


def line_add(args, res):
    for i in res:
        num = str(i["number"])
        resadd = requests.get("https://api.github.com/repos/%s/%s/pulls"
                              "/%s?page=1&per_page=100" %
                              (args["user"], args["repo"], num),
                              auth=(args["login"], args["password"]))
        resadd = resadd.json()
        print("Number of lines added with title {0}: {1}".format
              (i["title"], resadd["additions"]))


def line_del(args, res):
    for i in res:
        num = str(i["number"])
        resdel = requests.get("https://api.github.com/repos/%s/%s/pulls"
                              "/%s?page=1&per_page=100" %
                              (args["user"], args["repo"], num),
                              auth=(args["login"], args["password"]))
        resdel = resdel.json()
        print("Number of lines deleted with title {0}: {1}".format
              (i["title"], resdel["deletions"]))


def process():
    arguments, result = get_opt()
    if arguments["number"]:
        number(result)
    elif arguments["opend"]:
        opened_day(result)
    elif arguments["openu"]:
        user_open(result)
    elif arguments["lineadd"]:
        line_add(arguments, result)
    elif arguments["linedel"]:
        line_del(arguments, result)
    else:
        print("There are no arguments")


process()
