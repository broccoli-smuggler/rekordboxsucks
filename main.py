from xml_helper import XmlHelper


def run():
    xml = XmlHelper("rekord.xml")
    xml.fix_missing_files_with_wrong_ext()
    xml.export_new_library()


if __name__ == "__main__":
    run()
