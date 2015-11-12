from ojota import Ojota


class Artist(Ojota):
    plural_name = "Artists"
    pk_field = 'uuid'
    required_fields = ("uuid", "age")

    def __repr__(self):
        return "{}, ({})".format(self.uuid, self.age)