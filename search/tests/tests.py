import os

from ojota import set_data_source
from search.forms import ArtistSearchForm, BEST_FIT

# Setup sources for testing (Artists aged 16 to 20)
file_path = (os.path.dirname(os.path.abspath(__file__)))
set_data_source(file_path)


class TestArtistSearch(object):

    def test_best_fit_sort_uniform_sample(self):
        """
            Check Best fit sort works as expected, favouring artist in the middle of the age range

        """

        min_age = 16
        max_age = 20
        middle = (max_age - min_age) / 2 + min_age

        form = ArtistSearchForm(min_age=min_age, max_age=max_age, sort_order=BEST_FIT)
        unordered_artists = form.fetch_results()

        # obtain the distance from the middle from the artists sample and order it
        # It should be a list like [0, 0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3 ,3]
        expected = sorted(abs(a['age'] - middle) for a in unordered_artists)

        # Order by best fit and calculate the distances again
        obtained = [abs(a['age'] - middle) for a in form.sort_by_best_fit(unordered_artists)]

        # Both list should match
        assert expected == obtained, 'Best fit sort order did not favor artist in the middle of age range'

    def test_best_fit_sort_non_uniform_sample(self):
        """
            Best fit should be dictated by age range.
            If the sample is has only elements close to one end of the range, best fit sort should still order the
            artist favoring those closest to the middle of the params and not to the average age in the sample

        """

        min_age = 1
        max_age = 20
        middle = (max_age - min_age) / 2 + min_age

        form = ArtistSearchForm(min_age=min_age, max_age=max_age, sort_order=BEST_FIT)
        unordered_artists = form.fetch_results()

        expected = sorted(abs(a['age'] - middle) for a in unordered_artists)
        obtained = [abs(a['age'] - middle) for a in form.sort_by_best_fit(unordered_artists)]

        assert expected == obtained, 'Best fit sort order did not favor artist in the middle of age range'

    def test_artist_collected_within_age_range(self):
        """
            Make sure we are collecting samples accordingly

        """

        min_age=17
        max_age=19
        form = ArtistSearchForm(min_age=min_age, max_age=max_age, sort_order=BEST_FIT)

        expected = set(range(min_age, max_age + 1))
        obtained = set(a['age'] for a in form.fetch_results())

        assert obtained == expected, 'Artist collected outside age range'

