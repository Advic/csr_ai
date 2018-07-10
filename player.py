from spice import SpiceSet


class Caravan(SpiceSet):
    # todo: might be unnecessary, just make player.caravan implemented as a SpiceSet?
    def __init__(self, *args, **kwargs):
        super(Caravan, self).__init__(*args, **kwargs)
