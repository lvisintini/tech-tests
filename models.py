import os

from ojota import Ojota, set_data_source


file_path = (os.path.dirname(os.path.abspath(__file__)))
set_data_source(os.path.join(file_path, "data"))


class Artist(Ojota):
    plural_name = "Artists"
    pk_field = 'uuid'
    required_fields = ("uuid", "age")

    def __repr__(self):
        return "{}, ({})".format(self.uuid, self.age)