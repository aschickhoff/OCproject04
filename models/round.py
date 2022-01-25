
class Round:
    def __init__(self, round_name, start_time, end_time, matches):
        self.round_name = round_name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    def serialize_round(self):
        return self.__dict__

    @classmethod
    def deserialize_round(cls, serialized_round):
        round_name = serialized_round["round_name"]
        start_time = serialized_round["start_time"]
        end_time = serialized_round["end_time"]
        matches = serialized_round["matches"]
        return Round(round_name, start_time, end_time, matches)
