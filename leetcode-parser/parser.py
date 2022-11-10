from github import Github
import os
import shutil
import glob


def parse_to_leetcode(git_repo, myString, source, final_dir, is_root=False):
    if is_root:
        myString = './leetcode-parser/'+myString
    g = Github("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")

    repo = g.get_user().get_repo(git_repo)

    source = '../leetcode-syncs/' + source.split("/")[0]
    file_lists = os.listdir(source)
    for files in file_lists:
        with open(source+"/"+files, 'r') as file:
            content = file.read()

        # Upload to github
        git_prefix = myString + "/" + final_dir + "/"
        git_file = git_prefix + files
        try:
            contents = repo.get_contents(git_file, "main")
            repo.update_file(contents.path, "committing files",
                             content, contents.sha, branch="main")
            print(git_file + ' UPDATED')
        except Exception:
            repo.create_file(git_file, "committing files",
                             content, branch="main")
            print(git_file + ' CREATED')


path = '../leetcode-syncs/*'
counter = 0
hashset = set()
ROMANS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
for filename in glob.glob(os.path.join(path, 'NOTES.md')):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in readonly mode
      for line in f:
        # print(line.rstrip())
        if line != '\u200b':
            myString = line.replace("* ", "").replace("\n", "")
            myString = myString[:1].upper() + myString[1:]
            path = "leetcode-parser/"+myString
            lst = (filename.split("/")[-2]).split("-")
            lst[0] = int(lst[0])

            final_dir = str(lst[0]) + ". " + " ".join([i.upper() if i.upper()
                                                       in ROMANS else i.capitalize() for i in lst[1:]])
            destination = path+"/"+final_dir+"/"
            source = filename.rsplit('/', 2)[-2] + "/"
            try:
                shutil.copytree(source, destination)
                print("Syncing leetcode-syncs...")
                parse_to_leetcode("leetcode-syncs", myString,
                                  source, final_dir, is_root=True)
                print("Syncing leetcode...")
                parse_to_leetcode("leetcode", myString, source, final_dir)
                print("'{}' successfully parsed and placed under topic {}...".format(
                    final_dir, myString))
            except OSError as e:
                pass
