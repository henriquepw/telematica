class Sample(object):

    def __init__(self, cube, shuffle, steps):
        self.cube = cube
        self.steps = steps
        self.shuffle = shuffle

    def __str__(self):
        print('Cube: ' + str(self.cube))
        print('Shuffle: ' + str(self.shuffle))
        print('Steps: ' + str(self.steps))
