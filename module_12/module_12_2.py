class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)


    # def start(self):
    #     finish_times = {}
    #     place = 1# тут храним время которое потребуется участникам на дистанцию
    #     for participant in self.participants:
    #         time_finish = self.full_distance / participant.speed
    #         finish_times[str(participant)] = time_finish
    #     sorted_finishers = sorted(finish_times.items(), key=lambda x:x[1]) # сортируем от быстрова к медленому
    #
    #     finishers = {}
    #     for finisher in sorted_finishers: # раздаем занятые места согласно скорости бегуна
    #         finishers[place] = finisher[0]
    #         place +=1

        return finishers
