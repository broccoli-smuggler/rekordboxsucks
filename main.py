from xml_helper import XmlHelper
import flac


def run():
    xml = XmlHelper("rekordbox.xml")
    print(
        "\tWelcome to rekordbox sucks.\n",
        "Please select an option:",
        "1. "
    )

    # xml.change_library_location("/Users/login/Desktop/", "/Users/broccoli/Music/")
    # xml.fix_missing_files_with_wrong_ext()
    xml.export_new_library()


if __name__ == "__main__":
    run()
