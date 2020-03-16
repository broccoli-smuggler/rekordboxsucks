import sys
import getopt
from xml_helper import XmlHelper


def run(argv):
    if len(argv) != 1:
        print('Please provide the rekordbox.xml file')
        return
    try:
        opts, args = getopt.getopt(argv, "h")
    except getopt.GetoptError:
        print('main.py <rekordboxfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py <rekordboxfile>')
            sys.exit()

    xml = XmlHelper(str(sys.argv[1]))

    # xml.change_library_location("/Users/login/Desktop/", "/Users/broccoli/Music/")
    xml.fix_missing_files_with_wrong_ext()
    xml.export_new_library()


if __name__ == "__main__":
    run(sys.argv[1:])
