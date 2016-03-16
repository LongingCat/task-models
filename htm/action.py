import numpy as np


class Condition:
    """Pre or post condition on an environment state.

    Defined by a mask and feature values.
    """

    def __init__(self, mask, value):
        if np.count_nonzero((1 - mask) * value) != 0:
            raise ValueError('Masked values must be zeroed.')
        self.mask = mask
        self.value = value

    def check(self, state):
        return (state.get_features() * self.mask == self.value).all()


class Action:

    def __init__(self, pre_condition, post_condition, name="unnamed-action"):
        self.pre = pre_condition
        self.post = post_condition
        self.name = name

    def check(self, before, after):
        return self.pre.check(before) and self.post.check(after)
