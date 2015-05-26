from wtforms import Form, IntegerField, HiddenField, validators, ValidationError

from models import Artist

BEST_FIT = 'best-fit'


class GreaterThanOrEqualsTo(object):
    def __init__(self, fieldname, message=None):
        self.fieldname = fieldname
        self.message = message

    def __call__(self, form, field):
        try:
            other = form[self.fieldname]
        except KeyError:
            raise ValidationError(field.gettext(u"Invalid field name '%s'.") % self.fieldname)
        if field.data != '' and field.data < other.data:
            d = {
                'other_label': hasattr(other, 'label') and other.label.text or self.fieldname,
                'other_name': self.fieldname
            }
            if self.message is None:
                self.message = field.gettext(u'Field must be greater than or equals to %(other_name)s.')

            raise ValidationError(self.message % d)


class ArtistSearchForm(Form):
    sort_order = HiddenField(default=BEST_FIT)
    min_age = IntegerField('Min age', [
        validators.required(),
        validators.NumberRange(min=10)
    ])
    max_age = IntegerField('Max age', [
        validators.required(),
        validators.NumberRange(max=120),
        GreaterThanOrEqualsTo('min_age')
    ])

    def fetch_results(self):
        # Should not use _list, but it seems OjotaSet is not JSON serializable
        # I'll see about making a contrib to the project
        return Artist.many(age__gte=self.min_age.data, age__lte=self.max_age.data)._list

    def sort_by_best_fit(self, artists):
        middle = (self.max_age.data - self.min_age.data) / 2 + self.min_age.data
        return sorted(artists, key=lambda a: abs(a['age'] - middle))

    def get_results(self):
        artists = self.fetch_results()

        available_sorts = {
            BEST_FIT: self.sort_by_best_fit
        }

        if self.sort_order.data in available_sorts:
            artists = available_sorts[self.sort_order.data](artists)

        return artists