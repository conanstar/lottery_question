import requests

GAME_ID_INFO = {
    1: {
        'main_src_id': 1,
        'main_src_key': 'ssc',
        'sub_src_id': 2,
        'sub_src_key': 'bjsyxw'
    },
    2: {
        'main_src_id': 2,
        'main_src_key': 'bjsyxw',
        'sub_src_id': 1,
        'sub_src_key': 'bj11x5'
    }
}


class LotteryHandler:
    def __init__(self, lottery):
        self.game_id = lottery.get_game_id()
        self.issue = lottery.get_issue()

    def get_winning_number(self):
        gids = GAME_ID_INFO.keys()
        for gid in gids:
            if gid == self.game_id:
                main_src_id = GAME_ID_INFO[gid]['main_src_id']
                main_src_key = GAME_ID_INFO[gid]['main_src_key']
                sub_src_id = GAME_ID_INFO[gid]['sub_src_id']
                sub_src_key = GAME_ID_INFO[gid]['sub_src_key']

                main_win_num = self._get_from_src(main_src_id, main_src_key)
                sub_win_num = self._get_from_src(sub_src_id, sub_src_key)

                if main_win_num == sub_win_num:
                    return main_win_num
                else:
                    raise FetchFailureException()

    def _get_from_src(self, src_id, game_key):
        if src_id == 1:
            self._get_number_from_src_id_1(game_key)
        elif src_id == 2:
            self._get_number_from_src_id_2(game_key)
        else:
            raise FetchFailureException()

    def _get_number_from_src_id_1(self, game_key):
        url = 'http://one.fake/v1'
        params = {'gamekey': game_key, 'issue': self.issue}
        r = requests.get(url, params)

        if r.status_code == 200:
            data = r.json()['result']['data']
            for d in data:
                if d['gid'] == self.issue:
                    return d['award']
            return ''

        else:
            raise FetchFailureException()

    def _get_number_from_src_id_2(self, game_key):
        url = 'https://two.fake/newly.do'
        params = {'code': game_key}
        r = requests.get(url, params)

        if r.status_code == 200:
            data = r.json()['data']
            for d in data:
                if d['expect'] == self.issue:
                    return d['opencode']
            return ''

        else:
            raise FetchFailureException()


class FetchFailureException(Exception):
    pass
