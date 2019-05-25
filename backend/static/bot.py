from pypokerengine.players import BasePokerPlayer
from pypokerengine.api.game import setup_config, start_poker
import pprint

class Dorel(BasePokerPlayer):
    def declare_action(self, valid_actions, hole_card, round_state):
        call_action_info = valid_actions[1]
        action, amount = call_action_info["action"], call_action_info["amount"]
        return action, amount   # action returned here is sent to the poker engine

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass

conf = setup_config(max_round=10, initial_stack=100, small_blind_amount=10, ante=1)
conf.register_player("gigel", Dorel())
conf.register_player("matache", Dorel())
conf.register_player("mitica", Dorel())
conf.register_player("gogaie", Dorel())
res = start_poker(conf, verbose=1)

pretifier = pprint.PrettyPrinter(indent=4)
pretifier.pprint(res)
