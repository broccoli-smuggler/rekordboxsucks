import xml.etree.ElementTree as ET
import os
from urllib.parse import unquote
import mutagen

R_FILE_TYPES = {'flac': 'FLAC File', 'mp3': 'MP3 File', 'aiff': 'AIFF File', 'm4a': 'M4A File', 'wav': 'WAV File'}


class XmlHelper(object):
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    @staticmethod
    def _location_to_path(location):
        return unquote(location.replace('file://localhost', ''))

    def _change_element_file_extension(self, element, new_path, new_ext):
        if new_ext not in R_FILE_TYPES:
            return

        if new_ext == 'aiff':
            meta = mutagen.File(new_path).info
            bitrate = int(meta.bitrate / 1000)
            samplerate = meta.sample_rate
            new_location = element.attrib['Location'].split('.')[0] + '.' + new_ext

            element.attrib['Kind'] = R_FILE_TYPES[new_ext]
            element.attrib['BitRate'] = str(bitrate)
            element.attrib['SampleRate'] = str(samplerate)
            element.attrib['Location'] = new_location

            print([a for a in element.attrib.values()])

    def export_new_library(self):
        self.tree.write('new.xml')

    def get_track_elements(self):
        return [t for t in self.root.find('COLLECTION').iter('TRACK')]

    def get_missing_files(self):
        missing = []
        for te in self.get_track_elements():
            fl = self._location_to_path(te.get('Location'))
            if not os.path.isfile(fl):
                missing.append(te)
        return missing

    def fix_missing_files_with_wrong_ext(self):
        missing = self.get_missing_files()

        for miss in missing:
            fl = self._location_to_path(miss.get('Location'))
            pre = fl.split('.')[0]

            for ext in R_FILE_TYPES.keys():
                pre_ext = pre + "." + ext
                if os.path.isfile(pre_ext):
                    print(pre_ext)
                    self._change_element_file_extension(miss, pre_ext, ext)
                    break

    def get_all_tracks_of_type(self, ext='flac'):
        if ext not in R_FILE_TYPES:
            return

        r_type = R_FILE_TYPES[ext]
        tracks = []

        for te in self.get_track_elements():
            if te.get('Kind') == r_type:
                tracks.append(te)
        return tracks
