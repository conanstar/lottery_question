class Lottery:  # A lottery of single issue

    def __init__(self, game_id, issue):
        self.game_id = game_id
        self.issue = issue
        self.winning_number = ''

    def get_game_id(self):
        return self.game_id

    def get_issue(self):
        return self.issue

    def update(self, **kv):
        for key in kv.keys():
            if key == 'winning_number':
                self.winning_number = kv.get(key)
