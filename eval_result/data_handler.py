import json
import argparse
import os

def get_failed_cases_from_txt(txt):
    with open(txt) as txt_file:
        failed_cases = []
        for line in txt_file:
            failed_cases.append(line.strip())
        return failed_cases

def get_failed_cases_from_json(json):
    with open(json) as json_file:
        data = json.load(json_file)
        failed_cases = []
        # iterate json's value
        for case in data["eval"]:
            if data["eval"][case]["base"][0][0] == 'failed' or data["eval"][case]["plus"][0][0] == 'failed':
                failed_cases.append(case)
        return failed_cases

def generate_failed_cases():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True, type=str)
    parser.add_argument("--output", required=True, type=str)
    args = parser.parse_args()
    failed_cases = get_failed_cases_from_json(args.json)
    # write failed cases to file
    with open(f'{args.output}-failed-cases.txt', "w") as f:
        for case in failed_cases:
            f.write(case + "\n")

def compare_two_failed_cases():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file1", required=True, type=str)
    parser.add_argument("--file2", required=True, type=str)
    parser.add_argument("--output", required=True, type=str)
    args = parser.parse_args()
    f1 = get_failed_cases_from_txt(args.file1)
    f2 = get_failed_cases_from_txt(args.file2)

    # compare two failed cases
    f1_set = set(f1)
    f2_set = set(f2)
    f1_not_f2 = f1_set.difference(f2_set)
    f2_not_f1 = f2_set.difference(f1_set)
    # write to file
    with open(f'{args.output}-f1-not-f2.txt', "w") as f:
        for case in f1_not_f2:
            f.write(case + "\n")
    with open(f'{args.output}-f2-not-f1.txt', "w") as f:
        for case in f2_not_f1:
            f.write(case + "\n")


if __name__ == "__main__":
    compare_two_failed_cases()